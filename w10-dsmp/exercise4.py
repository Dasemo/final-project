def range(start=0, stop=None, step=1):
  if stop is None:
    stop = start
    start = 0
  
  if step == 0:
    return ()
  
  if (step > 0 and start > stop) or (step < 0 and start < stop):
    return ()
  
  result = []
  i = start
  while (step > 0 and i < stop) or (step < 0 and i > stop):
    result.append(i)
    i += step
  
  return tuple(result)

print(range(3, 9, 2))
