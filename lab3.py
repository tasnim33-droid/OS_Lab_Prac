from collections import deque


class Process:
    def __init__(self, pid, at, bt):
        self.pid, self.at, self.bt, self.rt = pid, at, bt, bt
        self.ct = self.tat = self.wt = 0




n = int(input("Enter number of processes: "))
procs = []

for i in range(n):
 pid = input("Enter Process ID: ")
 at = int(input(f"Enter Arrival Time for {pid}: "))
 bt = int(input(f"Enter Burst Time for {pid}: "))
 procs.append(Process(pid, at, bt))

tq, time, done = 5, 0, 0
q, visited = deque(), set()



def enqueue():
    for p in procs:
        if p.at <= time and p.pid not in visited and p.rt > 0:
            q.append(p)
            visited.add(p.pid)


enqueue()
while done < n:
    if not q:
        time += 1
        enqueue()
        continue

    curr = q.popleft()
    exec_time = min(tq, curr.rt)
    curr.rt -= exec_time
    time += exec_time

    enqueue()
    if curr.rt > 0:
        q.append(curr)
    else:
        curr.ct = time
        curr.tat = curr.ct - curr.at
        curr.wt = curr.tat - curr.bt
        done += 1

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(procs, key=lambda x: int(x.pid[1:])):
    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

print(f"\nAvg TAT: {sum(p.tat for p in procs) / n:.2f}")
print(f"Avg WT:  {sum(p.wt for p in procs) / n:.2f}")