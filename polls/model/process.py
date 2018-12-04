'''
#Project: Sentiment Analysis
#Author: Ho Ngoc Vinh Han
#Time: 11/2018
'''
import random as rand
import numpy as np
import pandas as pd
import os
from pyvi import ViTokenizer
from sklearn.externals import joblib


class Process(object):
    def test(cmt):
        
        test_data = []

        test_data.append({"data": cmt, "target": "none"})

        df_test = pd.DataFrame(test_data)

        for index in range(len(df_test.data)):
            df_test.data[index] = ViTokenizer.tokenize(df_test.data[index])
        pass

        # load the model from disk
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'finalized_model.sav')
        loaded_model = joblib.load(my_file)

        predicted = loaded_model.predict(df_test.data)
        #print(predicted[0])
        #print(loaded_model.predict_proba(df_test.data))
        if predicted[0]=='tich_cuc':
            return "Tích cực"
        else:
            return "Tiêu cực"
        pass

    pass


