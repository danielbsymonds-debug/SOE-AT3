import os

class Config:
    SECRET_KEY = "supersecretkey123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///smartcampus.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False