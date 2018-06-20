from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

import ctypes
import _ctypes
import pygame
from pygame.locals import *
import sys

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

# couleurs pour dessiner les différents corps
SKELETON_COLORS = [pygame.color.THECOLORS["red"], 
                  pygame.color.THECOLORS["blue"], 
                  pygame.color.THECOLORS["green"], 
                  pygame.color.THECOLORS["orange"], 
                  pygame.color.THECOLORS["purple"], 
                  pygame.color.THECOLORS["yellow"], 
                  pygame.color.THECOLORS["violet"]]


class BodyGameRuntime(object):
	def __init__(self):
		pygame.init()

        # Utilisé pour gérer la vitesse de mise à jour de l'écran
		self._clock = pygame.time.Clock()

        # Réglez la largeur et la hauteur de l'écran [largeur, hauteur]
		self._infoObject = pygame.display.Info()
		self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1), 
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

		# Nom de la fenêtre pygame
		pygame.display.set_caption("Kinect for Windows v2 Body Game")

        # Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture.
		self._done = False

        # Utilisé pour gérer la vitesse de mise à jour de l'écran
		self._clock = pygame.time.Clock()

		# Objet d'exécution Kinect, nous voulons seulement des cadres de couleur et de corps
		self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)

        # surface tampon arrière pour obtenir des images couleur Kinect, couleur 32 bits, largeur et hauteur égales à la taille du cadre couleur Kinect
		self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)

        # ici, nous allons stocker des données du squelette
		self._bodies = None
		
		

	def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
		joint0State = joints[joint0].TrackingState;
		joint1State = joints[joint1].TrackingState;

        # les deux articulations ne sont pas suivies
		if (joint0State == PyKinectV2.TrackingState_NotTracked) or (joint1State == PyKinectV2.TrackingState_NotTracked): 
			return

        # les deux articulations ne sont pas * vraiment * suivies
		if (joint0State == PyKinectV2.TrackingState_Inferred) and (joint1State == PyKinectV2.TrackingState_Inferred):
			return

        # au moins un est bon 
		start = (jointPoints[joint0].x, jointPoints[joint0].y)
		end = (jointPoints[joint1].x, jointPoints[joint1].y)
		

		try:
			#Dessiner un cercle sur la position de chaque main
			pygame.draw.circle(self._frame_surface, color, (int(jointPoints[joint0].x), int(jointPoints[joint0].y)) ,75,0)
						
		except: # besoin de l'attraper en raison de possibles positions invalides (avec inf)
			pass

	def draw_body(self, joints, jointPoints, color):
		
        	#Bras droit  
		self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandRight, PyKinectV2.JointType_HandTipRight);
        	#Bras gauche
		self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandLeft, PyKinectV2.JointType_HandTipLeft);


	def draw_color_frame(self, frame, target_surface):
		target_surface.lock()
		address = self._kinect.surface_as_array(target_surface.get_buffer())
		ctypes.memmove(address, frame.ctypes.data, frame.size)
		del address
		target_surface.unlock()

	def run(self):
			
		# -------- Boucle programme principal -----------
		while not self._done:
			# --- Boucle d'événement principale
			for event in pygame.event.get(): # L'utilisateur fait quelque chose
				if event.type == pygame.QUIT: # Si l'utilisateur a cliqué sur fermer
					self._done = True # Indique que nous avons terminé, donc nous quittons cette boucle

				elif event.type == pygame.VIDEORESIZE: # fenêtre redimensionnée
					self._screen = pygame.display.set_mode(event.dict['size'], 
					pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
			
            # --- Obtenir des cadres et dessiner 
            # --- Nous avons un cadre de couleur! Remplissons la surface du tampon avec les données du cadre 
			if self._kinect.has_new_color_frame():
				frame = self._kinect.get_last_color_frame()
				self.draw_color_frame(frame, self._frame_surface)
				frame = None

            # --- Nous avons un cadre de corps, donc nous pouvons obtenir des squelettes
			if self._kinect.has_new_body_frame(): 
				self._bodies = self._kinect.get_last_body_frame()

            # --- dessiner des squelettes à _frame_surface
			if self._bodies is not None: 
				for i in range(0, self._kinect.max_body_count):
					body = self._bodies.bodies[i]
					if not body.is_tracked: 
						continue 
                    
					joints = body.joints 
                    # convertir les coordonnées de joint en espace de couleur
					joint_points = self._kinect.body_joints_to_color_space(joints)
					self.draw_body(joints, joint_points, SKELETON_COLORS[i])

            # --- recopiez les pixels de surface du tampon à l'écran, redimensionnez-le si nécessaire et conservez les proportions
            # --- (La taille de l'écran peut être différente de la taille du cadre de couleur de Kinect)
			h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()
			target_height = int(h_to_w * self._screen.get_width())
			surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height));
			self._screen.blit(surface_to_draw, (0,0))
			
			surface_to_draw = None
			pygame.display.update()

            # --- mettre à jour l'écran avec ce que nous avons dessiné.
			pygame.display.flip()

            # --- Limite à 60 images par seconde
			self._clock.tick(60)

        # Fermer le capteur Kinect, fermer la fenêtre et quittez.
		self._kinect.close()
		pygame.quit()


__main__ = "Kinect v2 Body Game"
game = BodyGameRuntime();
game.run();
