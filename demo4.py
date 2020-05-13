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
    print(f"Unique artists: {len(df['artist'].unique())}")
    print(df[df['artist'] == 'Bacon, Francis'])
    print(df.loc[111, 'artist'])  # Selecting by label: RowIndexer, ColumnIndexer
    print(df.loc[[111, 26037], ['artist', 'units']])  # RowIndexer, ColumnIndexer
    print(df.iloc[0:5, :])


if __name__ == '__main__':
    t01 = time.time()
    main()
    t02 = time.time()
    print(f'{sys.argv[0]} took {t02 - t01:.0f} seconds')
