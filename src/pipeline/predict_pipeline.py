import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass



    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            #preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            #preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            #data_scaled=preprocessor.transform(features)
            preds=model.predict(features)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,status,bedrooms,bathrooms,acre_lot,city,state,house_size):
        self.status = status
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.acre_lot = acre_lot
        self.city = city
        self.state = state
        self.house_size = house_size


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "status": [self.status],
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "acre_lot": [self.acre_lot],
                "city": [self.city],
                "state": [self.state],
                "house_size": [self.house_size],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

