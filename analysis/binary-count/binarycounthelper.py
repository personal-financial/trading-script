import pandas as pd

def read_file(path):
    # csv_reader = csv.reader(path, delimiter='	')
    # line_count = 0
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')
    # print(path)
    # dfs = pd.read_csv(path)
    # data.head()
    dfs = pd.read_excel(path)
    # dfs = pd.read_excel(path, sheet_name="ETHUSD_H1_202103230000_20210924")
    print(dfs.head())
    return (path)
