req_sqnce = [60, 20, 100, 10, 15, 22, 42]

head = 50

total_seek = 0

current = head

while req_sqnce:
  nearest = min(req_sqnce, key=lambda x: abs(current - x))
  difference = abs(current - nearest)
  print(current,"=>",nearest,"=>",difference)
  total_seek += difference
  current = nearest

  req_sqnce.remove(nearest)

print("initial seek",total_seek