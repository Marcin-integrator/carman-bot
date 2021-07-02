import operator
import os.path
import random
import re
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
    words = re.split(' |\r\n', line)
    df = opencsv()
    seri = df.stack()
    occurrence = {}

    for word in words:
        fit = seri.str.contains(word)
        prop_lines = fit[fit].index

        for elen in prop_lines:
            if elen[1] == 'Line':
                if elen[0] not in occurrence:
                    occurrence[elen[0]] = 1
                else:
                    new_value = occurrence[elen[0]] + 1
                    occurrence[elen[0]] = new_value

    maxi = max(occurrence.items(), key=operator.itemgetter(1))[1]
    mostly = [k for k,v in occurrence.items() if v == maxi]

    idx_in = random.choice(mostly)
    idx_out = idx_in + 1
    answer = df.iloc[idx_out]

    return answer['Line']
