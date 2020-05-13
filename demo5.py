"""
Data import
https://github.com/tategallery/collection
"""
import sys
import time
import pandas as pd

csv_file = '/Users/jojivarghese/works/data/artwork_data.csv'
selected_columns = ['id', 'artist', 'title', 'medium', 'year',
                    'acquisitionYear', 'height', 'width', 'units']


def main():
    df = pd.read_csv(csv_file, index_col='id', usecols=selected_columns)
    print(df)
    print(df['width'].sort_values().head())
    df.loc[:, 'width'] = pd.to_numeric(df['height'], errors='coerce')
    df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')
    area = df['width'] * df['height']
    df = df.assign(area=area)
    mx = df['area'].max()
    print((df[df['area'] == mx]))  # prints a dataframe
    print((df.iloc[df['area'].idxmax(), :]))
    print((df.iloc[df['area'].idxmax(), :]))


if __name__ == '__main__':
    t01 = time.time()
    main()
    t02 = time.time()
    print(f'{sys.argv[0]} took {t02 - t01:.0f} seconds')
