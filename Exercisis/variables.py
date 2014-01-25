# -*- coding: utf-8 -*-.

# Variables i noms.


# Declarem el nom de totes les variables que farem servir i les hi assignem un
# valor, aquest valor tambe pot ser operacions matematiques o operacions de 
# altres variables. 

cotxes = 100
espai_al_cotxe = 4.0
conductors = 30
passatgers = 90
cotxes_sense_conductor = cotxes - conductors
cotxes_amb_conductor = conductors
capacitat_de_cotxe = cotxes_amb_conductor * espai_al_cotxe
mitja_de_passatgers = passatgers / cotxes_amb_conductor


# Per a imprimir el valor de una variable podem posar:
#			
# 			print nom_de_la_variable
#			print "Text aqui", nom_de_la_variable
#			print "Text aqui", nom_de_la_variable, "Text aqui"
#			print nom_de_la_variable, "Text aqui"


print "Hi ha", cotxes,"cotxes disponibles"
print "Nomes hi ha", conductors,"conductors disponibles"
print "Hi ha", cotxes_sense_conductor, "cotxes sense conductor"
print "Es poden transportar", capacitat_de_cotxe,"passatgers"
print "Avui tenim", passatgers, "passatgers per a transportar"
print "Haurien de cabre", mitja_de_passatgers,"per cotxe per a podre-los portar a tots"








