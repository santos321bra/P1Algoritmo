def busca_linear(lista, alvo):

    passos = 0  # contador de comparacoes, so para fins didaticos

    for indice in range(len(lista)):
        passos += 1
        if lista[indice] == alvo:
            print(f"Valor {alvo} encontrado no indice {indice} "
                  f"apos {passos} comparacao(oes).")
            return indice

    print(f"Valor {alvo} nao encontrado apos {passos} comparacao(oes) "
          f"(percorreu a lista inteira).")
    return -1

if __name__ == "__main__":
      numeros = list(range(1, 100))
      alvo = int(input("Digite um numero para buscar na lista: "))
      busca_linear(numeros, alvo)