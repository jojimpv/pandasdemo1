"""
Data import
https://github.com/tategallery/collection
"""
import json
import os
import sys
import time
import pandas as pd

csv_file = '/media/joji/DATA/workspace/data/artwork_data.csv'
selected_columns = ['id', 'artist', 'title', 'medium', 'year',
                    'acquisitionYear', 'height', 'width', 'units']


def main():
    df = pd.read_csv(csv_file, index_col='id', usecols=selected_columns)
    print(df)
    print(f"Unique artists: {len(df['artist'].unique())}")
    # print(len(set(df['artist'])))
    tf_series = df['artist'] == 'Bacon, Francis'
    print(tf_series.value_counts())
    print(type(tf_series.value_counts()))
    print(df['artist'].value_counts()['Bacon, Francis'])


if __name__ == '__main__':
    t01 = time.time()
    main()
    t02 = time.time()
    print(f'{sys.argv[0]} took {t02 - t01:.0f} seconds')
