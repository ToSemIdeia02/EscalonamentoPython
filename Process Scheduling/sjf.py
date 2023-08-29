# Algorítmo SJF
def sjf_scheduling(file_name):
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

    # Calcular tempo de espera e tempo de execução para cada processo
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    is_completed = [False] * n
    current_time = 0
    completed = 0

    execution_order = []

    while completed != n:
        minm = float('inf')
        shortest_process = -1
        for i in range(n):
            if processes[i][1] <= current_time and not is_completed[i]:
                if processes[i][2] < minm:
                    minm = processes[i][2]
                    shortest_process = i
                elif processes[i][2] == minm:
                    if processes[i][1] < processes[shortest_process][1]:
                        shortest_process = i

        if shortest_process == -1:
            current_time += 1
            continue

        execution_order.append(processes[shortest_process][0])

        completion_time[shortest_process] = processes[shortest_process][2] + current_time
        current_time += processes[shortest_process][2]
        turnaround_time[shortest_process] = completion_time[shortest_process] - processes[shortest_process][1]
        waiting_time[shortest_process] = turnaround_time[shortest_process] - processes[shortest_process][2]

        is_completed[shortest_process] = True
        completed += 1

    # Calcular tempo médio de espera e tempo médio de execução
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print results
    print("================================ SJF ==================================")
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




