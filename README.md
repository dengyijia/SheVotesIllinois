# SheVotesIllinois Website Development

This is the git repository for the She Votes Illinois project team of TechTeam at Institute of Politics. We aim to build a more impactful and accessible website for the statewide political action committee She Votes Illinois. In particular, we look forward to adding more dynamic components for the website, implementing a blogging section, enabling translation between Engliash and Spanish, and making donations easier.

We started this project in November 2019. So far we have constructed a basic prototype for the home page and a server that supports blogging functions.

We are using Vue.js on the frontend and flask on the backend. The frontend files can be found under the "shevotesillinois" directory, and the backend files are under "server".

To take a look of the current frontend on your local server, run "npm install" under shevotesillinois, and run "npm run serve". To run the backend, enter "run app.py" in the server directory.


## Functionality Implemented (All Features Work in Progress):

* Working navbar holding site map

* Volunteer page

* Newsletter page: Basic functionality -- listing current posts

* Who We Are page: Clickable photos that give information about SVI personnel

* Legislation Recap


## How to run:

### Requirements:

The quick start guide assumes you have the following:

* A Python 3 installation on your computer, 3.7 and up will do https://www.python.org/downloads/

* NPM (and thus Node.js) https://www.npmjs.com/get-npm

* MySQL installed on your computer https://dev.mysql.com/ (Requirement to be done away with soon)


### Quick Start Guide

1) Create a new virtual environment with pip, following the guide here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

2) From your command line, enter `pip install -r requirements.txt` in the `server` directory. This will set up your python environment to run the flask server.

3) You are now ready to run the server, and can do so by running `py app.py`

4) The next step is to run NPM to serve packages on the client side that we need to use in the project. You can do this by first running 

`npm install`

Then

`npm run serve --fix`

The --fix option is to fix any lint errors that might be caused by your editor's formatting if you open the files and edit them. Always run with this option.


5. With both npm running and flask, the website is up with its full interactivity. Open the link Flask gives you from running app.py to add and edit blog/event entries (see blog entries below). Open the link npm gives you to see the client facing side of the website. 


### Adding and Editing Blog Posts 

1) First, open the link flask gives you to open the link to the server site. It should be something along the lines of http://127.0.0.1:8000/ if not exactly that. 

2) Then, in the top left corner, click "Login". This should take you the Blog Posts page. Click a post to view its contents and edit it, or "New" to create a new post.

3) More functionality to this feature coming soon.





