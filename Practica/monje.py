texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

#Separo el texto por el símbolo "#"
partes = texto.split("#")

#Recorro cada parte del texto
for i, parte in enumerate(partes):
#Agrego un punto final al final de cada línea, excepto en la última
    if i < len(partes) - 1:
        partes[i] = parte + "..."
#Agrego un salto de línea al final de cada línea, excepto en la última
    if i > 0:
        partes[i] = "\n" + parte

#Uno todas las partes del texto en una sola cadena
texto_final = "".join(partes)
print(texto_final)