from tkinter import *
from tkinter import messagebox
import random

# initialisation de la fenetre


root = Tk()
root.title("CISEAUX - PIERRE - FEUILLE")
root.configure(bg="#FFD878")
root.geometry("247x250")



# creation d'une bande publicitaire en mouvement


def  move_label():
    global x
    x -= 1
    if x < -label.winfo_width():
        x = root.winfo_width()
    label.place(x=x, y=220)
    root.after(50, move_label)

x = root.winfo_width()
label = Label(root, text="Ciseaux - Pierre - Feuille :  jouez et gagnez des milions  : - )",
              font="Helvetica 12 bold",  bg="#FFD878", fg="red")
label.place(x=x, y=50)

move_label()


# Installation des elements de la fenetre


consigne_utilisateur = Label(root, text = "Votre choix :  ", font="Helvetica 14 bold", bg="#FFD878")
consigne_utilisateur .place(x=10, y=0)

saisie_utilisateur = Entry(root, font="Helvetica 14 italic")
saisie_utilisateur .place(x=10, y=30)

consigne_ordinateur = Label(root, text=" Choix de l'ordi :  ", font="Helvetica 14 bold",bg="#FFD878")
consigne_ordinateur.place(x=2, y=60)

affichage_choix_ordi = Label(root, font="Helvetica 14 italic", bg="#FFD878")
affichage_choix_ordi.place(x=160, y=60)

resultat_label = Label(root, font="Helvetica 14 italic", bg="#FFD878")
resultat_label.place(x=10, y=100)


# Fonction de logique du jeu


def jouer():
    choix_utilisateur = saisie_utilisateur.get().lower()
    choix_possible = ["ciseaux", "pierre", "feuille"]
    choix_ordi =  random.choice(choix_possible)

    if choix_utilisateur not in choix_possible:
        messagebox.showerror("Erreur", f"Vous ne pouvez pas choisir : {choix_utilisateur} \n Choix possible :  ciseau, pierre et feuille !")
        return
    affichage_choix_ordi.config(text=f"{choix_ordi}")

    if  choix_utilisateur == choix_ordi:
        resultat = "Egalité"

    elif  (choix_utilisateur == "ciseau"  and  choix_ordi == "feuille") or \
         (choix_utilisateur == "feuille"  and  choix_ordi == "pierre") or \
         (choix_utilisateur == "pierre"  and  choix_ordi  == "ciseau"):
        resultat = "Vous avez gagnez  :-) "

    else :
        resultat = "Vous avez perdu  :-("

    resultat_label.config(text=f"{resultat}")


# Fonction de reinitialisation du jeu


def reinit():
    saisie_utilisateur.delete(0, END)
    affichage_choix_ordi.config(text="")
    resultat_label.config(text="")

# Fonction pour quitter le jeu


def quitter_jeu():
    root.destroy()


# Les trois boutons d'action


btn_jouer = Button(root, text="Jouer",  bg="lightgreen",  font="Helvetica 14 bold", command=jouer)
btn_jouer.place(x=10, y=150)

btn_reinitialiser = Button(root, text="Réinit", font="Helvetica 14 bold", bg="orange", command=reinit)
btn_reinitialiser.place(x=83, y=150)

btn_quitter = Button(root, text="Quitter", font="Helvetica 14 bold", bg="red", command=quitter_jeu)
btn_quitter.place(x=154, y=150)





root.mainloop()


