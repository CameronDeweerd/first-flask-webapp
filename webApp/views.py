from webApp import app
from flask import Blueprint, render_template, request, redirect
from webApp import weight_check


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "POST":
        if not request.form.get("weights"):
            return render_template("weight.html")


        targets = request.form.get("weights")

        a_list = targets.split()
        map_object = map(int, a_list)
        targets = list(map_object)
        print(targets)
        # targets = [120, 55, 110, 140, 90, 85, 85]
        final_group, final_options = weight_check.make_groups(targets)


        return render_template("weight.html", final_group=final_group, final_options=final_options)
    else:
        return render_template("weight.html")
