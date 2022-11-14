from flask import Flask, redirect, url_for
import json
import sys

f = open('q_a.json')
data = json.load(f)
print(data["Question 1"])


sys.exit()

app = Flask(__name__)

@app.route('/')
def hello_world(): 
	return 'Hello world <h1>Sebastien Boulas</h1>'

@app.route("/<name>")
def user(name): 
	return f"Hello {name}! "

@app.route("/admin")
def admin(): 
	return redirect(url_for("hello_world"))

if __name__ == '__main__': 
	app.run()