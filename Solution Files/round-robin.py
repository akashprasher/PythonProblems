def find_waiting_time(n, b_time, wait, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = b_time[i]

    t = 0  # Current time

    while(1):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0):
                done = False

                if (rem_bt[i] > quantum):
                    t += quantum
                    rem_bt[i] -= quantum

                else:
                    t = t + rem_bt[i]
                    wait[i] = t - b_time[i]
                    rem_bt[i] = 0

            if (done == True):
                break


def find_turn_around_time(n, b_time, wait, tat):
    for i in range(n):
        tat[i] = b_time + wait[i]


def find_average_time(proc, n, b_time, quantum):
    wait = [0] * n
    tat = [0] * n

    find_waiting_time(n, b_time, wait, quantum)

    find_turn_around_time(n, b_time, wait, tat)

    print("Processes\tBurst Time\tWaiting", "Time\tTurn-Arounf Time")

    total_wait = 0
    total_tat = 0

    for i in range(n):
        total_wait = total_wait + wait[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", b_time[i], "\t\t", wait[i], "\t\t", tat[i])

    print("\nAverage waiting time = %.5f" % (total_wait / n))
    print("\nAverage turn around time = %.5f" % (total_tat / n))


if __name__ == "__main__":
    proc = [1, 2, 3]
    n = 3

    burst_time = [10, 5, 8]

    quantum = 2

    find_average_time(proc, n, burst_time, quantum)
