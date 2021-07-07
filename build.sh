#!/usr/bin/env bash

for d in *; do

    if [ -d "$d" ]; then
        cd "$d"

        echo "= PACK: $d ="
        FILE=title.txt
        if [ -f "$FILE" ]; then
            echo "✓ Title added"
        else 
            echo "❌ Add a title file"
            continue
        fi

        FILE=author.txt
        if [ -f "$FILE" ]; then
            echo "✓ Author added"
        else 
            echo "❌ Add an author file"
            continue
        fi

        
        echo "Building pack..."
        zip "ASCI_$d.wastickers" *
        mv "ASCI_$d.wastickers" ../
        cd ../

        echo ''
    else
        continue
    fi

    zip "ASCI_Stickers.zip" *.wastickers
    rm *.wastickers
done