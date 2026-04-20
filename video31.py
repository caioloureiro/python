frase = "Curso em vídeo Python"
print(frase)
print(frase[4])
print(frase[4:12])
print(frase[:13])
print(frase[13:])
print(frase[::2])
print(
"""lorem ipsum dolor sit amet, consectetur adipiscing elit.
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."""
)
print(frase.count("o"))
print(frase.upper().count("O"))
print(len(frase.strip()))
print(frase.replace("Python", "Android"))
print(frase)
print('Curso' in frase)
print(frase.lower().find("vídeo"))
print(frase.split())

frase = frase.replace(" ", "-")
print(frase)
print(frase.split("-"))
print(frase.split("-")[2][3])

input()