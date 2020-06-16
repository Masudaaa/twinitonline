import random
 
liste_cartes = []

class Carte:

    def __init__(self,id_carte,id_face_1,id_face_2,face_visible):
        self.id = id_carte
        self.id_face_1 = id_face_1
        self.id_face_2 = id_face_2
        self.face_visible = face_visible

    def retourner(self):
        if self.face_visible == 1:
            self.face_visible = 2
        elif self.face_visible == 1:
            self.face_visible = 1 


""" Creation de la liste des cartes  """

for i in range (1,129) :
    liste_cartes.append(Carte(i,i,i*2,random.randint(1,2)))

print(liste_cartes[125].id_face_2)



