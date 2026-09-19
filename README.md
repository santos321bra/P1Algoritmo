# Big O - O(N): Busca Linear

Exemplo pratico da complexidade de tempo **O(N)** usando o algoritmo de **Busca Linear**.

## O que o codigo faz

O programa `busca_linear.py` procura um numero dentro de uma lista, percorrendo
elemento por elemento, do inicio ao fim, ate encontrar o valor (ou concluir que
ele nao existe na lista).

## Por que e O(N)

No pior caso — quando o valor procurado esta na ultima posicao da lista ou nao
existe nela — o algoritmo precisa examinar **todos os N elementos** uma unica
vez. Se a lista dobrar de tamanho, o numero maximo de comparacoes tambem dobra.
Esse crescimento diretamente proporcional ao tamanho da entrada e a
caracteristica que define a complexidade **O(N)**.

## Como executar

```bash
python3 busca_linear.py
```

## Autor

Luiz Eduardo Oliveira Ferreira — Matricula 201911061

