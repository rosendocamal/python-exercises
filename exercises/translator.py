import translator

translatorR = translator(from_lang='SP', to_lang='EN')

txt = '¡Hola, Mundo!'

ans = translatorR.translate(txt)

print(ans)

# No funciona