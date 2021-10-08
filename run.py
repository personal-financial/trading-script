from utils.database.connection import connect_database
import sys
from analysis.binarycount import run
print("run")

# read_file("./../assets/ETHUSD_H1_202103230000_202109242300.xlsx");
def main_run(a):
    print(a)
if __name__ == "__main__":
    print(sys.argv[1])
    main_run(sys.argv[1])