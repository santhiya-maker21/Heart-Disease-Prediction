from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session
from flask import render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow

import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route('/homepage', methods =['GET', 'POST'])
def homepage():
    return render_template('index.html')
	
@app.route('/classification', methods =['GET', 'POST'])
def classification():
    return render_template('classification.html')

@app.route('/graph', methods =['GET', 'POST'])
def graph():
    return render_template('graph.html')

@app.route('/predict', methods =['GET', 'POST'])
def predict():
    msg = ''
    if request.method == 'POST' and 'age' and 'sex' and 'cp' and 'trestbps' and 'chol' and 'fbs' and 'restecg' and 'thalach' and 'exang' and 'oldpeak' and 'slope' and 'ca' and 'thal' in request.form :
        s1 = request.form['age']
        s2 = request.form['sex']
        s3 = request.form['cp']
        s4 = request.form['trestbps']
        s5 = request.form['chol']
        s6 = request.form['fbs']
        s7 = request.form['restecg']
        s8 = request.form['thalach']
        s9 = request.form['exang']
        s10 = request.form['oldpeak']
        s11 = request.form['slope']
        s12 = request.form['ca']
        s13 = request.form['thal']
        dataset = pd.read_csv('dataset.csv')
        y = dataset['target']
        X = dataset.drop(['target'], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 0)
        knn = KNeighborsClassifier(n_neighbors=7)
        knn.fit(X_train, y_train)
        Y_pred_svc = knn.predict([[float(s1),float(s2),float(s3),float(s4),float(s5),float(s6),float(s7),float(s8),float(s9),float(s10),float(s11),float(s12),float(s13)]])
        msg1=str(Y_pred_svc)
        msg='Result - normal'
        if msg1 == '[1]':
            msg='Result - Heart Disease'
    return render_template('resultpage.html', msg = msg)
    
if __name__ == "__main__":
    app.run(debug=True)