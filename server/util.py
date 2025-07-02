import json
import pickle
import numpy as np
import os


__locations=None
__data_columns=None
__model=None

def get_estimated_price(location, sqft, bhk, bath):
    global __model
    if __model is None or __data_columns is None:
        load_saved_artifacts()

    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

    
def get_location_names():
    global __locations
    if __locations is None:
        load_saved_artifacts()
    return __locations


def get_data_columns():
    global __data_columns
    if __data_columns is None:
        load_saved_artifacts()
    return __data_columns



def load_saved_artifacts():
    
    global __data_columns
    global __locations
    global __model
    print("loading saved artifacts starting...")

    BASE_DIR = os.path.dirname(__file__)
    columns_path = os.path.join(BASE_DIR, '../model/columns.json')
    model_path = os.path.join(BASE_DIR, '../model/bangalore_home_prices_model.pickle')


    with open(columns_path,'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]

    with open(model_path,'rb') as f:
        __model=pickle.load(f)


    print("loading the artifacts is done")
    


if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    #print(get_location_names())
    print(get_estimated_price('1st block jayanagar',1000,3,3))
    print(get_estimated_price('1st phase jp nagar',1000,3,3))
    print(get_estimated_price('1st phase jp nagar',1000,1,1))
   # print(get_estimated_price('1st phase jp nagar',1000,4,4))
    #print(get_estimated_price('kalhalli',1000,3,3))