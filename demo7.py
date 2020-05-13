"""
Data import
https://github.com/tategallery/collection
"""
import sys
import time
import pandas as pd
import sqlite3

csv_file = '/Users/jojivarghese/works/data/artwork_data.csv'
selected_columns = ['id', 'artist', 'title', 'medium', 'year',
                    'acquisitionYear', 'height', 'width', 'units']


def main():
    df = pd.read_csv(csv_file, index_col='id', usecols=selected_columns)
    df = df.iloc[1:1000, :].copy()
    print(df)
    df.to_excel('small_df.xlsx')
    with sqlite3.connect('db.sqlite3') as conn:
        df.to_sql('sample', conn)


if __name__ == '__main__':
    t01 = time.time()
    main()
    t02 = time.time()
    print(f'{sys.argv[0]} took {t02 - t01:.0f} seconds')
