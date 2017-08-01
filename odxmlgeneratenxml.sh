#!/bin/bash
# Usage:
# 
#


python3 xml2txt.py
python3 generateoutput_txt.py
python3 optxt2voc2007xml.py
python3 create_ImageSets.py
python cpsourceImage2voc.py
