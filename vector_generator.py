def read_file(path):
  with open(path) as f:
    arr = f.readlines()
    return arr

def get_info_from_str(string):
  track_id = int(string.split()[0])
  top_row = int(string.split()[1])
  top_column = int(string.split()[2])
  bottom_row = int(string.split()[3])
  bottom_column = int(string.split()[4])
  frame_number = int(string.split()[5])
  return track_id, top_row, top_column, bottom_row, bottom_column, frame_number

def generate_vectors(arr):
  vector = []
  for i in arr:
    track_id = i.split()[0]
    top_left 
    for j in arr:
    
        

read_file("/content/boxpaths/direction_trainer_dataset.txt")
