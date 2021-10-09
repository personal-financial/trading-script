from .binarycounthelper import read_file
from utils.database.connection import DatabaseConnection

# read_file("./../assets/ETHUSD_H1_202103230000_202109242300.xlsx");
def run(di):
    try:
        init_ins(di)
        binary_count(di)
    except:
        print("binary count run error")
    finally:
        end_process(di)

def binary_count(di):
    print('binary count run')
    dc = di.get_ins('database')
    connection = dc.get_connection()
    create_reviewers_table_query = """
    CREATE TABLE candlestick (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_reviewers_table_query)
        connection.commit()

def init_ins(di):
    database_connection = DatabaseConnection()
    database_connection.connect()
    di.set_ins('database', database_connection)

def end_process(di):
    dc = di.get_ins('database')
    dc.close()
    print("end")
