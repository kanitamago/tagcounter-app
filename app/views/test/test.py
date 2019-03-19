from app import app
from flask import render_template, redirect, url_for

@app.route("/")
def test_index():
    return render_template("test/test.html")

@app.route("/result")
def test_result():
    return "Success Test."
