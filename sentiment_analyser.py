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
    #print(df.comment)
    return df
def analyse_sentiments(df):
    # initialize afinn sentiment analyzer
    af = Afinn()

    # compute sentiment scores (polarity) and labels
    afinn_scores = [af.score(text) for text in df.comment]
    #print(afinn_scores)

    #categorize the sentiments
    sentiment_category = ['positive' if afinn_score > 0 else 'negative' if afinn_score < 0 else 'neutral' for afinn_score in afinn_scores]
    #print(sentiment_category)
    
    #sentiment statistics
    df2 = pd.DataFrame([sentiment_category,afinn_scores]).T
    df2.columns = ['sentiment','score']
    df2['score'] = df2.score.astype('float')
    print(df2.groupby(by=['sentiment']).describe())

    #print(df2)


    #df[['sentiment', 'afinn', 'text']].head(10)
    
    
    

def main():
    
    df = read_excel(r'data_store\reviews_pseudoanonymised.xlsx')
    analyse_sentiments(df)

if __name__ == '__main__':
    main()