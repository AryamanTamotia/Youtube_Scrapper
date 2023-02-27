from flask import Flask, render_template
from flask_cors import CORS,cross_origin
import csv

application = Flask(__name__)
app=application


csv_filename = 'Youtube_Scrapper.csv'

details=[]

with open(csv_filename,'r') as data:
    for line in csv.reader(data):
        mydict = {"Index": line[0], "URL": line[1], "Thumbnail": line[2], "Title": line[3], "Views": line[4], "Time": line[5]}
        details.append(mydict)


@app.route("/")
@cross_origin()
def home():
	return render_template('result.html',details=details)

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
	#app.run(debug=True)