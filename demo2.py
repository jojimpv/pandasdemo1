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
persist_file = '/media/joji/DATA/workspace/data/artwork_data.pickle'
selected_columns = ['id', 'artist', 'title', 'medium', 'year',
                    'acquisitionYear', 'height', 'width', 'units']
selected_columns_json = ['id', 'all_artists', 'title', 'medium',
                         'dateText', 'acquisitionYear', 'height', 'width', 'units']

artists_json_path = r'/media/joji/DATA/works/tategallery.collection/artworks/'


def read_from_json_file(file_path):
    with open(file_path) as artists_file:
        artists_rec = json.load(artists_file)
        return {k: v for k, v in artists_rec.items() if k in selected_columns_json}


def get_records(root_path):
    records = []
    for r, d, f in os.walk(root_path):
        for file_name in f:
            file_path = os.path.join(r, file_name)
            record = read_from_json_file(file_path)
            records.append(record)
    return records


def main():
    # df = pd.read_csv(csv_file, header=True, nrows=5)
    # df = pd.read_csv(csv_file, nrows=5, index_col='id', usecols=['id', 'artist'])
    df = pd.read_csv(csv_file, nrows=5, index_col='id', usecols=selected_columns)
    print(df)
    df.to_pickle(persist_file)
    print(f'Saved df to {persist_file}')
    records = get_records(artists_json_path)
    print(f'Count of records: {len(records)}')
    print(f'records[0] = {records[0]}')
    df2 = pd.DataFrame.from_records(records, columns=selected_columns_json, index='id')
    print(df2.head(5))


if __name__ == '__main__':
    t01 = time.time()
    main()
    t02 = time.time()
    print(f'{sys.argv[0]} took {t02 - t01:.0f} seconds')
