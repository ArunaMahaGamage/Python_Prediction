#Starting implementation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#%matplotlib inline
from sklearn import tree
from sklearn.model_selection import train_test_split

#from __future__ import division
from flask import Flask, render_template ,request, redirect, url_for
app = Flask(__name__)


from flaskext.mysql import MySQL

from Model import Model

app = Flask(__name__)


decision = 0.0


@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route('/result' ,  methods=['GET', 'POST'])
def result():

   if request.method == 'POST':
      day_of_week = request.form['day_of_week']
      weather = request.form['weather']
      light_condition = request.form['light_condition']
      road_surface_condition = request.form['road_surface_condition']
      validity_of_license = request.form['validity_of_license']
      vehicle_pre_crashfactors = request.form['vehicle_pre_crashfactors']
      alchohol = request.form['alchohol']
      ds_division = request.form['ds_division']
      Work_day_holiday = request.form['Work_day_holiday']
      driver_age = request.form['driver_age']
      gender = request.form['gender']
      if gender == 'Male':
         gender = "Male"
      elif gender == "Female":
         gender = "Female"

      if day_of_week is not "Select":
         model = Model()
         x = model.dayOfweek()
         # return redirect(url_for('success', name = day_of_week + " " + weather + light_condition + " " + road_surface_condition + " " + validity_of_license + " " + vehicle_pre_crashfactors + " " + alchohol + " " + ds_division + " " + Work_day_holiday + " " + driver_age + " " + gender + " " + x))
         return redirect(url_for('success', name =  x))


@app.route('/success/<name>')
def success(name):
   return render_template('index.html', name = name)
   # return 'Welcome %s' % name

if __name__ == '__main__':
   app.run(debug = True, port=8090)
