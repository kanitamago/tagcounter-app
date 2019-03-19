from app import app
from app.scripts.tag_counter import TagCounter
from flask import render_template, url_for, redirect, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def show_result():
    if request.method == "POST":
        try:
            try:
                fileobj = request.files["file-data"]
                data = fileobj.read().decode("utf-8")
                csv_check = request.form["csv-check"]
                create_file = bool(int(csv_check))
                tag_obj = TagCounter(data, create_file=create_file)
                output_text, image_path, csv_path = tag_obj.counter()
            except:
                data = request.form["text-data"]
                csv_check = request.form["csv-check"]
                create_file = bool(int(csv_check))
                tag_obj = TagCounter(data, create_file=create_file)
                output_text, image_path, csv_path = tag_obj.counter()
            return render_template("result.html", output_text=output_text, image_path=image_path, csv_path=csv_path)
        except:
            return render_template("result.html", output_text=None, image_path=None, csv_path=None)
    return redirect(url_for("index"))
