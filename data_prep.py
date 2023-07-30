import os


def walk_through_dir(dir_path):
  """
  Walks through dir_path returning its contents.
  Args:
    dir_path (str or pathlib.Path): target directory
  
  Returns:
    A print out of:
      number of subdiretories in dir_path
      number of images (files) in each subdirectory
      name of each subdirectory
  """
  for dirpath, dirnames, filenames in os.walk(dir_path):
    print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")
    
    
if __name__=="__main__":
    
    directory = "gtsrb"
    walk_through_dir(directory)
    
    

# '27': 'attention_pedestrian' - 240
# '0': '20_speed'              - 210
# '37': 'turn_straight_left'   - 210
