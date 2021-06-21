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
  f = open("vectors.txt","w")
  vector = []
  for i in arr:
    track_id, top_row, top_column, bottom_row, bottom_column, frame_number = get_info_from_str(i)
    #print("top_row, top_column, bottom_row, bottom_column")
    #print(top_row, top_column, bottom_row, bottom_column)    
    #print("mid_point")
    #print(mid_point)    
    for j in arr:
      track_id_, top_row_, top_column_, bottom_row_, bottom_column_, frame_number_ = get_info_from_str(j)
      if(track_id == track_id_):
        row_mid, col_mid = get_mid_point(top_row_, top_column_, bottom_row_, bottom_column_)
        mid_point = {row_mid, col_mid}
        vector.append(mid_point)
    #print("vector: ", vector)
    f.write(str(vector))
    vector = []
  f.close()
           
arr = read_file("/content/boxpaths/short_dataset.txt")
generate_vectors(arr)
