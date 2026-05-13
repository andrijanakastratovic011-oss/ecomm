import pandas as pd

ord=pd.read_csv('orders.csv')
cus=pd.read_csv('customers.csv')

ord.info()
cus.info()
ord.isnull().sum()
cus.isnull().sum()

class DataCeaner:
    def __init__(self, df: pd.DataFrame, name: str="dataset"):
        self.df=df
        self.name=name

    def report(self)-> None:
        self.size=self.__sizeof__(self.df)
        
