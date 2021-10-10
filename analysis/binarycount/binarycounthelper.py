import pandas as pd

def read_file(config, callback):
    # TODO read too low
    dfs = pd.read_excel(config["path"])
    dfs = dfs.head()
    arr = []
    nRow = len(dfs)
    for index, row in dfs.iterrows():
        arr.append(row)
        if((index == nRow - 1 or len(arr) == 100) and callback):
            callback(arr)
            arr.clear()
