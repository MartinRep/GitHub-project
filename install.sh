#!/bin/bash
echo 'Installing required python packages...'
pip install -r requirements.txt
echo 'Creating executable script...'
touch github
echo '#!/usr/bin/env python' > github
cat github.py >> github
chmod +x github
echo 'Copying script to local bin folder'
sudo cp ./github /usr/local/bin
sudo chmod +x /usr/local/bin/github