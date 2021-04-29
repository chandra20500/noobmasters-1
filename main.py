import flask
import numpy as np
from flask import jsonify
from flask import request
from operator import add
import json
import pandas as pd

app = flask.Flask("__main__")

@app.route('/')
def my_index():
	return flask.render_template("index.html",token = "hello world")

@app.route('/result', methods = ['POST'])
def result():
	json_data = request.get_json()
	movies = json_data['movie']
	result = []

	if len(movies) < 5:
		error_msg = ["Something is wrong!!! please check if you have selected atleast 5 movies"]
		return json.dumps(error_msg)
	if len(movies) > 5:
		error_msg = ["Something is wrong!!! please do not select more than 5 movies"]
		return json.dumps(error_msg)

	m1 = movies[0]
	m2 = movies[1]
	m3 = movies[2]
	m4 = movies[3]
	m5 = movies[4]

	for i in range(18):
		result.append(m1[i] + m2[i] + m3[i] + m4[i] + m5[i])
	
	f = open('data2.json',)

	return_metric = pd.DataFrame(columns=['name', 'dot_product'])
	return_metric.head()

	data = json.load(f)
	for i in data['movies']:
	  return_metric.loc[len(return_metric.index)] = [i['name'], np.dot(i['genres'],result)]
	
	final_metric = return_metric.sort_values(by = 'dot_product', ascending = False)
	arr = []

	df = final_metric.head(10)
	
	for i in df.index:
	  arr.append(df['name'][i])

	jsonString = json.dumps(arr)
	return jsonString

app.run(debug=True)