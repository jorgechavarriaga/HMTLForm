"""
*************************************************************************
*    Course: 100 Days of Code - Dra. Angela Yu                          *
*    Author: Jorge Chavarriaga                                          *
*    Day: 60 - html form                                                *
*    Date: 2021-01-31                                                   *
*************************************************************************
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def get_all_posts():

    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_data():
    user = request.form['username']
    pwd = request.form['password']
    data = f"<h1>Welcome {user}</h1>" \
           f"<h2>Password: {pwd}</h2>"
    return data


if __name__ == "__main__":
    app.run(debug=True)