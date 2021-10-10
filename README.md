# Trading Script
install Libs
source venv/bin/activate
pip3 install -r requirements.txt

# Recreate Virtualenv
virtualenv venv
source venv/bin/activate
deactivate

# Run 
python3 run.py binarycount

# Migration
python3 migration.py binarycountdown
python3 migration.py binarycountup