#Author: Katuta Kaunda
#Date: 20-oct-2020
#Description: social media sentiment visualiser
import sys,getopt
import os
import pandas as pd
import plotly
import plotly.express as plt
import time
from sentiment_analyser import *
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as mplt 
import unicodedata

##generates a bar chart visualization using plotly
def generateVisualization(df):
    print(df.groupby(by=['sentiment']).describe())
    df1 = df.groupby(["sentiment"]).count().reset_index()
    fig = plt.bar(df1,y=df.groupby(["sentiment"]).size(),x="sentiment",color='sentiment',title='AFINN sentiment Analysis') 
    saveReport(fig)

##Saves the generated visualizationas an html file
def saveReport(fig):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    
    # html file
    plotly.offline.plot(fig, filename='reports\sentiment_results-'+timestr+'.html')

def generateWordCloud(df):
    print(df)
    comment_words = '' 
    stopwords = set(STOPWORDS) 
    # iterate through the csv file 
    for text in df.comment: 
      
        # typecaste each val to string 
        #text = str(text)
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
  
        # split the value 
        tokens = text.split() 
      
        # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
      
        comment_words += " ".join(tokens)+" "
  
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
    # plot the WordCloud image                        
    mplt.figure(figsize = (8, 8), facecolor = None) 
    mplt.imshow(wordcloud) 
    mplt.axis("off") 
    mplt.tight_layout(pad = 0) 
  
    mplt.show() 

def main():
    
    df = read_excel(r'data_store\reviews_pseudoanonymised.xlsx')
    #df2 = analyse_sentiments(df)
    #generate the bar chart
    #generateVisualization(df2)

    #generate the word cloud
    generateWordCloud(df)

if __name__ == '__main__':
    main()
