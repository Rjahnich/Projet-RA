import pygame
from pygame.locals import *
import sys
import os
pygame.init()

#Chemin du dossier à changer !
os.chdir("C:/Users/Remi-laptop/Desktop/Projet_Kinect/Interface")

etat_fond = 0;


continuer = 1
wait = 0
niveau = 0
choix2 = 0
lancer = 0
compteur = 0
compteurfond = 0
positionDone = 0
pos_x = -200
pos_y = -200

x = []
y = []
parcours = []

x = [0,0,0,0,0,0]
y = [0,0,0,0,0,0]
parcours = ["","",""]

save_x = []
save_y = []
save_parcours = []

save_x = ["","","","","",""]
save_y = ["","","","","",""]
save_parcours = ["","",""]


bloquage1 = 0
bloquage2 = 0
bloquage3 = 0
bloquage4 = 0
bloquage5 = 0
bloquage6 = 0
#Lecture de la position des cibles

#Lecture de la sauvegarde des noms de parcours
fichier = open("Save_Parcours_Facile.txt","r")
contenu = fichier.read()
fichier.close()
save_parcours = contenu.split('  ')
parcour1f = save_parcours[0]
parcour2f = save_parcours[1]
parcour3f = save_parcours[2]

fichier = open("Save_Parcours_Moyen.txt","r")
contenu = fichier.read()
fichier.close()
save_parcours = contenu.split('  ')
parcour1m = save_parcours[0]
parcour2m = save_parcours[1]
parcour3m = save_parcours[2]

fichier = open("Save_Parcours_difficile.txt","r")
contenu = fichier.read()
fichier.close()
save_parcours = contenu.split('  ')
parcour1d = save_parcours[0]
parcour2d = save_parcours[1]
parcour3d = save_parcours[2]

fichier = open("Save_Parcours_Personnalise.txt","r")
contenu = fichier.read()
fichier.close()
save_parcours = contenu.split('  ')
parcour1p = save_parcours[0]
parcour2p = save_parcours[1]
parcour3p = save_parcours[2]

nom = ""

parcour = 1
edition = 0
modification = 0
enregistrement = 0
majuscule = 0
font=pygame.font.Font(None, 30)


#################DEFINITION DES IMAGES POUR L'AFFICHAGES###########################

#Ouverture de la fenêtre de presentation Pygame
fenetre = pygame.display.set_mode((1920, 1080),FULLSCREEN)

#Definition de toutes les images
fond = pygame.image.load("fond.jpg").convert()
fond2 = pygame.image.load("fond2.jpg").convert()
fond3 = pygame.image.load("fond3.jpg").convert()

bouton_facile1 = pygame.image.load("facile1.png").convert_alpha()
bouton_facile2 = pygame.image.load("facile2.png").convert_alpha()

bouton_moyen1 = pygame.image.load("moyen1.png").convert_alpha()
bouton_moyen2 = pygame.image.load("moyen2.png").convert_alpha()

bouton_difficile1 = pygame.image.load("difficile1.png").convert_alpha()
bouton_difficile2 = pygame.image.load("difficile2.png").convert_alpha()

bouton_perso1 = pygame.image.load("personnalise1.png").convert_alpha()
bouton_perso2 = pygame.image.load("personnalise2.png").convert_alpha()

bouton_fin1 = pygame.image.load("fin_partie1.png").convert()
bouton_fin2 = pygame.image.load("fin_partie2.png").convert()

bouton_lancer1 = pygame.image.load("lancer1.png").convert()
bouton_lancer2 = pygame.image.load("lancer2.png").convert()

bouton_retour1 = pygame.image.load("retour1.png").convert()
bouton_retour2 = pygame.image.load("retour2.png").convert()

bouton_editer1 = pygame.image.load("editer1.png").convert()
bouton_editer2 = pygame.image.load("editer2.png").convert()

bouton_fin1 = pygame.image.load("fin_partie1.png").convert()
bouton_fin2 = pygame.image.load("fin_partie2.png").convert()

bouton_modif1 = pygame.image.load("modif1.jpg").convert()
bouton_modif2 = pygame.image.load("modif2.jpg").convert()

message1 = pygame.image.load("message1.png").convert_alpha()
message2 = pygame.image.load("message2.png").convert_alpha()
message3 = pygame.image.load("message3.png").convert_alpha()
message4 = pygame.image.load("message4.png").convert_alpha()

cible1f = pygame.image.load("cible1f.png").convert_alpha()
cible2f = pygame.image.load("cible2f.png").convert_alpha()
cible3f = pygame.image.load("cible3f.png").convert_alpha()
cible4f = pygame.image.load("cible4f.png").convert_alpha()
cible5f = pygame.image.load("cible5f.png").convert_alpha()
cible6f = pygame.image.load("cible6f.png").convert_alpha()

cible1m = pygame.image.load("cible1m.png").convert_alpha()
cible2m = pygame.image.load("cible2m.png").convert_alpha()
cible3m = pygame.image.load("cible3m.png").convert_alpha()
cible4m = pygame.image.load("cible4m.png").convert_alpha()
cible5m = pygame.image.load("cible5m.png").convert_alpha()
cible6m = pygame.image.load("cible6m.png").convert_alpha()

cible1d = pygame.image.load("cible1d.png").convert_alpha()
cible2d = pygame.image.load("cible2d.png").convert_alpha()
cible3d = pygame.image.load("cible3d.png").convert_alpha()
cible4d = pygame.image.load("cible4d.png").convert_alpha()
cible5d = pygame.image.load("cible5d.png").convert_alpha()
cible6d = pygame.image.load("cible6d.png").convert_alpha()

cible1p = pygame.image.load("cible1p.png").convert_alpha()
cible2p = pygame.image.load("cible2p.png").convert_alpha()
cible3p = pygame.image.load("cible3p.png").convert_alpha()
cible4p = pygame.image.load("cible4p.png").convert_alpha()
cible5p = pygame.image.load("cible5p.png").convert_alpha()
cible6p = pygame.image.load("cible6p.png").convert_alpha()

mur = pygame.image.load("mur.jpg").convert()

bouton_parcour1f = pygame.image.load("parcour1fa.png").convert_alpha()
bouton_parcour1f2 = pygame.image.load("parcour1fb.png").convert_alpha()
bouton_parcour2f = pygame.image.load("parcour2fa.png").convert_alpha()
bouton_parcour2f2 = pygame.image.load("parcour2fb.png").convert_alpha()
bouton_parcour3f = pygame.image.load("parcour3fa.png").convert_alpha()
bouton_parcour3f2 = pygame.image.load("parcour3fb.png").convert_alpha()

bouton_parcour1m = pygame.image.load("parcour1ma.png").convert_alpha()
bouton_parcour1m2 = pygame.image.load("parcour1mb.png").convert_alpha()
bouton_parcour2m = pygame.image.load("parcour2ma.png").convert_alpha()
bouton_parcour2m2 = pygame.image.load("parcour2mb.png").convert_alpha()
bouton_parcour3m = pygame.image.load("parcour3ma.png").convert_alpha()
bouton_parcour3m2 = pygame.image.load("parcour3mb.png").convert_alpha()

bouton_parcour1d = pygame.image.load("parcour1da.png").convert_alpha()
bouton_parcour1d2 = pygame.image.load("parcour1db.png").convert_alpha()
bouton_parcour2d = pygame.image.load("parcour2da.png").convert_alpha()
bouton_parcour2d2 = pygame.image.load("parcour2db.png").convert_alpha()
bouton_parcour3d = pygame.image.load("parcour3da.png").convert_alpha()
bouton_parcour3d2 = pygame.image.load("parcour3db.png").convert_alpha()

bouton_parcour1p = pygame.image.load("parcour1pa.png").convert_alpha()
bouton_parcour1p2 = pygame.image.load("parcour1pb.png").convert_alpha()
bouton_parcour2p = pygame.image.load("parcour2pa.png").convert_alpha()
bouton_parcour2p2 = pygame.image.load("parcour2pb.png").convert_alpha()
bouton_parcour3p = pygame.image.load("parcour3pa.png").convert_alpha()
bouton_parcour3p2 = pygame.image.load("parcour3pb.png").convert_alpha()

def affichage(niveau,parcour):
	if niveau == 1 :
		if parcour == 1 :
			fenetre.blit(bouton_parcour1f2,(324,900))
			fenetre.blit(bouton_parcour2f,(804,900))
			fenetre.blit(bouton_parcour3f,(1284,900))
			parcour1 = font.render(parcour1f,1,(0,0,0))
			parcour2 = font.render(parcour2f,1,(255,255,255))
			parcour3 = font.render(parcour3f,1,(255,255,255))
		if parcour == 2 :
			fenetre.blit(bouton_parcour1f,(324,900))
			fenetre.blit(bouton_parcour2f2,(804,900))
			fenetre.blit(bouton_parcour3f,(1284,900))
			parcour1 = font.render(parcour1f,1,(255,255,255))
			parcour2 = font.render(parcour2f,1,(0,0,0))
			parcour3 = font.render(parcour3f,1,(255,255,255))
		if parcour == 3 :
			fenetre.blit(bouton_parcour1f,(324,900))
			fenetre.blit(bouton_parcour2f,(804,900))
			fenetre.blit(bouton_parcour3f2,(1284,900))
			parcour1 = font.render(parcour1f,1,(255,255,255))
			parcour2 = font.render(parcour2f,1,(255,255,255))
			parcour3 = font.render(parcour3f,1,(0,0,0))
	if niveau == 2 :
		if parcour == 1 :
			fenetre.blit(bouton_parcour1m2,(324,900))
			fenetre.blit(bouton_parcour2m,(804,900))
			fenetre.blit(bouton_parcour3m,(1284,900))
			parcour1 = font.render(parcour1m,1,(0,0,0))
			parcour2 = font.render(parcour2m,1,(255,255,255))
			parcour3 = font.render(parcour3m,1,(255,255,255))
		if parcour == 2 :
			fenetre.blit(bouton_parcour1m,(324,900))
			fenetre.blit(bouton_parcour2m2,(804,900))
			fenetre.blit(bouton_parcour3m,(1284,900))
			parcour1 = font.render(parcour1m,1,(255,255,255))
			parcour2 = font.render(parcour2m,1,(0,0,0))
			parcour3 = font.render(parcour3m,1,(255,255,255))
		if parcour == 3 :
			fenetre.blit(bouton_parcour1m,(324,900))
			fenetre.blit(bouton_parcour2m,(804,900))
			fenetre.blit(bouton_parcour3m2,(1284,900))
			parcour1 = font.render(parcour1m,1,(255,255,255))
			parcour2 = font.render(parcour2m,1,(255,255,255))
			parcour3 = font.render(parcour3m,1,(0,0,0))
	if niveau == 3 :
		if parcour == 1 :
			fenetre.blit(bouton_parcour1d2,(324,900))
			fenetre.blit(bouton_parcour2d,(804,900))
			fenetre.blit(bouton_parcour3d,(1284,900))
			parcour1 = font.render(parcour1d,1,(0,0,0))
			parcour2 = font.render(parcour2d,1,(255,255,255))
			parcour3 = font.render(parcour3d,1,(255,255,255))
		if parcour == 2 :
			fenetre.blit(bouton_parcour1d,(324,900))
			fenetre.blit(bouton_parcour2d2,(804,900))
			fenetre.blit(bouton_parcour3d,(1284,900))
			parcour1 = font.render(parcour1d,1,(255,255,255))
			parcour2 = font.render(parcour2d,1,(0,0,0))
			parcour3 = font.render(parcour3d,1,(255,255,255))
		if parcour == 3 :
			fenetre.blit(bouton_parcour1d,(324,900))
			fenetre.blit(bouton_parcour2d,(804,900))
			fenetre.blit(bouton_parcour3d2,(1284,900))
			parcour1 = font.render(parcour1d,1,(255,255,255))
			parcour2 = font.render(parcour2d,1,(255,255,255))
			parcour3 = font.render(parcour3d,1,(0,0,0))
	if niveau == 4 :
		if parcour == 1 :
			fenetre.blit(bouton_parcour1p2,(324,900))
			fenetre.blit(bouton_parcour2p,(804,900))
			fenetre.blit(bouton_parcour3p,(1284,900))
			parcour1 = font.render(parcour1p,1,(0,0,0))
			parcour2 = font.render(parcour2p,1,(255,255,255))
			parcour3 = font.render(parcour3p,1,(255,255,255))
		if parcour == 2 :
			fenetre.blit(bouton_parcour1p,(324,900))
			fenetre.blit(bouton_parcour2p2,(804,900))
			fenetre.blit(bouton_parcour3p,(1284,900))
			parcour1 = font.render(parcour1p,1,(255,255,255))
			parcour2 = font.render(parcour2p,1,(0,0,0))
			parcour3 = font.render(parcour3p,1,(255,255,255))
		if parcour == 3 :
			fenetre.blit(bouton_parcour1p,(324,900))
			fenetre.blit(bouton_parcour2p,(804,900))
			fenetre.blit(bouton_parcour3p2,(1284,900))
			parcour1 = font.render(parcour1p,1,(255,255,255))
			parcour2 = font.render(parcour2p,1,(255,255,255))
			parcour3 = font.render(parcour3p,1,(0,0,0))
	if edition == 0 :
		fenetre.blit(bouton_editer1,(753,1014))
	else:
		fenetre.blit(bouton_editer2,(753,1014))
	if modification == 0 :
		fenetre.blit(bouton_modif1,(965,1014))
	else:
		fenetre.blit(bouton_modif2,(965,1014))
	fenetre.blit(bouton_retour1,(10,1014))
	fenetre.blit(bouton_lancer1,(1708,1014))

	fenetre.blit(parcour1, (334,925))
	fenetre.blit(parcour2, (814,925))
	fenetre.blit(parcour3, (1294,925))
	


#BOUCLE DU PROGRAMME
while continuer:

	#FENETRE D'ACCUEIL
	if etat_fond == 0 and wait == 0 :
	
		fenetre.blit(fond, (0,0))
		compteurfond = 0
		positionDone = 0
		
		#bouton facile	
		if niveau == 1 :
			fenetre.blit(bouton_facile2,(380,800))
			fenetre.blit(message1,(573,968))
		else:
			fenetre.blit(bouton_facile1,(380,800))
		#bouton moyen		
		if niveau == 2 :
			fenetre.blit(bouton_moyen2,(680,800))
			fenetre.blit(message2,(573,968))
		else:
			fenetre.blit(bouton_moyen1,(680,800))
		#bouton difficile	
		if niveau == 3 :
			fenetre.blit(bouton_difficile2,(980,800))
			fenetre.blit(message3,(573,968))
		else:
			fenetre.blit(bouton_difficile1,(980,800))
		#bouton personnalise	
		if niveau == 4 :
			fenetre.blit(bouton_perso2,(1280,800))
			fenetre.blit(message4,(573,968))
		else:
			fenetre.blit(bouton_perso1,(1280,800))
			
		#bouton lancer
		fenetre.blit(bouton_lancer1,(859,925))

		
	#FENETRE D'EDITION	
	if etat_fond == 1 and wait == 0 :
		
		affichage(niveau,parcour)
		

	#FENTRE DE JEU 
	if etat_fond == 2 and wait == 0 :
		
		fenetre.blit(fond3, (0,0))
		fenetre.blit(bouton_fin1,(1708,1014))
		
		
	#évenement de la fenetre
	for event in pygame.event.get():
	
		#Quitter l'application
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer = 0
		
		#Relachement du bouton 1 de la souris
		if  event.type == MOUSEBUTTONUP and event.button == 1 :
			wait = 0
						
		#GESTION DES BOUTONS 1er ecran
		if etat_fond == 0 and wait == 0 :	
			#bouton facile
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 380 and event.pos[0] < 582 and event.pos[1] > 800 and event.pos[1] < 856:
				if niveau == 0 :
					niveau = 1
				else:
					niveau = 0
			#bouton moyen
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 680 and event.pos[0] < 882 and event.pos[1] > 800 and event.pos[1] < 856:
				if niveau == 0 :
					niveau = 2
				else:
					niveau = 0
			#bouton difficile		
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 980 and event.pos[0] < 1182 and event.pos[1] > 800 and event.pos[1] < 856:
				if niveau == 0 :
					niveau = 3
				else:
					niveau = 0
			#bouton personnalise
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 1280 and event.pos[0] < 1482 and event.pos[1] > 800 and event.pos[1] < 856:
				if niveau == 0 :
					niveau = 4
				else:
					niveau = 0					
					
			#bouton lancer
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 859 and event.pos[0] < 1061 and event.pos[1] > 925 and event.pos[1] < 981:
				fenetre.blit(bouton_lancer2,(859,925))
				if niveau == 0 :
					etat_fond = 0
					wait = 1
				else:
					lancer = 1
					etat_fond = 1
					wait = 1
					
			
		#GESTION DES BOUTONS FENETRE EDITION + CIBLES
		if etat_fond == 1 and wait == 0 :
			
			fenetre.blit(fond2, (0,0))
			##########En remplacement de l'écran de la kinect
			fenetre.blit(mur,(100,10))
			
			
			#Affiche les cibles avec leurs denières positions saugardés
			if modification == 0:
			
				if niveau == 1 :
					if parcour == 1 :
						fichier = open("saveXfacile1.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYfacile1.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1f, (x[0],y[0]))
						fenetre.blit(cible2f, (x[1],y[1]))
						fenetre.blit(cible3f, (x[2],y[2]))
						fenetre.blit(cible4f, (x[3],y[3]))
						fenetre.blit(cible5f, (x[4],y[4]))
						fenetre.blit(cible6f, (x[5],y[5]))
						
					if parcour == 2 :
						fichier = open("saveXfacile2.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYfacile2.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1f, (x[0],y[0]))
						fenetre.blit(cible2f, (x[1],y[1]))
						fenetre.blit(cible3f, (x[2],y[2]))
						fenetre.blit(cible4f, (x[3],y[3]))
						fenetre.blit(cible5f, (x[4],y[4]))
						fenetre.blit(cible6f, (x[5],y[5]))
						
					if parcour == 3 :
						fichier = open("saveXfacile3.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYfacile3.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1f, (x[0],y[0]))
						fenetre.blit(cible2f, (x[1],y[1]))
						fenetre.blit(cible3f, (x[2],y[2]))
						fenetre.blit(cible4f, (x[3],y[3]))
						fenetre.blit(cible5f, (x[4],y[4]))
						fenetre.blit(cible6f, (x[5],y[5]))
					
				if niveau == 2 :
					if parcour == 1 :
						fichier = open("saveXmoyen1.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYmoyen1.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1m, (x[0],y[0]))
						fenetre.blit(cible2m, (x[1],y[1]))
						fenetre.blit(cible3m, (x[2],y[2]))
						fenetre.blit(cible4m, (x[3],y[3]))
						fenetre.blit(cible5m, (x[4],y[4]))
						fenetre.blit(cible6m, (x[5],y[5]))
						
					if parcour == 2 :
						fichier = open("saveXmoyen2.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYmoyen2.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1m, (x[0],y[0]))
						fenetre.blit(cible2m, (x[1],y[1]))
						fenetre.blit(cible3m, (x[2],y[2]))
						fenetre.blit(cible4m, (x[3],y[3]))
						fenetre.blit(cible5m, (x[4],y[4]))
						fenetre.blit(cible6m, (x[5],y[5]))
						
					if parcour == 3 :
						fichier = open("saveXmoyen3.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYmoyen3.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1m, (x[0],y[0]))
						fenetre.blit(cible2m, (x[1],y[1]))
						fenetre.blit(cible3m, (x[2],y[2]))
						fenetre.blit(cible4m, (x[3],y[3]))
						fenetre.blit(cible5m, (x[4],y[4]))
						fenetre.blit(cible6m, (x[5],y[5]))
						
				if niveau == 3 :
					if parcour == 1 :
						fichier = open("saveXdifficile1.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYdifficile1.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1d, (x[0],y[0]))
						fenetre.blit(cible2d, (x[1],y[1]))
						fenetre.blit(cible3d, (x[2],y[2]))
						fenetre.blit(cible4d, (x[3],y[3]))
						fenetre.blit(cible5d, (x[4],y[4]))
						fenetre.blit(cible6d, (x[5],y[5]))
						
					if parcour == 2 :
						fichier = open("saveXdifficile2.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYdifficile2.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1d, (x[0],y[0]))
						fenetre.blit(cible2d, (x[1],y[1]))
						fenetre.blit(cible3d, (x[2],y[2]))
						fenetre.blit(cible4d, (x[3],y[3]))
						fenetre.blit(cible5d, (x[4],y[4]))
						fenetre.blit(cible6d, (x[5],y[5]))
						
					if parcour == 3 :
						fichier = open("saveXdifficile3.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYdifficile3.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1d, (x[0],y[0]))
						fenetre.blit(cible2d, (x[1],y[1]))
						fenetre.blit(cible3d, (x[2],y[2]))
						fenetre.blit(cible4d, (x[3],y[3]))
						fenetre.blit(cible5d, (x[4],y[4]))
						fenetre.blit(cible6d, (x[5],y[5]))
						
				if niveau == 4 :
					if parcour == 1 :
						fichier = open("saveXpersonnalise1.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYpersonnalise1.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1p, (x[0],y[0]))
						fenetre.blit(cible2p, (x[1],y[1]))
						fenetre.blit(cible3p, (x[2],y[2]))
						fenetre.blit(cible4p, (x[3],y[3]))
						fenetre.blit(cible5p, (x[4],y[4]))
						fenetre.blit(cible6p, (x[5],y[5]))
						
					if parcour == 2 :
						fichier = open("saveXpersonnalise2.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYpersonnalise2.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1p, (x[0],y[0]))
						fenetre.blit(cible2p, (x[1],y[1]))
						fenetre.blit(cible3p, (x[2],y[2]))
						fenetre.blit(cible4p, (x[3],y[3]))
						fenetre.blit(cible5p, (x[4],y[4]))
						fenetre.blit(cible6p, (x[5],y[5]))
						
					if parcour == 3 :
						fichier = open("saveXpersonnalise3.txt","r")
						contenu_x = fichier.read()
						fichier.close()
						fichier = open("saveYpersonnalise3.txt","r")
						contenu_y = fichier.read()
						fichier.close()
						
						save_x = contenu_x.split(' ')
						for i in range (6) :
							x[i] = int(save_x[i])
							
						save_y = contenu_y.split(' ')
						for i in range (6) :
							y[i] = int(save_y[i])
						
						fenetre.blit(cible1p, (x[0],y[0]))
						fenetre.blit(cible2p, (x[1],y[1]))
						fenetre.blit(cible3p, (x[2],y[2]))
						fenetre.blit(cible4p, (x[3],y[3]))
						fenetre.blit(cible5p, (x[4],y[4]))
						fenetre.blit(cible6p, (x[5],y[5]))
						
				#fonction affichage
				affichage(niveau,parcour)
				
			else :
				#Placement des 6 cibles si le bouton 1 de la souris est cliquée en fonction de la position de la souris
				if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 100 and event.pos[0] < 1686  and event.pos[1] >= 10 and event.pos[1] < 763:
					compteur = compteur + 1
					if compteur == 1 :
						x[0] = event.pos[0]
						y[0] = event.pos[1]
					if compteur == 2 :
						x[1] = event.pos[0]
						y[1] = event.pos[1]
					if compteur == 3 :
						x[2] = event.pos[0]
						y[2] = event.pos[1]
					if compteur == 4 :
						x[3] = event.pos[0]
						y[3] = event.pos[1]
					if compteur == 5 :
						x[4] = event.pos[0]
						y[4] = event.pos[1]
					if compteur == 6 :
						x[5] = event.pos[0]
						y[5] = event.pos[1]	
						
					
							
				#Affichage de la cible avec le mouvement de la souris	
				if 	event.type ==  MOUSEMOTION and event.pos[0] >= 100 and event.pos[0] < 1686  and event.pos[1] >= 10 and event.pos[1] < 763:
					pos_x = event.pos[0]
					pos_y = event.pos[1]	
					
				if compteur == 0 :
					if niveau == 1 :
						fenetre.blit(cible1f, (pos_x,pos_y))
					if niveau == 2 :
						fenetre.blit(cible1m, (pos_x,pos_y))
					if niveau == 3 :
						fenetre.blit(cible1d, (pos_x,pos_y))
					if niveau == 4 :
						fenetre.blit(cible1p, (pos_x,pos_y))
					affichage(niveau,parcour)
				if compteur == 1 :
					if niveau == 1 :
						fenetre.blit(cible2f, (pos_x,pos_y))
					if niveau == 2 :
						fenetre.blit(cible2m, (pos_x,pos_y))
					if niveau == 3 :
						fenetre.blit(cible2d, (pos_x,pos_y))
					if niveau == 4 :
						fenetre.blit(cible2p, (pos_x,pos_y))
					affichage(niveau,parcour)
				if compteur == 2 :
					if niveau == 1 :
						fenetre.blit(cible3f, (pos_x,pos_y))
					if niveau == 2 :
						fenetre.blit(cible3m, (pos_x,pos_y))
					if niveau == 3 :
						fenetre.blit(cible3d, (pos_x,pos_y))
					if niveau == 4 :
						fenetre.blit(cible3p, (pos_x,pos_y))
					affichage(niveau,parcour)
				if compteur == 3 :
					if niveau == 1 :
						fenetre.blit(cible4f, (pos_x,pos_y))
					if niveau == 2 :
						fenetre.blit(cible4m, (pos_x,pos_y))
					if niveau == 3 :
						fenetre.blit(cible4d, (pos_x,pos_y))
					if niveau == 4 :
						fenetre.blit(cible4p, (pos_x,pos_y))
					affichage(niveau,parcour)
				if compteur == 4 :
					if niveau == 1 :
						fenetre.blit(cible5f, (pos_x,pos_y))
					if niveau == 2 :
						fenetre.blit(cible5m, (pos_x,pos_y))
					if niveau == 3 :
						fenetre.blit(cible5d, (pos_x,pos_y))
					if niveau == 4 :
						fenetre.blit(cible5p, (pos_x,pos_y))
					affichage(niveau,parcour)
				if compteur == 5 :
					if niveau == 1 :
						fenetre.blit(cible6f, (pos_x,pos_y))
					if niveau == 2 :
						fenetre.blit(cible6m, (pos_x,pos_y))
					if niveau == 3 :
						fenetre.blit(cible6d, (pos_x,pos_y))
					if niveau == 4 :
						fenetre.blit(cible6p, (pos_x,pos_y))
					affichage(niveau,parcour)
				if compteur == 6 :
					enregistrement = 1
					modification = 0
					
					affichage(niveau,parcour)
				
				#Affichage des cibles
				for i in range (compteur):
					if niveau == 1 :
						if i == 0 and bloquage1 == 0 :
							fenetre.blit(cible1f, (x[0],y[0]))
							bloquage1 == 1
						if i == 1 and bloquage2 == 0 :
							fenetre.blit(cible2f, (x[1],y[1]))
							bloquage2 == 1
						if i == 2 and bloquage3 == 0 :
							fenetre.blit(cible3f, (x[2],y[2]))
							bloquage3 == 1
						if i == 3 and bloquage4 == 0 :
							fenetre.blit(cible4f, (x[3],y[3]))
							bloquage4 == 1
						if i == 4 and bloquage5 == 0 :
							fenetre.blit(cible5f, (x[4],y[4]))
							bloquage5 == 1
						if i == 5 and bloquage6 == 0 :
							fenetre.blit(cible6f, (x[5],y[5]))
							bloquage6 == 1
					if niveau == 2 :
						if i == 0 and bloquage1 == 0 :
							fenetre.blit(cible1m, (x[0],y[0]))
							bloquage1 == 1
						if i == 1 and bloquage2 == 0 :
							fenetre.blit(cible2m, (x[1],y[1]))
							bloquage2 == 1
						if i == 2 and bloquage3 == 0 :
							fenetre.blit(cible3m, (x[2],y[2]))
							bloquage3 == 1
						if i == 3 and bloquage4 == 0 :
							fenetre.blit(cible4m, (x[3],y[3]))
							bloquage4 == 1
						if i == 4 and bloquage5 == 0 :
							fenetre.blit(cible5m, (x[4],y[4]))
							bloquage5 == 1
						if i == 5 and bloquage6 == 0 :
							fenetre.blit(cible6m, (x[5],y[5]))
							bloquage6 == 1
					if niveau == 3 :
						if i == 0 and bloquage1 == 0 :
							fenetre.blit(cible1d, (x[0],y[0]))
							bloquage1 == 1
						if i == 1 and bloquage2 == 0 :
							fenetre.blit(cible2d, (x[1],y[1]))
							bloquage2 == 1
						if i == 2 and bloquage3 == 0 :
							fenetre.blit(cible3d, (x[2],y[2]))
							bloquage3 == 1
						if i == 3 and bloquage4 == 0 :
							fenetre.blit(cible4d, (x[3],y[3]))
							bloquage4 == 1
						if i == 4 and bloquage5 == 0 :
							fenetre.blit(cible5d, (x[4],y[4]))
							bloquage5 == 1
						if i == 5 and bloquage6 == 0 :
							fenetre.blit(cible6d, (x[5],y[5]))
							bloquage6 == 1
					if niveau == 4 :
						if i == 0 and bloquage1 == 0 :
							fenetre.blit(cible1p, (x[0],y[0]))
							bloquage1 == 1
						if i == 1 and bloquage2 == 0 :
							fenetre.blit(cible2p, (x[1],y[1]))
							bloquage2 == 1
						if i == 2 and bloquage3 == 0 :
							fenetre.blit(cible3p, (x[2],y[2]))
							bloquage3 == 1
						if i == 3 and bloquage4 == 0 :
							fenetre.blit(cible4p, (x[3],y[3]))
							bloquage4 == 1
						if i == 4 and bloquage5 == 0 :
							fenetre.blit(cible5p, (x[4],y[4]))
							bloquage5 == 1
						if i == 5 and bloquage6 == 0 :
							fenetre.blit(cible6p, (x[5],y[5]))
							bloquage6 == 1
				
				
				#Enregistrement des nouveaux emplacements des cibles
				if enregistrement == 1:
					for i in range (compteur) :
						if i  < 7 :
							#sauvegarde des positions de X
							save_x[i] = str(x[i])
							if i<5 :
								save_x[i] = save_x[i] + " "
							else:
								save_x[i] = save_x[i]
								
							#sauvegarde des positions de Y
							save_y[i] = str(y[i])
							if i<5 :
								save_y[i] = save_y[i] + " "
							else:
								save_y[i] = save_y[i]
								
							#Choix du fichier ou enregistrer les données X
							if parcour == 1 :
								if niveau == 1 :
									fichier = open("saveXfacile1.txt","w")
								if niveau == 2 :
									fichier = open("saveXmoyen1.txt","w")
								if niveau == 3 :
									fichier = open("saveXdifficile1.txt","w")
								if niveau == 4 :
									fichier = open("saveXpersonnalise1.txt","w")
							if parcour == 2 :
								if niveau == 1 :
									fichier = open("saveXfacile2.txt","w")
								if niveau == 2 :
									fichier = open("saveXmoyen2.txt","w")
								if niveau == 3 :
									fichier = open("saveXdifficile2.txt","w")
								if niveau == 4 :
									fichier = open("saveXpersonnalise2.txt","w")
							if parcour == 3 :
								if niveau == 1 :
									fichier = open("saveXfacile3.txt","w")
								if niveau == 2 :
									fichier = open("saveXmoyen3.txt","w")
								if niveau == 3 :
									fichier = open("saveXdifficile3.txt","w")
								if niveau == 4 :
									fichier = open("saveXpersonnalise3.txt","w")
							#enregistrement dans le fichier
							for i in save_x:
								fichier.write(i)
							fichier.close()
								
							#Choix du fichier ou enregistrer les données Y
							if parcour == 1 :
								if niveau == 1 :
									fichier = open("saveYfacile1.txt","w")
								if niveau == 2 :
									fichier = open("saveYmoyen1.txt","w")
								if niveau == 3 :
									fichier = open("saveYdifficile1.txt","w")
								if niveau == 4 :
									fichier = open("saveYpersonnalise1.txt","w")
							if parcour == 2 :
								if niveau == 1 :
									fichier = open("saveYfacile2.txt","w")
								if niveau == 2 :
									fichier = open("saveYmoyen2.txt","w")
								if niveau == 3 :
									fichier = open("saveYdifficile2.txt","w")
								if niveau == 4 :
									fichier = open("saveYpersonnalise2.txt","w")
							if parcour == 3 :
								if niveau == 1 :
									fichier = open("saveYfacile3.txt","w")
								if niveau == 2 :
									fichier = open("saveYmoyen3.txt","w")
								if niveau == 3 :
									fichier = open("saveYdifficile3.txt","w")
								if niveau == 4 :
									fichier = open("saveYpersonnalise3.txt","w")
							#enregistrement dans le fichier
							for i in save_y:
								fichier.write(i)
							fichier.close()
							enregistrement = 0
					
			#Saisie des carratères
			if edition == 1 :
				if niveau == 1 :
					if parcour == 1 :
						parcour1f = nom
						parcour1 = font.render(parcour1f,1,(0,0,0))
						fenetre.blit(parcour1, (334,925))
					if parcour == 2 :
						parcour2f = nom
						parcour2 = font.render(parcour2f,1,(0,0,0))
						fenetre.blit(parcour2, (814,925))
					if parcour == 3 :
						parcour3f = nom
						parcour3 = font.render(parcour3f,1,(0,0,0))
						fenetre.blit(parcour3, (1294,925))
				if niveau == 2 :
					if parcour == 1 :
						parcour1m = nom
						parcour1 = font.render(parcour1m,1,(0,0,0))
						fenetre.blit(parcour1, (334,925))
					if parcour == 2 :
						parcour2m = nom
						parcour2 = font.render(parcour2m,1,(0,0,0))
						fenetre.blit(parcour2, (814,925))
					if parcour == 3 :
						parcour3m = nom
						parcour3 = font.render(parcour3m,1,(0,0,0))
						fenetre.blit(parcour3, (1294,925))
				if niveau == 3 :
					if parcour == 1 :
						parcour1d = nom
						parcour1 = font.render(parcour1d,1,(0,0,0))
						fenetre.blit(parcour1, (334,925))
					if parcour == 2 :
						parcour2d = nom
						parcour2 = font.render(parcour2d,1,(0,0,0))
						fenetre.blit(parcour2, (814,925))
					if parcour == 3 :
						parcour3d = nom
						parcour3 = font.render(parcour3d,1,(0,0,0))
						fenetre.blit(parcour3, (1294,925))
				if niveau == 4 :
					if parcour == 1 :
						parcour1p = nom
						parcour1 = font.render(parcour1p,1,(0,0,0))
						fenetre.blit(parcour1, (334,925))
					if parcour == 2 :
						parcour2p = nom
						parcour2 = font.render(parcour2p,1,(0,0,0))
						fenetre.blit(parcour2, (814,925))
					if parcour == 3 :
						parcour3p = nom
						parcour3 = font.render(parcour3p,1,(0,0,0))
						fenetre.blit(parcour3, (1294,925))
			
				if len(nom) < 25 :
					if event.type == KEYDOWN and event.key == K_a:
						if majuscule == 1:
							nom = nom + "Q"
						else:
							nom = nom + "q"
					if event.type == KEYDOWN and event.key == K_z:
						if majuscule == 1:
							nom = nom + "W"
						else:
							nom = nom + "w"
					if event.type == KEYDOWN and event.key == K_e:
						if majuscule == 1:
							nom = nom + "E"
						else:
							nom = nom + "e"
					if event.type == KEYDOWN and event.key == K_r:
						if majuscule == 1:
							nom = nom + "R"
						else:
							nom = nom + "r"
					if event.type == KEYDOWN and event.key == K_t:
						if majuscule == 1:
							nom = nom + "T"
						else:
							nom = nom + "t"
					if event.type == KEYDOWN and event.key == K_y:
						if majuscule == 1:
							nom = nom + "Y"
						else:
							nom = nom + "y"
					if event.type == KEYDOWN and event.key == K_u:
						if majuscule == 1:
							nom = nom + "U"
						else:
							nom = nom + "u"
					if event.type == KEYDOWN and event.key == K_i:
						if majuscule == 1:
							nom = nom + "I"
						else:
							nom = nom + "i"
					if event.type == KEYDOWN and event.key == K_o:
						if majuscule == 1:
							nom = nom + "O"
						else:
							nom = nom + "o"
					if event.type == KEYDOWN and event.key == K_p:
						if majuscule == 1:
							nom = nom + "P"
						else:
							nom = nom + "p"
						
					if event.type == KEYDOWN and event.key == K_q:
						if majuscule == 1:
							nom = nom + "A"
						else:
							nom = nom + "a"
					if event.type == KEYDOWN and event.key == K_s:
						if majuscule == 1:
							nom = nom + "S"
						else:
							nom = nom + "s"
					if event.type == KEYDOWN and event.key == K_d:
						if majuscule == 1:
							nom = nom + "D"
						else:
							nom = nom + "d"
					if event.type == KEYDOWN and event.key == K_f:
						if majuscule == 1:
							nom = nom + "F"
						else:
							nom = nom + "f"
					if event.type == KEYDOWN and event.key == K_g:
						if majuscule == 1:
							nom = nom + "G"
						else:
							nom = nom + "g"
					if event.type == KEYDOWN and event.key == K_h:
						if majuscule == 1:
							nom = nom + "H"
						else:
							nom = nom + "h"
					if event.type == KEYDOWN and event.key == K_j:
						if majuscule == 1:
							nom = nom + "J"
						else:
							nom = nom + "j"
					if event.type == KEYDOWN and event.key == K_k:
						if majuscule == 1:
							nom = nom + "K"
						else:
							nom = nom + "k"
					if event.type == KEYDOWN and event.key == K_l:
						if majuscule == 1:
							nom = nom + "L"
						else:
							nom = nom + "l"
					if event.type == KEYDOWN and event.key == K_SEMICOLON:
						if majuscule == 1:
							nom = nom + "M"
						else:
							nom = nom + "m"

					if event.type == KEYDOWN and event.key == K_w:
						if majuscule == 1:
							nom = nom + "Z"
						else:
							nom = nom + "z"
					if event.type == KEYDOWN and event.key == K_x:
						if majuscule == 1:
							nom = nom + "X"
						else:
							nom = nom + "x"
					if event.type == KEYDOWN and event.key == K_c:
						if majuscule == 1:
							nom = nom + "C"
						else:
							nom = nom + "c"
					if event.type == KEYDOWN and event.key == K_v:
						if majuscule == 1:
							nom = nom + "V"
						else:
							nom = nom + "v"
					if event.type == KEYDOWN and event.key == K_b:
						if majuscule == 1:
							nom = nom + "B"
						else:
							nom = nom + "b"
					if event.type == KEYDOWN and event.key == K_n:
						if majuscule == 1:
							nom = nom + "N"
						else:
							nom = nom + "n"
					#Espace
					if event.type == KEYDOWN and event.key == K_SPACE:
						nom = nom + " "

					#Retour arrière
					if event.type == KEYDOWN and event.key == K_BACKSPACE:
						nom = nom[0:-1]
						if parcour == 1 :
							fenetre.blit(bouton_parcour1f2,(324,900))
						if parcour == 2 :
							fenetre.blit(bouton_parcour2f2,(804,900))
						if parcour == 3 :
							fenetre.blit(bouton_parcour3f2,(1284,900))


					#Majuscule --> CAPSLOCK,LSHIFT,RSHIFT	
					if event.type == KEYDOWN and event.key == K_CAPSLOCK or event.type == KEYDOWN and event.key == K_LSHIFT or event.type == KEYDOWN and event.key == K_RSHIFT:
						majuscule = 1
					if event.type == KEYUP and event.key == K_CAPSLOCK or event.type == KEYUP and event.key == K_LSHIFT or event.type == KEYUP and event.key == K_RSHIFT:
						majuscule = 0

				#Validation
				if event.type == KEYDOWN and event.key == K_RETURN:	
					edition = 0
					#Sauvegarde des noms dans un fichier texte
					if niveau == 1 :
						if parcour == 1 :
							save_parcours[0] = parcour1f
						if parcour == 2 :
							save_parcours[1] = parcour2f
						if parcour == 3 :
							save_parcours[2] = parcour3f
						
						for i in range(3) :
							if i < 2 :
								save_parcours[i] = save_parcours[i] + "  "
							else:
								save_parcours[i] = save_parcours[i]
						fichier = open("Save_Parcours_Facile.txt","w")
						for i in save_parcours:
							fichier.write(i)
						fichier.close()
						
					if niveau == 2 :
						if parcour == 1 :
							save_parcours[0] = parcour1m
						if parcour == 2 :
							save_parcours[1] = parcour2m
						if parcour == 3 :
							save_parcours[2] = parcour3m
						
						for i in range(3) :
							if i < 2 :
								save_parcours[i] = save_parcours[i] + "  "
							else:
								save_parcours[i] = save_parcours[i]
						fichier = open("Save_Parcours_Moyen.txt","w")
						for i in save_parcours:
							fichier.write(i)
						fichier.close()
					
					if niveau == 3 :
						if parcour == 1 :
							save_parcours[0] = parcour1d
						if parcour == 2 :
							save_parcours[1] = parcour2d
						if parcour == 3 :
							save_parcours[2] = parcour3d
						
						for i in range(3) :
							if i < 2 :
								save_parcours[i] = save_parcours[i] + "  "
							else:
								save_parcours[i] = save_parcours[i]
						fichier = open("Save_Parcours_Difficile.txt","w")
						for i in save_parcours:
							fichier.write(i)
						fichier.close()
						
					if niveau == 4 :
						if parcour == 1 :
							save_parcours[0] = parcour1p
						if parcour == 2 :
							save_parcours[1] = parcour2p
						if parcour == 3 :
							save_parcours[2] = parcour3p
						
						for i in range(3) :
							if i < 2 :
								save_parcours[i] = save_parcours[i] + "  "
							else:
								save_parcours[i] = save_parcours[i]
						fichier = open("Save_Parcours_Personnalise.txt","w")
						for i in save_parcours:
							fichier.write(i)
						fichier.close()
			
			#boutons parcours
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 324 and event.pos[0] < 635 and event.pos[1] > 900 and event.pos[1] < 969 and edition == 0:
				parcour = 1
				wait = 1
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 804 and event.pos[0] < 1115 and event.pos[1] > 900 and event.pos[1] < 969 and edition == 0:
				parcour = 2
				wait = 1
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 1284 and event.pos[0] < 1595 and event.pos[1] > 900 and event.pos[1] < 969 and edition == 0:
				parcour = 3
				wait = 1	
			
			#bouton modification de l'emplacement de cibles
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 965 and event.pos[0] < 1167 and event.pos[1] > 1015 and event.pos[1] < 1070:
				modification = 1
				compteur = 0
				bloquage1 = 0
				bloquage2 = 0
				bloquage3 = 0
				bloquage4 = 0
				bloquage5 = 0
				bloquage6 = 0
				wait = 1
				
			#bouton editer texte des parcours
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 753 and event.pos[0] < 955 and event.pos[1] > 1014 and event.pos[1] < 1070:
				edition = 1
				nom = ""
				wait = 1
			
			#bouton retour
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 10 and event.pos[0] < 212 and event.pos[1] > 1014 and event.pos[1] < 1070:
				fenetre.blit(bouton_retour2,(10,1014))
				compteur = 0
				etat_fond = 0
				wait = 1
				
			#bouton lancer
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 1708 and event.pos[0] < 1910 and event.pos[1] > 1014 and event.pos[1] < 1070:
				fenetre.blit(bouton_lancer2,(1708,1014))
				etat_fond = 2
				wait = 1

		#FENETRE DE JEU
		if etat_fond == 2 and wait == 0 :
			#bouton fin de partie
			if  event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 1708 and event.pos[0] < 1910 and event.pos[1] > 1014 and event.pos[1] < 1070:
				fenetre.blit(bouton_fin2,(1708,1014))
				etat_fond = 0;
				wait = 1
			
				#ajouter l'écran de la kinect
			
			
	pygame.display.flip()
	

	
	
	
	