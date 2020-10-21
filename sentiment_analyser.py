#Author: Katuta Kaunda
#Date: 20-oct-2020
#Description: social media sentiment analysis using the AFINN lexicon
import sys,getopt
import os
import pandas as pd




#Given a path load excel document into pandas dataframe
def read_excel(path):
    df = pd.read_excel(path)
    print(df)

def main():
    
    read_excel(r'data_store\reviews_pseudoanonymised.xlsx')

if __name__ == '__main__':
    main()