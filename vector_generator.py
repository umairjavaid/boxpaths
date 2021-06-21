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

def get_mid_point(top_row, top_column, bottom_row, bottom_column):
  row_mid = int((bottom_row - top_row)/2) + top_row
  col_mid = int((bottom_column - top_column)/2) + top_column
  return row_mid, col_mid

def generate_vectors(arr):
  vector = []
  for i in arr:
    track_id, top_row, top_column, bottom_row, bottom_column, frame_number = get_info_from_str(i)
    print("top_row, top_column, bottom_row, bottom_column")
    print(top_row, top_column, bottom_row, bottom_column)
    mid_point = get_mid_point(top_row, top_column, bottom_row, bottom_column)
    print("mid_point")
    print(mid_point)
            
arr = read_file("/content/boxpaths/direction_trainer_dataset.txt")
generate_vectors(arr)
