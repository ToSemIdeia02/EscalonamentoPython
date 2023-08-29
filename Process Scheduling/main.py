import os
import sys

from fcfs import fcfs_scheduling
from rr import round_robin_scheduling
from sjf import sjf_scheduling
from srtf import srtf_scheduling
from priop import priop_scheduling


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
            elif algorithm_name == 'priop':
                priop_scheduling(file_name)
            else:
                raise ValueError(f"Algorítmo desconhecido: {algorithm_name}")
        except FileNotFoundError:
            print(f"Erro: arquivo '{file_name}' não encontrado")


def print_usage():
    print("Uso: python main.py [opções] [nome_arquivo] [algorítmo]")
    print()
    print("Opções:")
    print("  -h, --help     Mostrar essa mensagem de ajuda e sair")
    print()
    print("Argumentos:")
    print("  nome_arquivo     Nome do arquivo de texto (opcional)")
    print()
    print("  algorítmo     Adiciona um algorítmo de escalonamento (FCFS, SJF, Round Robin, SRTF, PRIOp)")


if __name__ == '__main__':
    scheduler = Scheduler()

    # Checar se -h ou --help foram providenciados
    if '-h' in sys.argv or '--help' in sys.argv:
        print_usage()
        sys.exit(0)

    # Checar se foi providenciado um arg com nome do arquivo
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        # Pedir o nome do arquivo pro usuário
        file_name = input("Digite o nome do arquivo: ").lower()

    # Se precisar, adicionar .txt no final do nome do arquivo
    if not file_name.endswith('.txt'):
        file_name = file_name + '.txt'

    # Checar se foi providenciado um arg com nome do algorítmo
    if len(sys.argv) > 2:
        algorithm_name = sys.argv[2].lower().replace(' ', '')
    else:
        # Pegar algorítmo e nome do arquivo do usuário
        algorithm_name = input("Digite um algorítmo de escalonamento (FCFS, SJF, Round Robin, SRTF, PRIOp): ").lower().replace(
            ' ',
            '')

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
