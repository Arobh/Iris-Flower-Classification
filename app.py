# app.py

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load Iris dataset and train Logistic Regression model
url = 'https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/iris.csv'
namelist = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=namelist)
X = np.array(iris.iloc[:, :4])
Y = np.array(iris.iloc[:, 4])
model = LogisticRegression()
model.fit(X, Y)

# Route to render index.html   
@app.route('/') 
def index():
    return render_template('index.html')    

# Route to handle form submission and return prediction
@app.route('/rec', methods=['POST'])   
def predict():
    try:
        spl = float(request.form['spl'])
        spw = float(request.form['spw'])
        ptl = float(request.form['ptl'])
        ptw = float(request.form['ptw'])
        
        input_data = np.array([[spl, spw, ptl, ptw]])
        prediction = model.predict(input_data)[0]
        
        return jsonify({'result': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})
 
if __name__ == '__main__':    
    app.run(debug=True)      
 