import os
import csv

directory = "data"

# labels reference: https://github.com/magnusja/GTSRB-caffe-model/blob/master/labeller/main.py
label_map = {
    '0': 'stop',
    '1': 'turn_straight_left',
    '2': '20_speed'
}

# write annotations (data labels) to annotations.csv
with open('data/annotations.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    
    for foldername in os.listdir(directory):
        if foldername != "annotations.csv":
            for filename in os.listdir(os.path.join(directory, foldername)):
                if filename.endswith((".ppm")):
                    f = os.path.join(foldername, filename)
                    writer.writerow([f, label_map[foldername]])
