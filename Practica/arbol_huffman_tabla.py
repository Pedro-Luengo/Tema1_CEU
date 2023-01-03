mensaje1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
mensaje2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
frecuencias = {}

for c in mensaje1:
  if c in frecuencias:
    frecuencias[c] += 1
  else:
    frecuencias[c] = 1

print(frecuencias) # {'H': 1, 'o': 2, 'l': 2, 'a': 1, ',': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1, '!': 1}
tuplas = [(char, freq) for char, freq in frecuencias.items()]
tuplas = sorted(tuplas, key=lambda x: x[1])
print(tuplas) # [('H', 1), ('a', 1), ('m', 1), ('u', 1), ('n', 1), ('d', 1), ('!', 1), (',', 1), (' ', 1), ('o', 2), ('l', 2)]