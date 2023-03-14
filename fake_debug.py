from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import sys
from faker import Faker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)


with app.app_context():
    db.create_all()
    # Your code that uses Flask objects goes here
    n = 705
    faker = Faker()
    for i in range(n):
        user = User(
            name=faker.name(),
            age=random.randint(20, 80),
            address=faker.address().replace("\n", ", "),
            phone=faker.phone_number(),
            email=faker.email(),
        )
        db.session.add(user)
    db.session.commit()
    print(f"Added {n} fake users to the database.")
