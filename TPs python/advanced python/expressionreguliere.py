import re #bibliotheque expression reguliere

regex = re.compile('[a-z]+') #verifie si c'est mot et si c'est repete une ou plusieurs fois
#compile permet de rassembler plusieurs expression reguliere
result = regex.match('toto') #verifie que ca match bien avec le mot "tempo"
print(result)

#affichage du resultat trouvé
print(result.group()) #On recupere le mot qu'on a trouve

result = regex.match('tempo, toto, python')
print(result)
print(result.group())
