class Process:
    def __init__(self, P_id, at, bt):
        self.P_id, self.at, self.bt, self.rt = P_id, at, bt, bt
        self.ct = self.tat = self.wt = 0


n = int(input("Enter number of processes: "))

procs = []

for i in range(n):
    P_id = input("Enter Process ID: ")
    at = int(input(f"Enter Arrival Time for {P_id}: "))
    bt = int(input(f"Enter Burst Time for {P_id}: "))

    procs.append(Process(P_id, at, bt))


time, done = 0, 0

while done < n:
    ready = [p for p in procs if p.at <= time and p.rt > 0]

    if not ready:
        time += 1
        continue

    curr = min(ready, key=lambda p: p.rt)

    curr.rt -= 1
    time += 1

    if curr.rt == 0:
        curr.ct = time
        curr.tat = curr.ct - curr.at
        curr.wt = curr.tat - curr.bt
        done += 1


print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for p in sorted(procs, key=lambda x: x.P_id):
    print(f"{p.P_id}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


avg_tat = sum(p.tat for p in procs) / n
avg_wt = sum(p.wt for p in procs) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time:    {avg_wt:.2f}")