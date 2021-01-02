#Author: Katuta Kaunda
#Date: 20-oct-2020
#Description: social media sentiment analysis using the AFINN lexicon
import sys,getopt
import os
import pandas as pd
from afinn import Afinn

#Demo Example Commit
ExammpleCodeCommit = "Test" 

#Given a path load excel document into pandas dataframe
def read_excel(path):
    df = pd.read_excel(path)
    return df
    
def analyse_sentiments(df):
    # initialize afinn sentiment analyzer
    af = Afinn()

    # compute sentiment scores (polarity) and labels
    afinn_scores = [af.score(text) for text in df.comment]
    
    #categorize the sentiments
    sentiment_category = ['positive' if afinn_score > 0 else 'negative' if afinn_score < 0 else 'neutral' for afinn_score in afinn_scores]
    
    #sentiment statistics
    df2 = pd.DataFrame([sentiment_category,afinn_scores]).T
    df2.columns = ['sentiment','score']
    df2['score'] = df2.score.astype('float')

    return df2
    
    

def main():
    
    df = read_excel(r'data_store\reviews_pseudoanonymised.xlsx')
    df2 = analyse_sentiments(df)
    print(df2)

if __name__ == '__main__':
    main()