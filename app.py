from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__, template_folder='Templates')

model=pickle.load(open('randomforest.pkl','rb'))
car=pd.read_csv('carprice.csv')

@app.route('/',methods=['GET','POST'])
def index():
    companies=sorted(car['Make'].unique())
    car_models=sorted(car['Model'].unique())
    dpclasses=sorted(car['displacement-based class'].unique())

    companies.insert(0,'Select Company')
    return render_template('index.html',companies=companies, car_models=car_models, dpclasses=dpclasses)

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    company=request.form.get('company')
    car_model=request.form.get('car_model')
    door=request.form.get('door')
    capac=request.form.get('capac')
    length=request.form.get('length')
    width=request.form.get('width')
    height=request.form.get('height')
    wbase=request.form.get('wbase')
    weight=request.form.get('weight')
    mp=request.form.get('mp')
    displacement=request.form.get('displacement')
    dpclass=request.form.get('dpclass')
    bore=request.form.get('bore')
    stroke=request.form.get('stroke')
    fte=request.form.get('fte')
    year=request.form.get('year')

    prediction=model.predict(pd.DataFrame([[company,car_model,door,capac,length,width,height,wbase,weight,mp,displacement,dpclass,
                                             bore,stroke,fte,year]], columns=['Make', 'Model', 'Doors', 'Riding Capacity', 'Overall Length (mm)', 'Overall Width (mm)',
                                                   'Overall Height (mm)', 'Wheelbase (mm)', 'Weight (kg)', 'Maximum Power (kW)',
                                                   'Displacement (cc)', 'displacement-based class', 'Bore (mm)', 'Stroke (mm)', 'Fuel Tank Equipment (L)', 
                                                   'year of launch']))
    print(prediction)

    return str(np.round(prediction[0],2))

if __name__=='__main__':
    app.run()