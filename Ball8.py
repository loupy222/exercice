# -*- coding: utf8 -*-
import random
import os

#lists of sentences

p_quotes=[
"Réponse positive malgré quelques,obstacles",
"La réponse est 'OUI'",
 "Biensur que oui",
 "Vous pouvez conpter dessus",
 "Avec certitude, 'OUI'"]
i_quotes=[
  "Trop d'endecisions, essayez encore dans quelques istants",
  "Vous pouver me reposer la question dans quelques instants",
  "Concentres-vous encore sur la question et recommencez",
  "l'avenir est trop flue, pour l'instant...essayez encore",
  "Mangé mes tentatives, je n'ai pas de répon se a vous donner pour l'instant, reposez votre question a nouveau"]
n_quotes =[ 
  "La réponse est 'NON'",
  "Jamais cela arrivera",
  "trop des difilcutés et donc c'est plutôt,'NON'",
  "Le destin me dit 'NON'", 
  "Pour l'instant la réponse est 'NON'"]

master_list=[p_quotes, i_quotes, n_quotes]

#start program
continuer_partie = True 
print("BIENVENNU Sur BALL8")
print("Concentrez-vous sur la question à poser")

while continuer_partie:

	def chose_list (master_list):
		rand_number = random.randint (0, len(master_list) -1)
		item =master_list[rand_number]
		return (item)
	

	def get_random_item_in(my_list):
		rand_numb = random.randint(0, len(my_list) - 1)
		item = my_list[rand_numb] 
		return item
	
	user_question = input("Quelle est la question que vous voulez poser?")

	user_answer = input("Dées que vous êtes prêt, a inerroger la balle, appuyez sur 'ENTREE'")

	print("A la question : ",user_question, "la réponse est : ",get_random_item_in(chose_list(master_list)))
	
	
	quitter = input("Souhaitez-vous me poser une autre question (o/n) ? ")
	if quitter == "n" or quitter == "N":
		print("MERCI D'AVOIR UTILISR BALL8")
		continuer_partie = False

	
os.system("pause")
continuer_partie = True	
	
