import streamlit as st
import pandas as pd
import numpy as np
import joblib

# input dict for categorical label
# brand dict
brand_dic = {'TOYOTA': 0,
 'Daihatsu': 1,
 'Honda': 2,
 'Isuzu': 3,
 'Lexus': 4,
 'Mazda': 5,
 'Mitsubishi': 6,
 'Mitsuoka': 7,
 'Nissan': 8,
 'Subaru': 9,
 'Suzuki': 10}

# displacement_based dict
displacement_based_dic = {'mid-range': 0, 'mini': 1, 'Subcompact': 2, 'large': 3}

# model dict
model_dic = {'TOYOTA CAMRY': 0,
 'TOYOTA CAMRY GRACIA': 1,
 'TOYOTA CAMRY GRACIA SEDAN': 2,
 'TOYOTA CAMRY GRACIA STATIONWAGON': 3,
 'Daihatsu Charade': 4,
 'Daihatsu Charade DE Tomaso': 5,
 'Daihatsu Copen': 6,
 'Daihatsu Charade Social': 7,
 'Daihatsu COO': 8,
 'Daihatsu Boon': 9,
 'Daihatsu BE GO': 10,
 'Daihatsu Boon Luminas': 11,
 'Honda Civic': 12,
 'Honda Capa': 13,
 'Honda Integra': 14,
 'Honda Integra SJ': 15,
 'Isuzu Gemini': 16,
 'Isuzu MU': 17,
 'Isuzu Piazza Nero': 18,
 'Isuzu Vehicross': 19,
 'Isuzu Wizard': 20,
 'Isuzu Piazza': 21,
 'Isuzu MU Wizard': 22,
 'Isuzu Wizard Alive': 23,
 'Lexus RX': 24,
 'Lexus NX': 25,
 'Lexus RC': 26,
 'Lexus RC F': 27,
 'Lexus UX': 28,
 'Lexus SC': 29,
 'Lexus LS': 30,
 'Lexus LX': 31,
 'Mazda Cx-5': 32,
 'Mazda Cx-8': 33,
 'Mazda Cx-7': 34,
 'Mitsubishi Galant Fortis': 35,
 'Mitsubishi Grandis': 36,
 'Mitsubishi Galant Sigma': 37,
 'Mitsubishi GTO': 38,
 'Mitsubishi Galant Fortis Sportback': 39,
 'Mitsubishi Galant Sports': 40,
 'Mitsuoka Galue II': 41,
 'Mitsuoka Galue 204': 42,
 'Mitsuoka Galue Convertible': 43,
 'Mitsuoka Galue Limousine S50': 44,
 'Mitsuoka Galue': 45,
 'Mitsuoka Galue Classic': 46,
 'Mitsuoka Galue I': 47,
 'Mitsuoka Galue III': 48,
 'Mitsuoka Nouera 6-02 Sedan': 49,
 'Mitsuoka Nouera 6-02 Wagon': 50,
 'Mitsuoka Nouera': 51,
 'Nissan Cedric': 52,
 'Nissan Dayz': 53,
 'Subaru Impreza Sport Wagon': 54,
 'Subaru Impreza WRX': 55,
 'Subaru Impreza XV': 56,
 'Suzuki KEI': 57,
 'Suzuki KEI Sport': 58,
 'Suzuki KEI Works': 59,
 'Suzuki Kizashi': 60,
 }


# list of categorical label
brand_list = ['TOYOTA',
 'Daihatsu',
 'Honda',
 'Isuzu',
 'Lexus',
 'Mazda',
 'Mitsubishi',
 'Mitsuoka',
 'Nissan',
 'Subaru',
 'Suzuki']

displacement_based_list = ['mid-range', 'mini', 'Subcompact', 'large']


# setting custome tab
st.set_page_config(page_title='Used Car price Prediction by Subha', page_icon='????')


# ceating car model brand list.
# loading the dataset.
car = pd.read_csv('carprice.csv')

# creating a function for filtering the model name correspond to it brand.
def find_model(brand):
    model = car[car['Make'] == brand]['Model'] # return series of filter model name for specific brand.
    return list(set(model)) # return list of filter model name for specific brand.


# loding the model
@st.cache(allow_output_mutation=True)
def model_loader(path):
    model = joblib.load(path)
    return model


# loading both models
with st.spinner('???????????????????????????????? Hold on, the app is loading !! ????????????????????????????????'):
    model_forest = model_loader("xxx.pkl")




# # writing header
# st.title('# Used Car Price Predition???  ????')
st.markdown("<h2 style='text-align: center;'>????  Japanese Car Price Prediction???  ????</h2>", unsafe_allow_html=True)


col1, col2 = st.beta_columns(2)

# start taking inpouts

#brand integer
brand_inp = col1.selectbox(label='Enter the Brand of the car', options=brand_list, help='From which brand the car is belongs?') # passing the brand list
brand = brand_dic[brand_inp] # converting the brand name to numerical encoding form

#model of the car for specific brand
if brand_inp == 'TOYOTA':
    model_inp = col1.selectbox('Enter the Model for the Audi', options=find_model('TOYOTA'))
    model = model_dic[model_inp]  # doing numerical encoding

elif brand_inp == 'Daihatsu':
    model_inp = col1.selectbox('Enter the model for Daihatsu', options=find_model('Daihatsu'))
    model = model_dic[model_inp] 

elif brand_inp == 'Honda':   
    model_inp = col1.selectbox('Enter the model Honda', options=find_model('Honda'))
    model = model_dic[model_inp]

elif brand_inp == 'Isuzu':
    model_inp = col1.selectbox('Enter the model for Isuzu', options=find_model('Isuzu'))
    model = model_dic[model_inp] 

elif brand_inp == 'Lexus':
    model_inp = col1.selectbox('Enter the model for Lexus', options=find_model('Lexus'))
    model = model_dic[model_inp] 
    
elif brand_inp == 'Mazda':
    model_inp = col1.selectbox('Enter the model for Mazda', options=find_model('Mazda'))
    model = model_dic[model_inp] 

elif brand_inp == 'Mitsubishi':
    model_inp = col1.selectbox('Enter the model for Mitsubishi', options=find_model('Mitsubishi'))
    model = model_dic[model_inp] 
    
elif brand_inp == 'Mitsuoka':
    model_inp = col1.selectbox('Enter the model for Mitsuoka', options=find_model('Mitsuoka'))
    model = model_dic[model_inp] 

elif brand_inp == 'Nissan':
    model_inp = col1.selectbox('Enter the model for Nissan', options=find_model('Nissan'))
    model = model_dic[model_inp] 
    
elif brand_inp == 'Subaru':
    model_inp = col1.selectbox('Enter the model for Subaru', options=find_model('Subaru'))
    model = model_dic[model_inp] 

elif brand_inp == 'Suzuki':
    model_inp = col1.selectbox('Enter the model for Suzuki', options=find_model('Suzuki'))
    model = model_dic[model_inp] 
    

#doors
doors = col1.number_input(label='Enter the number of doors of the car, e.g: 4 (enter number only)')

#riding capacity
capac = col1.number_input(label='Enter the number of seats of the car, e.g: 4 (enter number only)')

#length
length = col1.number_input(label='Enter the length (mm) of the car, e.g: 4 (enter number only)')
length = float(length)

#width
width = col1.number_input(label='Enter the width (mm) of the car, e.g: 4 (enter number only)')
width = float(width)

#height
height = col1.number_input(label='Enter the height (mm) of the car, e.g: 4 (enter number only)')
height = float(height)

#weight
weight = col1.number_input(label='Enter the weight (kg) of the car, e.g: 4 (enter number only)')
weight = float(weight)

#year
year =  col2.slider('Enter the year when the car was manufactured, e.g: 2005', 1980,2020,2005,help='The year when the car is manufactured.')

#dpclass
dpclass = col2.selectbox(label='Enter the displacement class', options=displacement_based_list)
dpclass = displacement_based_dic[dpclass]

#wheelbase
wb = col2.number_input(label='Enter the wheelbase (mm) of the car')
wb = float(wb)

#maximumpower
mp = col2.number_input(label='Enter the MaximumPower (kW) of the car')
mp = float(mp)

#displacement
displacement = col2.number_input(label='Enter the Displacement (cc) of the car')
displacement = float(displacement)

#bore
bore = col2.number_input(label='Enter the Bore (mm) of the car')
bore = float(bore)

#stroke
stroke = col2.number_input(label='Enter the Stroke (mm) of the car')
stroke = float(stroke)

#fte
fte = col2.number_input(label='Enter the Fuel Tank Equipment (L) of the car')
fte = float(fte)


# creatng a input array for prediction
inp_array = np.array([[year,doors,capac,wb,weight,mp,displacement,fte,length,width,height,bore,stroke,brand,dpclass,model]])

predict = col1.button('Predict') # creating a predict buutton

if predict: 
        pred = model_forest.predict(inp_array)
        if pred < 0: # handeling negative outputs.
            st.error('The input values must be irrelevant, try again by giving relevent information.')
        pred = round(float(pred),3)
        write = 'The predicted price of the car is ?? '+ str(pred) + ' ????' # showing the price prediction.
        st.success(write)
        st.balloons()


# writing some information about the projects.


