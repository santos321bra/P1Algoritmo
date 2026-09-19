def busca_linear(lista, alvo):

    passos = 0 

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
    numeros = [4, 8, 15, 16, 23, 42, 65, 71, 90]

    print("Lista:", numeros)
    print()

    busca_linear(numeros, 23)

    print()

    busca_linear(numeros, 90)

    print()

    busca_linear(numeros, 100)

    print()

    lista_grande = list(range(1, 1000001))
    print("Testando com lista de 1.000.000 de elementos, "
          "procurando o ultimo valor (pior caso):")
    busca_linear(lista_grande, 1000000)
