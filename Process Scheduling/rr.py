# Algorítmo RR
def round_robin_scheduling(file_name, time_quantum):
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
    remaining_time = [p[2] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    current_time = 0

    execution_order = []

    # Algorítmo RR
    while sum(remaining_time) > 0:
        for i in range(n):
            if remaining_time[i] > 0:
                if remaining_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                    execution_order.append(processes[i][0])
                else:
                    current_time += remaining_time[i]
                    remaining_time[i] = 0
                    completion_time[i] = current_time
                    waiting_time[i] = completion_time[i] - processes[i][1] - processes[i][2]
                    turnaround_time[i] = completion_time[i] - processes[i][1]
                    execution_order.append(processes[i][0])

    # Calcular tempo médio de espera e tempo médio de execução
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print results
    print("================================ RR ==================================")
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


