from flask import Flask, redirect, url_for, render_template
import json
import sys

# f = open('q_a.json')
# data = json.load(f)
# print(data["Question 1"])



app = Flask(__name__, template_folder='templates')

@app.route('/')
def home(): 
	return render_template('home.html')

@app.route("/<name>")
def user(name): 
	return f"Hello {name}! "

@app.route("/admin")
def admin(): 
	return redirect(url_for("hello_world"))

if __name__ == '__main__': 
	app.run()