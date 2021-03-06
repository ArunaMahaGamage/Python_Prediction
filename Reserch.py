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
         try :
            model = Model()
            # x = model.dayOfweek()
            x = model.mysqlResult(day_of_week, weather, light_condition, road_surface_condition, validity_of_license, vehicle_pre_crashfactors, alchohol, ds_division, Work_day_holiday, driver_age, gender)
            # return redirect(url_for('success', name = day_of_week + " " + weather + light_condition + " " + road_surface_condition + " " + validity_of_license + " " + vehicle_pre_crashfactors + " " + alchohol + " " + ds_division + " " + Work_day_holiday + " " + driver_age + " " + gender + " " + x))
            y = percentage(x,100)
            return redirect(url_for('success', name =  (y), percentage = "%"))
         except ValueError:
            return redirect(url_for('success', name=("0.0") , percentage = "%"))

def percentage(part, whole):
  return 100 * float(part)

@app.route('/success/<name> <percentage>')
def success(name,percentage):
   return render_template('index.html', name = name, percentage = percentage)
   # return 'Welcome %s' % name

if __name__ == '__main__':
   app.run(debug = True, port=8090)
