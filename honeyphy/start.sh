#!/bin/bash

# Jalankan honeypot.py di background
python honeypot.py 8080 &

# Jalankan log.py di foreground
python log.py 9000
