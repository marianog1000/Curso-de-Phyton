def censor(text, word):
    str = text.split()
    texto = ""
    for n in str:
        if n == word:
            cant = len(n)
            texto += "*" * cant + " "
        else:
            texto += n + " "
    return texto
    
print censor("hoy es dia de sol con mucho sol", "sol")
