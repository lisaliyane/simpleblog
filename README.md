# simpleblog - what is it?

It is a super simple web application blog system, which includes 2 functionalities:
1. List all blog posts dynamically
2. Post a new blog post

It only includes 2 files with dozens of lines of code: 
1. blog.py
2. templates/template.html

# How does it work?
It is for practising below technologies:
1. Python Flask: the lightweight Python web application framework, for controller implementation and template rendering
2. SQLAlchemy: ORM to SQLite db
3. HTML & Javascript: submit request with form data to backend

and it is super simple to be deployed in your system:
1. clone the Git project
2. create SQLite db objects before run the system
```jsonc
from blog import app, db
with app.app_context():
    db.create_all()
```
3. run the system by the command:
```jsonc
python3 blog.py
```
Enjoy!
