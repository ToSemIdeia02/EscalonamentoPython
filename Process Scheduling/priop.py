# Algorítmo PRIOp
from queue import PriorityQueue


def priop_scheduling(file_name):
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

    # Inicializar variáveis
    current_time = 0
    pq = PriorityQueue()
    i = 0
    execution_order = []

    # Calcular tempo de espera e tempo de execução
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Algorítmo PRIOp
    while not pq.empty() or i < n:
        # Adicionar processos que chearam na fila
        while i < n and processes[i][1] <= current_time:
            pq.put((processes[i][3], i))
            i += 1

        # Checar se algum processo está pronto para executar
        if not pq.empty():
            # Separar processos de maior prioridade
            priority, index = pq.get()
            p_id, arrival_time, burst_time, _ = processes[index]

            # Executar o processo para 1 unidade de tempo
            execution_order.append(p_id)
            burst_time -= 1
            current_time += 1

            # Atualizar tempo de espera dos outros processos
            for j in range(n):
                if processes[j][0] != p_id and processes[j][1] <= current_time and burst_time > 0:
                    waiting_time[j] += 1

            # Checar se o processo acabou de executar
            if burst_time > 0:
                # Devolver o processo para a fila de prioridade
                pq.put((priority, index))
                processes[index] = (p_id, arrival_time, burst_time, priority)
            else:
                # Atualizar tempo de execução do processo completado
                turnaround_time[index] = current_time - arrival_time
        else:
            # Nenhum processo pronto para executar, passar para próximo tempo de chegada
            current_time = processes[i][1]

    # Calcular tempo médio de espera e tempo médio de execução
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print("================================= PRIOP ======================================")

    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

    print("Execution Order:")
    print(" -> ".join(execution_order))


if __name__ == '__main__':
    priop_scheduling('priop.txt')
