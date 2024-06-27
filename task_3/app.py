from tkinter import *
from time import sleep

#Création de la fenetre
Win=Tk()
Win.title("Visualizer")
Win.geometry("1100x800")
Win.minsize(1000, 800)
Win.config(background="#FFFFFC")

#Zone d'affichage de l'image
affichage=Frame(Win, bg="#000001", width=380,height=380)
affichage.pack(side="bottom", pady=20)


#Loading
class LoadingSplash:
    #Loading text
    Load=Label(affichage, text="Loading ....", font=("Arial", 25), fg="#FFFFFF", bg="#000001").place(x="120", y="80")
   
    #Loading blocks
    block1=Label(affichage, bg="#FFFFFC", width=2, height=1).place(x=50,y=180)
    block2=Label(affichage, bg="#FFFFFC", width=2, height=1).place(x=100,y=180)
    block3=Label(affichage, bg="#FFFFFC", width=2, height=1).place(x=150,y=180)
    block4=Label(affichage, bg="#FFFFFC", width=2, height=1).place(x=250,y=180)
    block5=Label(affichage, bg="#FFFFFC", width=2, height=1).place(x=300,y=180)
    block6=Label(affichage, bg="#FFFFFC", width=2, height=1).place(x=340,y=180)
    
    #Animation des blocks

#Titre de l'application
titre=Label(Win, text="VISUALIZER", font=("Arial", 50), bg="#FFFFFC").pack(fill="x")

#Guide pour mettre la description de l'image souhaitée
info1=Label(Win, text="Décrivez-nous l'image que vous aimeriez ", font=("Arial", 25) , bg="#FFFFFC").pack(pady=10 , fill="both")
info2=Label(Win, text="avoir dans l'espace ci-dessous" ,font=("Arial", 25) , bg="#FFFFFC").pack(fill="both")

#Fonction qui récupère la description de l'utilisateur au click du bouton créer 
def enregistrer ():
    descr=entree.get()
    
#Description de l'image
descr=StringVar()
entree=Entry(Win,textvariable=descr ,  bg="#d6cdcd" , font=("Arial", 17) )
entree.pack(fill="both", side="top", padx=200, pady=30)

#Bouton créer
crea=Button(Win, text="CREER", font=("Arial", 30) , bg="#d6cdcd", width=6 , command=enregistrer)
crea.pack(side="top" )

#Affichage de la fenetre et de tout son contenu
Win.mainloop()




