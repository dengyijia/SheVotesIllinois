
from flask import Flask, render_template_string, redirect, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, MetaData
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_blogging import SQLAStorage, BloggingEngine
import json, datetime


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


###############################################################
############################ BLOG #############################
###############################################################

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
# this engine is the one running off the remotemysql.com free online MySQL database
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
        return "Ruth Bader Ginsburg"  # typically the user's name

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

"""
print(sql_storage.get_posts())

[{'post_id': 4, 'title': 'SVI Going Rogue', 'text': 'A small project team at the **university of chicago** has gone rogue and is operating without oversight from the IOP. More at 11.', 
                'post_date': datetime.datetime(2020, 4, 24, 23, 31, 19), 'last_modified_date': datetime.datetime(2020, 4, 24, 23, 31, 19), 
                'draft': 0, 'user_id': 'testuser', 'tags': ['TAGS', 'AND', 'SOME', 'MORE']}, 
{'post_id': 3, 'title': 'Should Look Like a Title', 'text': 'Body text and more and more body text', 
                'post_date': datetime.datetime(2020, 2, 23, 19, 41, 51), 'last_modified_date': datetime.datetime(2020, 2, 23, 19, 41, 51), 
                'draft': 0, 'user_id': 'testuser', 'tags': ['COMMA', 'SEPARATED', 'TAGS']}, 
{'post_id': 2, 'title': 'Office Hours', 'text': '6-7 in ryerson 60 9  ', 
                'post_date': datetime.datetime(2020, 1, 25, 17, 49, 56), 'last_modified_date': datetime.datetime(2020, 1, 25, 17, 49, 56), 
                'draft': 0, 'user_id': 'testuser', 'tags': ['DSAFDSF']}]

posts is a list of dicts, fields are:
post_id, title, text, post_date, last_modified_date, draft, user_id, testuser, tags
 """

def read_posts(storage, path):
    posts = storage.get_posts() #gets the last 10 posts as a list of dicts

    blog_posts = {} # (title, dict)
    
    for p in posts:
        p['post_year'] = str(p['post_date'].year)
        p['post_month'] = str(p['post_date'].month)
        p['post_day'] = str(p['post_date'].day)
        p['last_mod_year'] = str(p['last_modified_date'].year)
        p['last_mod_month'] = str(p['last_modified_date'].month)
        p['last_mod_day'] = str(p['last_modified_date'].day)
        try:
            del p['post_date']
            del p['last_modified_date']
        except Exception as e:
            pass

        blog_posts[p['title'].replace(' ','_')] = p

    with open(path, mode='w') as f:
        #print(str(blog_posts).strip('"\''), file=f)
        json.dump(blog_posts, f)

    return

###############################################################
########################## END BLOG ###########################
###############################################################

if __name__ == '__main__':
    path = "../shevotesillinois/src/assets/blog_posts.json"
    read_posts(sql_storage, path)
    #app.run(debug=True, port=8000, use_reloader=True)
