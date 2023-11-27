import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass

class EncodingCS:
    def data_encoding(self):
        df = pd.read_csv('notebook\data\data.csv')
        df.dropna(subset=['city'],inplace=True)

        mean_ordinal_city = df.groupby(['city'])['price'].mean().to_dict()
        mean_ordinal_state = df.groupby(['state'])['price'].mean().to_dict()

        df['city'] = df['city'].map(mean_ordinal_city)
        df['state'] = df['state'].map(mean_ordinal_state)
        df['status'] = df['status'].map({'for_sale': 1, 'ready_to_build': 0})
        df.drop('prev_sold_date', axis=1, inplace=True)
        df.drop('zip_code', axis=1, inplace=True)
        df['bed'].fillna(df['bed'].median(), inplace=True)
        df['bath'].fillna(df['bath'].median(), inplace=True)
        df['acre_lot'].fillna(0.23, inplace=True)
        df['house_size'].fillna(1800, inplace=True)
        df['price'].fillna(df['price'].median(), inplace=True)
        df.to_csv('notebook\data\data2.csv',index=False)
        return mean_ordinal_city, mean_ordinal_state

