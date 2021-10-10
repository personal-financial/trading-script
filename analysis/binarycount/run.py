from .binarycounthelper import read_file
from utils.database.connection import DatabaseConnection

# read_file("./../assets/ETHUSD_H1_202103230000_202109242300.xlsx");
def run(di):
    try:
        init_ins(di)
        binary_count(di)
    except Exception as e:
        print("binary count run error")
        print(e)
    finally:
        end_process(di)

def binary_count(di):
    print('binary count run')

    def insert_data(arr, di=di):
        dc = di.get_ins('database')
        connection = dc.get_connection()
        insert_table_query = """
        INSERT INTO candlestick (open_price) values {values};
        """.format(values = ','.join(["(" + str(item["<OPEN>"]) + ")" for item in arr]))
        print(insert_table_query)
        with connection.cursor() as cursor:
            cursor.execute(insert_table_query)
            connection.commit()

    read_file({"path": "./analysis/assets/chart-files/ETHUSD_M1_202107051133_202110082359_test.xlsx"}, insert_data)

def init_ins(di):
    database_connection = DatabaseConnection()
    database_connection.connect()
    di.set_ins('database', database_connection)

def end_process(di):
    dc = di.get_ins('database')
    dc.close()
    print("end")
