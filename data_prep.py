import os
import random
import shutil


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
   
    # directory = "gtsrb"
    # walk_through_dir(directory)
    
    get_test_samples("gtsrb-small/train/0", "gtsrb-small/test/0")
    get_test_samples("gtsrb-small/train/27", "gtsrb-small/test/27")
    get_test_samples("gtsrb-small/train/37", "gtsrb-small/test/37")
    
    print()
    directory = "gtsrb-small"
    walk_through_dir(directory)
    
    
# '0': '20_speed'              - 210
# '27': 'attention_pedestrian' - 240
# '37': 'turn_straight_left'   - 210

# There are 0 directories and 24 images in 'gtsrb-small/test/27'.
# There are 0 directories and 21 images in 'gtsrb-small/test/0'.
# There are 0 directories and 21 images in 'gtsrb-small/test/37'.

# There are 0 directories and 216 images in 'gtsrb-small/train/27'.
# There are 0 directories and 189 images in 'gtsrb-small/train/0'.
# There are 0 directories and 189 images in 'gtsrb-small/train/37'.
