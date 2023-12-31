import os
import csv
from PIL import Image
from pathlib import Path

directory = "data"

# write annotations (data labels) to annotations.csv
with open('data/annotations.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    column_names = ["data path", "label"]
    writer.writerow(column_names)
    
    for foldername in os.listdir(directory):
        if foldername != "annotations.csv":
            for filename in os.listdir(os.path.join(directory, foldername)):
                if filename.endswith((".png")):
                    
                    # convert to png (no need to do it again)
                    # path = Path(os.path.join(directory, foldername, filename))
                    # path.rename(path.with_suffix('.png'))
                    
                    f = os.path.join(foldername, filename)
                    writer.writerow([f, foldername])
