from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as time
from application import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin

# reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# class: a table in the database
class User(db.Model, UserMixin):
        
        __tablename__ = 'user'
        __table_args__ = {'sqlite_autoincrement': True}

        # account data
        id = db.Column(db.Integer, nullable = False, primary_key = True, unique = True)
        username = db.Column(db.String(70), unique = True, nullable = False)
        email = db.Column(db.String(120), unique = True, nullable = False)
        creationdate = db.Column(db.DateTime, nullable = False, default = time.utcnow)

        # profile pictures and passwords are hashed
        profilepic = db.Column(db.String(20), nullable = False, default = 'profile.jpg')
        password = db.Column(db.String(60), nullable = False)

        # user service data
        debttype = db.Column(db.String(30), nullable = False)
        income = db.Column(db.String(12), nullable = False)
        savings = db.Column(db.String(12), nullable = False)
        interestrate = db.Column(db.String(12), nullable = False)
        savingsyield = db.Column(db.String(12), nullable = False)
        debt = db.Column(db.String(12), nullable = False)
        objective = db.Column(db.String(12), nullable = False)
        rent = db.Column(db.String(12), nullable = False)
        transport = db.Column(db.String(12), nullable = False)
        food = db.Column(db.String(12), nullable = False)
        bills = db.Column(db.String(12), nullable = False)
        shopping = db.Column(db.String(12), nullable = False)
        extra = db.Column(db.String(12), nullable = False)

        def __repr__(self): # representation
                return f"'{self.id}'"

        def __str__(self): # object to string
                return f"User '{self.username}': email = '{self.email}', profile pic = '{self.profilepic}', created on '{self.creationdate}'"

