

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ProxyModelEDA():
    
    def __init__(self, 
                 dataset_filename: str, 
                 data_directory: str):

        # Save dataset path
        self._dataset_filename = dataset_filename
        self._data_directory = data_directory
        self._dataset_path = os.path.join(self._data_directory, self._dataset_filename)

        self._df = pd.DataFrame()

        # Read Data
        self.read_data()

        # self.describe_data()

        # self.view_pairplot()
        

    def read_data(self):
        self._df = pd.read_csv(self._dataset_path)


    def view_data_raw(self):
        '''View Head of data'''

        if self._df.empty:
            print('Empty Dataframe. Please read data first.')
        else:
            print(self._df.head())
        
    def describe_data(self):
        '''Print description of data'''

        if self._df.empty:
            print('Empty Dataframe. Please read data first.')
        else:
            print(self._df.describe(include='all'))

    def view_pairplot(self):
        '''Visualize Data using a pairplot'''

        if self._df.empty:
            print('Empty Dataframe. Please read data first.')
        else:
            sns.pairplot(self._df)
            plt.show()

    def get_dataframe(self):
        '''Return Dataframe'''
        return self._df


