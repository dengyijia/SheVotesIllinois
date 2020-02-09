from flask import Flask, render_template_string, redirect
from sqlalchemy import create_engine, MetaData
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_blogging import SQLAStorage, BloggingEngine
import os
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
app.config["BLOGGING_URL_PREFIX"] = "/blog"
app.config["BLOGGING_DISQUS_SITENAME"] = "test"
app.config["BLOGGING_SITEURL"] = "http://localhost:8000"
app.config["BLOGGING_SITENAME"] = "My Site"
app.config["BLOGGING_KEYWORDS"] = ["blog", "meta", "keywords"]
app.config["FILEUPLOAD_IMG_FOLDER"] = "fileupload"
app.config["FILEUPLOAD_PREFIX"] = "/fileupload"
app.config["FILEUPLOAD_ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg", "gif"]

# extensions
# this engine is the one I used on my own laptop
# engine = create_engine('mysql+mysqldb://dom:nematode@localhost:3306/shevotes')
# this engine is the one running off the remotesql.com free online MySQL database
engine = create_engine('mysql+mysqldb://5OYt9U79fX:slcIdrLwMQ@remotemysql.com:3306/5OYt9U79fX')
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(app, sql_storage)
login_manager = LoginManager(app)
meta.create_all(bind=engine)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_name(self):
        return "Paul Dirac"  # typically the user's name

@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)

index_template = """
<!DOCTYPE html>
<html>
    <head> </head>
    <body>
        {% if current_user.is_authenticated %}
            <a href="/logout/"> Logout </a>
        {% else %}
            <a href="/login/"> Login </a>
        {% endif %}
        &nbsp&nbsp<a href="/blog/"> Blog </a>
        &nbsp&nbsp<a href="/blog/sitemap.xml">Sitemap</a>
        &nbsp&nbsp<a href="/blog/feeds/all.atom.xml">ATOM</a>
        &nbsp&nbsp<a href="/fileupload/">FileUpload</a>
    </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(index_template)

@app.route("/login/")
def login():
    user = User("testuser")
    login_user(user)
    return redirect("/blog")

@app.route("/logout/")
def logout():
    logout_user()
    return redirect("/")

def format_date(date):
    m = date.month
    d = date.day
    y = date.year

    months = ["January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"]

    return "{} {}, {}".format(months[m], d, y)

path = "../../shevotesillinois/src/assets/"

# reads posts from sql storage, saves metadata to blog_posts.json
# saves posts themselves as markdown files in assets/blog_posts

# print(sql_storage.get_posts())
#[{'post_id': 2, 'title': 'Office Hours', 'text': '6-7 in ryerson 60', 
# 'post_date': datetime.datetime(2020, 1, 25, 17, 49, 56), 
# 'last_modified_date': datetime.datetime(2020, 1, 25, 17, 49, 56), 
# 'draft': 0, 'user_id': 'testuser', 'tags': ['DSAFDSF']}]

def read_posts(storage):
    posts = storage.get_posts() #gets the last 10 posts as a list of dicts
    blog_posts = {} #the dict to be saved as blog_posts.json
    blog_texts = {} #dict with same format, year keys list of dict values, 
                    #entries are dict of titles (strings) and articles (strings), 
                    #where each article str is to be saved as a .md in assets/blog_posts
    
    years = [] #unique years posts come from, subfolders of blog_posts
    for p in posts:
        year = str(p['post_date'].year)
        if not (year in years): years.append(year)
    for y in years: 
        blog_posts[y] = []
        blog_texts[y] = []

    for p in posts:
        print("\n post: \n", p)
        metadata = {
            'id': str(p['post_id']), 
            'date': format_date(p['post_date']),
            'title': p['title']
            #'slug': str(p['slug'])
            #'description': '' # sql doesnt have description field
        }
        blog_posts[str(p['post_date'].year)].append(metadata)
        blog_texts[str(p['post_date'].year)].append({'filename': str(p['post_id'])+'.md', 'text': p['text']})

    #print("\nblog posts: \n", blog_posts)
    #print("\nblog texts: \n", blog_texts)

    with open("../../shevotesillinois/src/assets/blog_posts.json", mode='w') as f:
        #print(str(blog_posts).strip('"\''), file=f)
        json.dump(blog_posts, f)
    for y in years:
        try:
            os.mkdir("../../shevotesillinois/src/assets/blog_posts/"+y)
        except Exception as e:
            print(e)
    for y, ps in blog_texts.items():
        path = "../../shevotesillinois/src/assets/blog_posts/"+y+"/"
        for post in ps:
            with open(path+post['filename'], 'w') as f:
                print(post['text'], file=f)

        

if __name__ == "__main__":
    read_posts(sql_storage)
    app.run(debug=True, port=8000, use_reloader=True)
    #print(type(sql_storage))
    #print("Num posts: {}".format(sql_storage.count_posts()))
    
    
