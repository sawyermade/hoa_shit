import pandas as pd, numpy as np, os, sys, json
from sqlalchemy import create_engine

def main(ind='../data/', outd='../data/output/', inf='expenses_2024.json'):
    # Setup paths
    input_dir = ind
    output_dir = outd
    input_fpath = os.path.join(input_dir, inf)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load data from json
    dsf = load_data_json(input_dir, output_dir, input_fpath)

    # Save data
    save_dataframes(dsf, output_dir)

def load_data_json(input_dir, output_dir, input_fpath):
    # Load all data
    data = {}
    with open(input_fpath, 'r') as f:
        data = json.load(f)
    print(f'data size: {len(data)}')

    # Load data into dataframes
    dfs = {}
    for k, v in data.items():
        dfs[k] = pd.json_normalize(v)
    print(f'dfs size: {len(dfs)}')

    # # Check head on dataframes
    # for k, v in dfs.items():
    #     print(k)
    #     print(v.head())

    return dfs

def save_dataframes(dfs, output_dir, csv=True, html=True, sql=True):
    # Save dataframes to csv
    if csv:
        for k, v in dfs.items():
            output_fpath = os.path.join(output_dir, f'{k}.csv')
            v.to_csv(output_fpath, index=False)
            print(f'{k} saved to {output_fpath}')

    # Save dataframes to html
    if html:
        for k, v in dfs.items():
            output_fpath = os.path.join(output_dir, f'{k}.html')
            v.to_html(output_fpath)
            print(f'{k} saved to {output_fpath}')

    # Save dataframes to sql
    if sql:
        engine = create_engine('sqlite:///../data/expenses_2024.db', echo=False)
        for k, v in dfs.items():
            v.to_sql(k, con=engine, if_exists='replace', index=False)
            print(f'{k} saved to sql')

if __name__ == '__main__':
    main()