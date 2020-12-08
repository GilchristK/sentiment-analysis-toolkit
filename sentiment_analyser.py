#Author: Katuta Kaunda
#Date: 20-oct-2020
#Description: social media sentiment analysis using the AFINN lexicon
import sys,getopt
import os
import pandas as pd
from afinn import Afinn



#Given a path load excel document into pandas dataframe
def read_excel(path):
    df = pd.read_excel(path)
    print(df)
    #return df
def analyse_sentiments(df):
    # initialize afinn sentiment analyzer
    af = Afinn()

    # compute sentiment scores (polarity) and labels
    afinn_scores = [af.score(text) for text in df.comment]
    df['afinn'] = afinn_scores
    df[['sentiment', 'afinn', 'text']].head(10)
    
    
    

def main():
    
    df = read_excel(r'data_store\reviews_pseudoanonymised.xlsx')

if __name__ == '__main__':
    main()