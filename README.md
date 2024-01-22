# simpleblog - what is it?

It is a super simple web application blog system, which includes 2 functionalities:
1. List all blog posts dynamically
2. Post a new blog post

It only includes 2 files with dozens of lines of code: 
1. blog.py
2. templates/template.html

# How does it work?
It is for practising below technologies:
* `Python Flask`: the lightweight Python web application framework, for controller implementation and template rendering
* `SQLAlchemy`: ORM to SQLite db
* `HTML & Javascript`: submit request with form data to backend

and it is super simple to be deployed in your system:
1. Clone the Git project
2. Create SQLite db objects before run the system. It will create a subfolder with name 'instance' and a .db file.
```jsonc
from blog import app, db
with app.app_context():
    db.create_all()
```

3. Run the system by the command:
```jsonc
python3 blog.py
```
Enjoy!
