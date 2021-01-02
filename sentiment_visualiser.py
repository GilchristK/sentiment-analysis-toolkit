#Author: Katuta Kaunda
#Date: 20-oct-2020
#Description: social media sentiment visualiser
import sys,getopt
import os
import pandas as pd
import plotly.express as plt
from sentiment_analyser import *
def generateVisualization(df):
    #df2 = df.groupby(by=['sentiment'])
    #fig = plt.bar(df, x='sentiment', y='score',title='AFINN sentiment Analysis')
    #fig.show()
    df1 = df.groupby(["sentiment"]).count().reset_index()
    fig = plt.bar(df1,y=df.groupby(["sentiment"]).size(),x="sentiment",color='sentiment',title='AFINN sentiment Analysis') 
    fig.show()

def main():
    
    df = read_excel(r'data_store\reviews_pseudoanonymised.xlsx')
    df2 = analyse_sentiments(df)
    print(df2.describe())
    generateVisualization(df2)

if __name__ == '__main__':
    main()
