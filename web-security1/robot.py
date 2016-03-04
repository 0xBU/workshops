#!/usr/bin/python
from flask import Flask, request, json, session
from subprocess import check_output

app  = Flask(__name__)

@app.route('/robot/<path:task>', methods=['GET'])
def robot_task(task):
	print("python " + task + ".py")
	r = check_output("python " + task + ".py", shell=True)
	return r

app.run(host='127.0.0.1', port=5000, debug=True)

