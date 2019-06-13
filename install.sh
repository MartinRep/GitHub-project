#!/bin/bash
touch github
echo '#!/usr/bin/env python' > github
cat github.py >> github
chmod +x github
sudo cp ./github /usr/local/bin
sudo chmod +x /usr/local/bin/github