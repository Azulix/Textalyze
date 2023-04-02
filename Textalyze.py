import tkinter as tk
from tkinter import ttk

def analyser_texte():
    texte = texte_entree.get("1.0", "end-1c")
    mots = len(texte.split())
    phrases = len(texte.split("."))
    caracteres = len(texte)
    nb_mots.configure(text="Nombre de mots : " + str(mots))
    nb_phrases.configure(text="Nombre de phrases : " + str(phrases))
    nb_caracteres.configure(text="Nombre de caractères : " + str(caracteres))

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="#1E1E1E")
root.title("Textalyze")

style = ttk.Style()
style.configure("TLabel", background="#1E1E1E", foreground="#FFFFFF", font=("Arial", 12))
style.configure("TEntry", background="#FFFFFF", foreground="#000000", font=("Arial", 12))
style.configure("TButton", background="#373737", foreground="#FFFFFF", font=("Arial", 12))

texte_label = ttk.Label(root, text="Saisir le texte à analyser :")
texte_label.place(x=150, y=30)

texte_entree = tk.Text(root, height=4, width=50)
texte_entree.place(x=150, y=90)

analyser_bouton = ttk.Button(root, text="Analyser", command=analyser_texte)
analyser_bouton.place(x=270, y=200)

nb_mots = ttk.Label(root, text="Nombre de mots : 0")
nb_mots.place(x=150, y=300)

nb_phrases = ttk.Label(root, text="Nombre de phrases : 0")
nb_phrases.place(x=150, y=330)

nb_caracteres = ttk.Label(root, text="Nombre de caractères : 0")
nb_caracteres.place(x=150, y=360)

root.mainloop()
