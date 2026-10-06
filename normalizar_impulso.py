import sys


def normalizar_tempo(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    cabecalho = linhas[:2]
    dados = linhas[2:]

    primeiro_tempo = float(dados[0].split()[0])

    with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(cabecalho)

        for linha in dados:
            partes = linha.split()

            if len(partes) >= 2:
                tempo = float(partes[0])
                resto = " ".join(partes[1:])

                novo_tempo = tempo - primeiro_tempo

                arquivo.write(f" {novo_tempo:.3f} {resto}\n")
            else:
                arquivo.write(linha)

    print(f"Arquivo salvo em: {arquivo_saida}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso:")
        print("python normalizar_tempo.py arquivo_entrada.eng arquivo_saida.eng")
        sys.exit(1)

    normalizar_tempo(sys.argv[1], sys.argv[2])
