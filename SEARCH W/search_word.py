def search_word(archivo, word):
    with open(archivo) as a:
        for line in a:
            if word in line:
                yield line.strip()
                break

for i in search_word("archivo.txt", "hola"):
    print(i)
