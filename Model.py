
import decimal
import pandas as pd
import mysql.connector

import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

class Model :

    def dayOfweek(self):

          df = pd.read_csv("acdents.csv")
          df.columns = ["X1", "X2", "X3", "X4","X5","X6","X7","X8","X9","X10","X11","X12","X13", "Y"]
          df.head()
          decision = tree.DecisionTreeClassifier(criterion="gini")
          X = df.values[:, 0:13]
          Y = df.values[:, 13]
          trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.5)
          decision = decision.fit(trainX, trainY)
          decision.predict([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
          return (decision.score(testX, testY))

    def mysqlResult(self, day_of_week, weather, light_condition, road_surface_condition, validity_of_license, vehicle_pre_crashfactors, alchohol, ds_division, Work_day_holiday, driver_age, gender):
        day_of_weeks = {"Sunday": "1", "Monday": "2", "Tuesday": "3", "Wednesday": "4", "Thursday": "5" , "Friday": "6" , "Saturday": "7"}
        weathers = {"Clear": "1", "Cloudy": "2", "Rainy": "3", "Fogg/Mist": "4", "Other": "9" , "Not Known": "0"}
        light_conditions = {"DayLight": "1", "Night, No Street lamps": "2", "Dusk,Dawn": "3", "Night, Improper street lightning": "4", "Night, Good street lighting": "5" , "Not Known": "0"}
        road_surface_= {"Dry": "1", "Wet": "2", "Flooded with water": "3", "Slippery Surface": "4", "Other": "9" , "Not Known": "0"}
        validity_license_= {"International license": "5", "Probation license": "4", "Learner Permit": "3", "No valid license for vehicle": "2", "Valied license": "1" , "Not Known": "0"}
        vehicle_pre_crashfactor= {"Other,Not Known": "9", "Over loaded or wrongly loaded vehicle": "6", "Poor mechanical condition": "5", "Lights, Lamps": "4" , "Steering": "3", "Tyres": "2", "Brakes": "1"}
        alchohol_test_= {"Not tested": "3", "Over leagal limit": "2", "No Alchohol": "1"}
        ds_divisions_= {"Ampara": "1", "Anuradhapura": "2", "Badulla": "3", "Slippery Surface": "4", "Other": "9", "Not Known": "0",  "Not Known": "0"}
        Work_day_holidays = {"Work Day": "1", "Holiday": "2"}
        Driver_gender_= {"Male": "1", "Female": "2"}





        # Setup MySQL connection
        db = mysql.connector.connect(
            host="localhost",  # your host, usually localhost
            user="root",  # your username
            password="R1327526",  # your password
            database="accidents"  # name of the data base
        )

        # You must create a Cursor object. It will let you execute all the queries you need
        cur = db.cursor()

        # Use all the SQL you like
        # cur.execute("SELECT * FROM accident WHERE DayofWeek = " + day_of_weeks[day_of_week] + "AND Weather = 1")
        cur.execute("SELECT * FROM accidents.accident WHERE DSDivision = 6 and Weather = 2")

        # Put it all to a data frame
        df = pd.DataFrame(cur.fetchall())
        df.columns = cur.column_names

        # Close the session
        db.close()

        # Show the data
        df.head()
        decision = tree.DecisionTreeClassifier(criterion="gini")
        X = df.values[:, 0:13]
        Y = df.values[:, 13]
        trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.5)
        decision = decision.fit(trainX, trainY)
        decision.predict([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
        # return (day_of_weeks[day_of_week])
        return (decision.score(testX, testY))

