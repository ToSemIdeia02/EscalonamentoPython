# Algorítmo FCFS
def fcfs_scheduling(file_name):
    # Ler dados do arquivo
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = len(lines)
        processes = []
        for i in range(n):
            p_id, arrival_time, burst_time, priority, p_type = lines[i].split()
            processes.append((p_id, int(arrival_time), int(burst_time)))

    # Organizar processos por tempo de chegada
    processes.sort(key=lambda x: x[1])

    # Calcular tempo de espera e tempo de execução
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Algorítmo FCFS
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]

    # Calcular tempo médio de espera e tempo médio de execução
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print results
    print("================================= FCFS ======================================")
    print(
        "{:<12} | {:<13} | {:<11} | {:<13} | {:<15}".format("Process ID", "Arrival Time", "Burst Time", "Waiting Time",
                                                            "Turnaround Time"))
    for i in range(n):
        p_id, arrival_time, burst_time = processes[i]
        print("{:<12} | {:<13} | {:<11} | {:<13} | {:<15}".format(p_id, arrival_time, burst_time, waiting_time[i],
                                                                  turnaround_time[i]))
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

    print("\nExecution Order:")
    execution_order = [p[0] for p in processes]
    print(" -> ".join(execution_order))
