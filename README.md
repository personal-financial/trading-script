# Trading Script
install Libs
source venv/bin/activate
pip3 install -r requirements.txt

# Recreate Virtualenv
virtualenv venv
source venv/bin/activate
deactivate

# Run Elasticsearch
sudo systemctl start elasticsearch