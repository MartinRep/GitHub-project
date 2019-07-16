#!/bin/bash

FILE="gh"
FOLDER="/usr/local/bin"

echo 'Installing required python packages...'
pip install --user -r requirements.txt
echo 'Creating executable script...'

if [[ -z "$1" ]]; then
    echo -n "Enter GitHub Token?: "
    read TOKEN
    if [[ -z "$TOKEN" ]]; then
        echo "No Token entered. Exiting.."
        exit
    fi
else
    echo "Using GitHub token: $1"
    TOKEN=$1
fi

touch "$FILE"
echo "#!/usr/bin/env python" > "$FILE"
input="gh.py"
while IFS= read -r line
do
if [[ "$line" == "GH_tokken = \"Your Github Token\" # Get your own from https://github.com/settings/tokens" ]]; then
  echo "GH_tokken = \"$TOKEN\" # This is your unique GitHub Access Token. Replace if gets compromised" >> "$FILE"
else
  echo "$line" >> "$FILE"
fi
done < "$input"

chmod +x $FILE
echo 'Copying script to local bin folder...'
sudo mv $FILE $FOLDER
sudo chmod +x "$FOLDER/$FILE"
echo "The script file $FILE created in $FOLDER"