# Tutto in Python è implementato utilizzando le classi. Ciò vuol dire che le
# stringhe, gli interi, i booleani e tutto ciò che vedremo nel seguito è a tutti
# gli effetti una classe.

# Di queste classi possiamo utilizzare i metodi.

abc = 'ciao come stai?'  

result = abc.capitalize()
print(result)

result = abc.upper()
print(result)

print(abc.split(sep=' '))                # ['ciao', 'come', 'stai']

print(abc.split(sep=' ', maxsplit=1))    # ['ciao', 'come stai?']

print(abc.replace(' ', '',))             # 'ciaocomestai'

new_abc = abc.rsplit(' ', maxsplit=1)
print(new_abc)                           # ['ciao come', 'stai?']

print(abc.isnumeric())                   # False