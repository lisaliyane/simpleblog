from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#create a Flask web application instance, and assign it to the app variable. The _name_ argument represents the name of the current module.
app = Flask(__name__)
# set the configuration for the Flask application to use a SQLite db named blog.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
#create SQLAlchemy object db, and bind it to the Flask application. This object acts as the intermediary between the Flask application and the database, which allow you to interact with the db with SQLAlchemy's ORM functionality.
db = SQLAlchemy(app)

#create a blogpost model using SLQAlchemy's declarative syntax. It inherits from SQLAlchemy.Model, which is the base class for defining models
class blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createtime = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

#define controller, list all blog items when visit home page 
@app.route('/')
def home():
    # Render the home page with blog posts
    result = blogpost.query.all()
    return render_template('template.html', page_list=result)

#define controller, get the form data and insert the blog item into db
@app.route('/api/submit',methods=['POST'])
def new_post():  
    content=request.form['blogcontent']
    post = blogpost(createtime=datetime.now(), content=content)
    db.session.add(post)
    db.session.commit()
    return "done"

if __name__ == '__main__':
    #start web service, the default port is 5000
    app.run(debug=True)
