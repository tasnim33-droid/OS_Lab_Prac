req_sqnce = [0, 41, 30, 100, 62, 51, 20]

head = 70

total_seek = 0
current = head
remaining = req_sqnce.copy()
sequence = []

while remaining:
  closest = min(remaining,key=lambda x:abs(current - x))
  difference = abs(current - closest)
  total_seek += difference
  sequence.append(closest)
  current = closest
  remaining.remove(closest)




print("initial seek",total_seek)