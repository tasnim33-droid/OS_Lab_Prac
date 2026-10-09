n = int(input("Enter number of processes: "))
time_quantum = int(input("Enter Time Quantum: "))

processes = []

for i in range(n):
    print(f"\nProcess P{i + 1}:")

    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    priority = int(input("Priority: "))

    processes.append({
        "PID": f"P{i + 1}",
        "AT": at,
        "BT": bt,
        "Priority": priority,
        "Remaining": bt
    })

time = 0
completed = 0
total_wt = 0
total_tat = 0

while completed < n:

    ready = []

    for p in processes:
        if p["AT"] <= time and p["Remaining"] > 0:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    highest = ready[0]

    for p in ready:
        if p["Priority"] < highest["Priority"]:
            highest = p

        elif p["Priority"] == highest["Priority"]:
            if p["AT"] < highest["AT"]:
                highest = p

    run_time = min(time_quantum, highest["Remaining"])

    highest["Remaining"] -= run_time
    time += run_time

    if highest["Remaining"] == 0:
        highest["CT"] = time

        highest["TAT"] = highest["CT"] - highest["AT"]

        highest["WT"] = highest["TAT"] - highest["BT"]

        total_wt += highest["WT"]
        total_tat += highest["TAT"]

        completed += 1


print("\nPID\tAT\tBT\tPriority\tCT")

for p in processes:
    print(
        p["PID"], "\t",
        p["AT"], "\t",
        p["BT"], "\t",
        p["Priority"], "\t\t",
        p["CT"]
    )

print("\nAverage Waiting Time:", total_wt / n)
print("Average Turnaround Time:", total_tat / n)