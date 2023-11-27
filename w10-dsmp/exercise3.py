def get_positions(lst, element):
  positions = []
  for i, v in enumerate(lst):
    if v == element:
      positions.append(i)
  return tuple(positions)

def check_same_position(list1, list2, element):
  pos1 = get_positions(list1, element)
  pos2 = get_positions(list2, element)
  
  for p in pos1:
    if p in pos2:
      return True
  return False

list1 = [1, 2, 3, 2, 5] 
list2 = [4, 2, 6, 2, 8]
print(check_same_position(list1, list2, 2)) # True

list3 = [1, 3, 5, 7, 9]
list4 = [2, 4, 6, 8, 10] 
print(check_same_position(list3, list4, 2)) # False
