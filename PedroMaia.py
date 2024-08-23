with open('arquivo.txt', 'w') as file:
    # Escreve algumas linhas no arquivo
    file.write("Nome: Pedro Maia\n")
    file.write("Idade: 18 anos\n")
    file.write("Motivação: Estudante do curso de SI, pelo interesse na area de tecnologia\n")

with open('arquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)