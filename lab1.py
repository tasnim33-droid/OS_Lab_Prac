n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = input("Enter Process ID: ")
    arrival = int(input("Enter Arrival Time: "))
    burst = int(input("Enter Burst Time: "))

    processes.append([pid, arrival, burst])

# Sort according to Arrival Time
processes.sort(key=lambda x: x[1])

current_time = 0

total_turnaround = 0
total_waiting = 0

print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for p in processes:
    pid = p[0]
    arrival = p[1]
    burst = p[2]

    # If CPU is idle
    if current_time < arrival:
        current_time = arrival

    # Completion Time
    current_time = current_time + burst
    completion = current_time

    # Turnaround Time
    turnaround = completion - arrival

    # Waiting Time
    waiting = turnaround - burst

    # Add for average calculation
    total_turnaround = total_turnaround + turnaround
    total_waiting = total_waiting + waiting

    print(pid, "\t", arrival, "\t", burst, "\t",
          completion, "\t", turnaround, "\t", waiting)


# Calculate Average
avg_turnaround = total_turnaround / n
avg_waiting = total_waiting / n

print("\nAverage Turnaround Time =", avg_turnaround)
print("Average Waiting Time =", avg_waiting)