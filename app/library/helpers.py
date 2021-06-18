import os.path
import markdown
import pandas as pd


def openfile(filename):
    filepath = os.path.join('app/pages/', filename)
    with open(filepath, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {
        'text': html
    }

    return data

def opencsv():
    textfile = 'docs/All-seasons.csv'
    df = pd.read_csv(textfile)
    return df

def readcsv():
    df = opencsv()
    df_episodes = df.groupby('Season')['Episode'].unique()
    df_episodes.drop(index=df_episodes.index[-1], 
        axis=0, 
        inplace=True)
    df_episodes.index.astype(int)

    return df_episodes

def get_lines(s, e):
    df = opencsv()
    df_lines = df[(df['Season']==s) & (df['Episode']==e)]
    return df_lines
