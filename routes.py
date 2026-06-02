from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Truyen

def regis_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")