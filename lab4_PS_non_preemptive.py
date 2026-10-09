
non-preemptive.py
100%
class Process:
    def __init__(self, pid, at, bt, pr):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.pr = pr
        self.ct = 0
        self.tat = 0
        self.wt = 0


n = int(input("Enter number of processes: "))
procs = []

# Input
for i in range(n):
    pid = f"P{i+1}"
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    pr = int(input(f"Enter Priority for {pid}: "))

    procs.append(Process(pid, at, bt, pr))


# Priority Scheduling
time = 0
done = 0

while done < n:

    # Find arrived processes
    ready = [p for p in procs
             if p.at <= time and p.ct == 0]

    # If no process has arrived
    if not ready:
        time += 1
        continue

    # Select highest priority
    current = min(ready, key=lambda p: p.pr)

    # Run the process completely
    time = time + current.bt

    # Calculate CT, TAT and WT
    current.ct = time
    current.tat = current.ct - current.at
    current.wt = current.tat - current.bt

    done += 1


# Output
print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")

for p in procs:
    print(p.pid, "\t", p.at, "\t", p.bt, "\t",
          p.pr, "\t", p.ct, "\t", p.tat, "\t", p.wt)


# Average
avg_tat = sum(p.tat for p in procs) / n
avg_wt = sum(p.wt for p in procs) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
Displaying non-preemptive.py.Previous