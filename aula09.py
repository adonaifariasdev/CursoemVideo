frase = 'Curso em Vídeo Python'
frase1 = '   Curso em Vídeo Pyhton  '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])

print('Oi')

print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join().""")

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))

print(len(frase))

print(len(frase1))
print(len(frase.strip()))

print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)


print('Curso' in frase)
print(frase.find('Curso'))

print(frase.lower().find('vídeo'))

print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])