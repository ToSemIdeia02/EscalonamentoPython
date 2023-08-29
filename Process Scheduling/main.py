from fcfs import fcfs_scheduling
from sjf import sjf_scheduling
from rr import round_robin_scheduling
from srtf import srtf_scheduling
import os

class Scheduler:
    def __init__(self):
        pass

    # Lógica da escolha do algorítmo
    def run(self, algorithm_name, file_name, time_quantum=None):
        try:
            if algorithm_name == 'fcfs':
                fcfs_scheduling(file_name)
            elif algorithm_name == 'sjf':
                sjf_scheduling(file_name)
            elif algorithm_name == 'roundrobin' or algorithm_name == 'rr':
                if time_quantum is None:
                    raise ValueError("Esse algorítmo necessita de um quantum")
                round_robin_scheduling(file_name, time_quantum)
            elif algorithm_name == 'srtf':
                srtf_scheduling(file_name)
            else:
                raise ValueError(f"Algorítmo desconhecido: {algorithm_name}")
        except FileNotFoundError:
            print(f"Erro: arquivo '{file_name}' não encontrado")


if __name__ == '__main__':
    scheduler = Scheduler()

    # Pegar algorítmo e nome do arquivo do usuário
    algorithm_name = input("Digite um algorítmo de escalonamento (FCFS, SJF, Round Robin, SRTF): ").lower().replace(" ", "")
    file_name = input("Enter input file name: ").lower()

    # Se usuário não botou ".txt" no nome no arquivo, adicionar a extensão
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Limpar console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Verificar se o algorítmo é Round Robin, caso sim, pedir o quantum
    if algorithm_name == 'roundrobin' or algorithm_name == 'rr':
        time_quantum = int(input("Enter time quantum: "))
        scheduler.run(algorithm_name, file_name, time_quantum)
    else:
        scheduler.run(algorithm_name, file_name)
