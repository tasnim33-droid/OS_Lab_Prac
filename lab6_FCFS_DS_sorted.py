
req_sqnce = [0, 41, 30, 100, 62, 51, 20]

head = 70

total_seek = 0

current = head

for n in req_sqnce:
  difference = abs(current - n)
  print(current,"=>",n,"=>",difference)
  total_seek += difference
  current = n

print("initial seek",total_seek)