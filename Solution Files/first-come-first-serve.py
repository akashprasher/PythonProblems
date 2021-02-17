def find_waiting_time(process, n, b_time, wait):
    wait[0] = 0

    for i in range(1, n):
        wait[i] = b_time[i - 1] + wait[i - 1]


def find_turn_around_time(processes, n, b_time, wait, tat):
    for i in range(n):
        tat[i] = b_time[i] + wait[i]


def find_avg_time(processes, n, b_time):
    wait = [0] * n
    tat = [0] * n
    total_wait = 0
    total_tat = 0

    find_waiting_time(processes, n, b_time, wait)

    find_turn_around_time(processes, n, b_time, wait, tat)

    print("Processes |" + " Burst time |" +
          " Waiting time |" + " Turn around time")

    for i in range(n):
        total_wait = total_wait + wait[i]
        total_tat = total_tat + tat[i]

        print(" " + str(i + 1) + "\t\t" +
              str(b_time[i]) + "\t " + str(wait[i]) + "\t\t " + str(tat[i]))

    print("Average waiting time = " + str(total_wait / n))
    print("Average turn Around time = " + str(total_tat / n))


if __name__ == "__main__":

    print('How many processes?')
    n = int(input())
    processes = []
    burst_time = []
    print("Enter Burst Time(P.NO. 1, 2, 3, .. by Default)")
    for i in range(0, n):
        processes.append(i + 1)
        burst_time.append(int(input()))

    find_avg_time(processes, n, burst_time)
