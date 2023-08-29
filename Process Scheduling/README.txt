Aluno: Gustavo Augusto Palmeira Oliveira
Matrícula: 22052624

Código do algoritmo de Escalonamento
=========================

Este código implementa quatro algoritmos de agendamento diferentes: Primeiro a Chegar, Primeiro a Ser Servido (FCFS), Trabalho Mais Curto Primeiro (SJF), Round Robin, Tempo Restante Mais Curto Primeiro (SRTF) e PRIOp.

O código está organizado em arquivos separados para cada algoritmo de escalonamento (`fcfs.py`, `sjf.py`, `round_robin.py` e `srtf.py`) e um arquivo `main.py` que os importa e utiliza.

Para executar o código, é necessário ter o Python 3 instalado no seu computador. Você pode baixar o Python 3 do site oficial do Python: https://www.python.org/downloads/

Depois de ter o Python 3 instalado, abra uma janela de prompt de comando ou terminal e navegue até o diretório onde salvou os arquivos de código. Em seguida, execute o arquivo `main.py` usando o seguinte comando:

"python main.py"

O código solicitará a introdução do algoritmo de agendamento e do nome do ficheiro de entrada a utilizar. Se selecionar o algoritmo Round Robin, também lhe será pedido que introduza o quantum de tempo.

O arquivo de entrada deve conter uma linha por processo com o ID do processo, tempo de chegada, tempo de duração, a prioridade e o tipo separados por espaços. Por exemplo:

P1 0 1 0 1
P2 0 2 0 1
P3 0 3 0 1
P4 0 3 0 1
P5 0 5 0 1
P6 0 7 0 1


Depois de ter introduzido as informações necessárias, o código executará o algoritmo de escalonamento selecionado e apresentará os resultados.
