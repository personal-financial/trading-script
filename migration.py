from utils.designpattern.di import DI
import sys
from analysis.binarycount.migration import run as binarycountmigrate


# read_file("./../assets/ETHUSD_H1_202103230000_202109242300.xlsx");
def main_run(arg):
    print("main")
    di = DI()
    if( arg == 'binarycountup'):
        binarycountmigrate(di, 'up')
    if( arg == 'binarycountdown'):
        binarycountmigrate(di, 'down')
if __name__ == "__main__":
    main_run(sys.argv[1])