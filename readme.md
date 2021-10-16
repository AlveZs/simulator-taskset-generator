# Gerador de tarefas

O projeto foi criado para gerar tarefas fictícias para a simulação de tarefas de tempo real.  
Ele gera conjuntos de tarefas com utilização de 40% até 100% de 10 em 10.  

### Execução

Para executar o projeto, rode o comando:

```
python3 main.py
```
### Formato do arquivo

#### Primeira linha  
Param 0 = Número de sistemas  
Param 1 = Número de processadores  
Param 2 = Número de tarefas  

#### Demais linhas
1º parâmetro = Subtasks  
2º até nº de processadores parâmetro = WCET subtask em cada processador  
nº de processadores parâmetro + 1 = Dependência da subtask (sucessores)  
Penúltimo parâmetro = Período  
Último parâmetro = Deadline  

### Exemplo de arquivo de saída

1 3 5  
1  58.749 58.749 58.749 0  82 82  
1  6.374 6.374 6.374 0  9 9  
1  2.074 2.074 2.074 0  59 59  
1  40.39 40.39 40.39 0  64 64  
1  4.018 4.018 4.018 0  13 13  