import os
import random
import shutil

# TODO: 
# - randomly remove some images in each folder in gtsrb-small and move to test dataset
# - create a function that loads gtsrb-small into ImageFolder

def walk_through_dir(dir_path):
  for dirpath, dirnames, filenames in os.walk(dir_path):
    print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")
    

def get_test_samples(source, destination):
    files = os.listdir(source)
    no_of_files = len(files) // 10

    for file_name in random.sample(files, no_of_files):
        shutil.move(os.path.join(source, file_name), destination)

    
if __name__=="__main__":
    
    # GTSRB labels reference: https://github.com/magnusja/GTSRB-caffe-model/blob/master/labeller/main.py
   
    directory = "gtsrb"
    walk_through_dir(directory)
    
    # get_test_samples("gtsrb-small/37", "gtsrb-small/test")
    print()
    directory = "gtsrb-small"
    walk_through_dir(directory)
    
    

# '27': 'attention_pedestrian' - 240
# '0': '20_speed'              - 210
# '37': 'turn_straight_left'   - 210
