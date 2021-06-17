import os.path
import random
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

def find_answer(line):
    words = line.split(' ')
    print(words)
    df = opencsv()
    seri = df.stack()
    fit = seri.str.contains(line)
    prop_lines = fit[fit].index
    idx_in = random.choice(prop_lines)
    idx_out = idx_in[0] + 1
    answer = df.iloc[idx_out]
    return answer['Line']
