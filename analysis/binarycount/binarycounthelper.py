import pandas as pd

def read_file(path):
    dfs = pd.read_excel(path)
    # print(dfs.dtypes)
    for index, row in dfs.head().iterrows():
        print(row['<OPEN>'])
        print(row['<CLOSE>'])
        print(row['<CLOSE>'] - row['<OPEN>'])
    return (path)
