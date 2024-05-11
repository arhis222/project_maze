#!/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
lireLaby.py : lecture de labyrinthes / Maze input

SPDX-FileCopyrightText: 2022 UGA            <carole.adam@univ-grenoble-alpes.fr>
SPDX-License-Identifier: CC-BY-NC-SA-4.0

Voir l'avis de copyright à la fin de ce fichier.
See copyright notice at the end of this file.
--------------------------------------------------------------------------------
"""

import turtle as tt

global dicoJeu

def labyFromFile(fn) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    Read a maze from the file named fn.
    """
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut
'''
#programme principale
nom_fichier = input("Ecrivez le nom du fichier : ")
print(labyFromFile(nom_fichier))
laby,mazeIn,mazeOut=(labyFromFile(nom_fichier))
global dicoJeu
dicoJeu={'laby':laby,'mazeIn':mazeIn,'mazeOut':mazeOut,"coin_superieur(x)":0,"coin_superieur(y)":30,"longueur_cellule":30}
'''
#Affichage de labyrinthe

def afficheTextue1(dico):
    for j in range(0,len(dico['laby'])):                #pour attribuer les numeros des listes dans laby à variable "j".cette à dire qu'on donne le numero de ligne à "j"
        for i in range(len(dico['laby'][j])):           # pour attribuer les numeros des listes dans les listes  de laby à variable "i".cette à dire qu'on donne le numero de colonne à "i"
            if dico['laby'][j][i]==1:                   # si il est 1 on remplace avec #(mur),si il est 0  normalement on remplace avec " "(espace) mais si les coordonnées(ligne,colonne) sont egale à entrèe du labyrinthe on remplace avec "o" ou bien si les coordonnées(ligne,colonne) sont egale à sortie du labyrinthe on remplace avec "x"
               print('#',end='')
            if dico ['laby'][j][i]==0:
                    if dico['mazeIn']==[j,i]:
                        print("o",end="")
                    elif dico ['mazeOut']==[j,i]:
                        print("x",end="")
                    else:
                        print(" ",end="")

        print("")



#print(dicoJeu)
#print(afficheTextue1(dicoJeu))

#import turtle
def carre(couleur,largeur):
    tt.speed(100)
    tt.color(couleur)
    tt.begin_fill()
    tt.tracer(0)
    for i in range(4):
        tt.forward(largeur)
        tt.left(90)
    tt.end_fill()
    tt.up()
    tt.forward(largeur)
    tt.down()

def afficheGraphique(dico):
    tt.tracer(0)

    x = 0
    y = 0
    for j in range(0,len(dico['laby'])):                #pour attribuer les numeros des listes dans laby à variable "j".cette à dire qu'on donne le numero de ligne à "j"
        for i in range(len(dico['laby'][j])):           # pour attribuer les numeros des listes dans les listes  de laby à variable "i".cette à dire qu'on donne le numero de colonne à "i"

            if dico['laby'][j][i]==1:                   # si il est 1 on dessine un carré avec couleur voilet,si il est 0  normalement on dessine un carré blanc,en plus si il est carrefour on dessin un carré gris,  mais si les coordonnées(ligne,colonne) sont egale à entrèe du labyrinthe on desssin un carré verte(entrée) ou bien si les coordonnées(ligne,colonne) sont egale à sortie du labyrinthe on dessine un carré rouge(sortie)
               carre("purple",30)
            if dico['laby'][j][i]==0:
                    if dico['mazeIn']==[j,i]:
                        carre("green",30)
                    elif dico ['mazeOut']==[j,i]:
                        carre("red",30)
                    else:
                        if (dico["laby"][j - 1][i] == 0 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 1) or (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 0 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 1) or (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 0 and dico["laby"][j][i + 1] == 1) or (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 0):  #BONUS#ORANGE POUR IMPASSE# les 4 cas pour que type est impasse(c'est l'inverse de carrefour)
                            carre("orange",30)
                        elif (dico["laby"][j-1][i] == 0 and dico["laby"][j+1][i] ==0 and dico["laby"][j][i-1] == 0 and dico["laby"][j][i+1] == 1):    #BONUS  # #premiere cas pour dessiner un carrefour
                            carre("grey",30)
                        elif (dico["laby"][j-1][i] == 0 and dico["laby"][j+1][i] ==0 and dico["laby"][j][i-1] == 1 and dico["laby"][j][i+1] == 0):   # deuxieme cas pour dessiner un carrefour
                            carre("grey",30)
                        elif (dico["laby"][j-1][i] == 0 and dico["laby"][j+1][i] ==1 and dico["laby"][j][i-1] == 0 and dico["laby"][j][i+1] == 0):   # troisime cas pour dessiner un carrefour
                            carre("grey",30)
                        elif (dico["laby"][j-1][i] == 1 and dico["laby"][j+1][i] ==0 and dico["laby"][j][i-1] == 0 and dico["laby"][j][i+1] == 0):   # final cas pour dessiner un carrefour
                            carre("grey",30)
                        else:
                            carre("white",30)

        y -= 30  #pour ne pas dessiner dans les meme pixel cote a cote

        tt.up()
        tt.goto(x,y)
        tt.down()

    tt.up()
    tt.goto(105, 75)
    tt.down()
    carre("red",60)
    tt.up()
    tt.goto(185, 75)
    tt.down()
    carre("blue", 60)
    tt.up()
    tt.goto(265, 75)
    tt.down()
    carre("green", 60)

    tt.tracer(1)


    tt.tracer(1)
    #x += 1 normalde ama isler karisio celluelun orta noktasini bulurken ayni sekilde ustteki y de y-= 31
#3 Positionnement de la tortue

def pixel2cell(x_cor,y_cor):
    longueur_cellule = dicoJeu["longueur_cellule"]  #on donne le longuer de cellule dans dicoJeu à variable longuer_cellule
    colonne = round((x_cor-dicoJeu["coin_superieur(x)"])//longueur_cellule) +1   #pour trouver le numero de colonne on obtient le coordone de x et soustraire de le coordone de coin superieur gauche pour mesure la distance et on divise ce distance par longueur de cellule pour obtenir numero de colonne
    ligne = round((y_cor-dicoJeu["coin_superieur(y)"])//(-1*longueur_cellule)) +1 #pour trouver le numero de ligne on obtient le coordone de y et soustraire de le coordone de coin superieur gauche pour mesure la distance et on divise ce distance par longueur de cellule pour obtenir numero de ligne
    return[colonne,ligne]

#afficheGraphique(dicoJeu)
#print(pixel2cell(135,-225))

def testClic(x,y,dicoJeu="dicoJeu"):
    print(pixel2cell(x,y))
    return pixel2cell(x,y)


#tt.onscreenclick(testClic) #pour teste le fonction testclic on utilise ca
#tt.mainloop()     #pour clicker plusieur fois

#afficheGraphique(dicoJeu)

def cell2pixel(j,i):
    for x in range(1000):
        for y in range(1000,-1000,-1):
            if  pixel2cell(x,y) == [j,i]:
                return [x+15,y-15,]

#print(cell2pixel(1,2))

#4 Cases speciales
def typeCellule(colonne,ligne,dico):  #j = ligne et i = colonne et on ajoute une parametre dico
    type = "hors du labyrinthe"     #type est initialement "hors du labyrinthe" car si les coordones hors du labyrinthe ,cette une cellule vide
    for j in range(len(dico['laby'])):
        for i in range(len(dico['laby'][j])):   #je vais controller le type de cellule a partir du dictionnaire(listes).
            if (j+1 == ligne) and (i+1 == colonne):
                if dico['laby'][j][i] == 1:
                    type = "mur"
                if dico ['laby'][j][i] == 0:
                        if dico['mazeIn'] == [j,i]:
                            type = "entrée"
                        elif dico ['mazeOut'] == [j,i]:
                            type = "sortie"
                        else:
                            if (dico["laby"][j - 1][i] == 0 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 1) or (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 0 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 1) or (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 0 and dico["laby"][j][i + 1] == 1) or (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 0): #les 4 cas pour que type est impasse(c'est l'inverse de carrefour)
                                type = "impasse"
                            elif (dico["laby"][j - 1][i] == 0 and dico["laby"][j + 1][i] == 0 and dico["laby"][j][i - 1] == 0 and dico["laby"][j][i + 1] == 1):  # premiere cas pour dessiner un carrefour
                                type = "carrefour"

                            elif (dico["laby"][j - 1][i] == 0 and dico["laby"][j + 1][i] == 0 and dico["laby"][j][i - 1] == 1 and dico["laby"][j][i + 1] == 0):  # deuxieme cas pour dessiner un carrefour
                                type = "carrefour"

                            elif (dico["laby"][j - 1][i] == 0 and dico["laby"][j + 1][i] == 1 and dico["laby"][j][i - 1] == 0 and dico["laby"][j][i + 1] == 0):  # troisime cas pour dessiner un carrefour
                                type = "carrefour"

                            elif (dico["laby"][j - 1][i] == 1 and dico["laby"][j + 1][i] == 0 and dico["laby"][j][i - 1] == 0 and dico["laby"][j][i + 1] == 0):  # final cas pour dessiner un carrefour
                                type = "carrefour"
                            else:
                                type = "passage"
    return type

#print(typeCellule(0,4,dicoJeu))

#6NAVIGATION GUIDEE
'''
import turtle as tt

tt.up()  #pour que tortue ne marque pas un ligne en arrirèe plan
tt.shape("turtle")
tt.color("black")
tt.shapesize(1)
liste_chemin = []
'''
def gauche(cellule=30):
    tt.color("black")                                          #color default de tortue
    if typeCellule(pixel2cell((tt.xcor()-cellule),tt.ycor())[0],pixel2cell((tt.xcor()-cellule),tt.ycor())[1],dicoJeu)  != ("mur") and  typeCellule(pixel2cell((tt.xcor()-cellule),tt.ycor())[0],pixel2cell((tt.xcor()-cellule),tt.ycor())[1],dicoJeu)  !="hors du labyrinthe":
        tt.goto(tt.xcor()-cellule,tt.ycor())        #on prend un argument celulle pour passer autre block car on imagine que tortue se trouve au milieu de cellule pour passer au milieu de l'autre cellule il doit bouger une mesure de 2 demi-cellule donc une cellule
        print("gauche ; left")
        liste_chemin.append("gauche")


        if  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "carrefour":  #comme tortue deja bougé à cette celulle  on doit verifier type de cellule actuelle
            tt.color("dark blue")    #cas de carrefour tortue change sa couleur à bleu foncé

        elif  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "impasse":
            tt.color("pink")  #cas de impasse tortue change sa couleur à rose

        elif typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "sortie":    #cas de gagné si tortue arrive à la sortie
            tt.color("dark green")
            print("wuhuuuu félicitations tu as gagné :) ")

        return "ca marche"  # pour controller si le fonction marche ou pas

    else:                                                                                       #cas de mur ou sortie du labyrtinhe,tortue change sa couleur à rouge
        print("error: la tortue ne peut pas traverser le mur ou bien sortir de labyrinthe  ")
        tt.color("red")

def droite(cellule=30):
    tt.color("black")
    if typeCellule(pixel2cell((tt.xcor() + cellule), tt.ycor())[0],pixel2cell((tt.xcor() + cellule), tt.ycor())[1],dicoJeu) != ("mur") and typeCellule(pixel2cell((tt.xcor() + cellule), tt.ycor())[0],pixel2cell((tt.xcor() + cellule), tt.ycor())[1],dicoJeu) != "hors du labyrinthe" :
        tt.goto(tt.xcor()+cellule,tt.ycor())
        print("droite ; right")
        liste_chemin.append("droite")

        if  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "carrefour":   #comme tortue deja bougé à cette celulle  on doit verifier type de cellule actuelle
            tt.color("dark blue")    #cas de carrefour tortue change sa couleur à bleu foncé

        elif  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "impasse":
            tt.color("pink")  #cas de impasse tortue change sa couleur à rose

        elif typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "sortie":    #cas de gagné si tortue arrive à la sortie
            tt.color("dark green")
            print("wuhuuuu félicitations tu as gagné :) ")

        return "ca marche"  # pour controller si le fonction marche ou pas
    else:                                                                                       #cas de mur ou sortie du labyrtinhe,tortue change sa couleur à rouge
        print("error: la tortue ne peut pas traverser le mur ou bien sortir de labyrinthe  ")
        tt.color("red")

def bas(cellule=30):
    tt.color("black")
    if typeCellule(pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[0], pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[1],dicoJeu) != ("mur") and typeCellule(pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[0], pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[1],dicoJeu) != "hors du labyrinthe":
        tt.goto(tt.xcor() , tt.ycor()-cellule)
        print("bas ; down")
        liste_chemin.append("bas")


        if  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "carrefour":    #comme tortue deja bougé à cette celulle  on doit verifier type de cellule actuelle
            tt.color("dark blue")    #cas de carrefour tortue change sa couleur à bleu foncé

        elif  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "impasse":
            tt.color("pink")  #cas de impasse tortue change sa couleur à rose

        elif typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "sortie":   #cas de gagné si tortue arrive à la sortie
            tt.color("dark green")
            print("wuhuuuu félicitations tu as gagné :) ")

        return "ca marche"  # pour controller si le fonction marche ou pas

    else:                                                                                   #cas de mur ou sortie du labyrtinhe,tortue change sa couleur à rouge
        print("error: la tortue ne peut pas traverser le mur ou bien sortir de labyrinthe  ")
        tt.color("red")

def haut(cellule=30):
    tt.color("black")
    if typeCellule(pixel2cell(tt.xcor(),(tt.ycor()+cellule))[0], pixel2cell(tt.xcor(),(tt.ycor()+cellule))[1],dicoJeu) != ("mur") and typeCellule(pixel2cell(tt.xcor(),(tt.ycor()+cellule))[0], pixel2cell(tt.xcor(),(tt.ycor()+cellule))[1],dicoJeu) !=  "hors du labyrinthe":
        tt.goto(tt.xcor(),tt.ycor()+cellule)
        print("haut ; up")
        liste_chemin.append("haut")


        if  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "carrefour":     #comme tortue deja bougé à cette celulle  on doit verifier type de cellule actuelle
            tt.color("dark blue")    #cas de carrefour tortue change sa couleur à bleu foncé

        elif  typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "impasse":
            tt.color("pink")  #cas de impasse tortue change sa couleur à rose

        elif typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "sortie":    #cas de gagné si tortue arrive à la sortie
            tt.color("dark green")
            print("wuhuuuu félicitations tu as gagné :) ")

        return "ca marche"  # pour controller si le fonction marche ou pas
    else:                                                                                   #cas de mur ou sortie du labyrtinhe,tortue change sa couleur à rouge
        print("error: la tortue ne peut pas traverser le mur ou bien sortir de labyrinthe  ")
        tt.color("red")

# key bindings
'''
tt.onkeypress(gauche, "Left")      #si user press le button left il appel la fonction gauche
tt.onkeypress(droite, "Right")     #si user press le right left il appel la fonction droite
tt.onkeypress(haut, "Up")          #si user press le button up il appel la fonction haut
tt.onkeypress(bas, "Down")         #si user press le button down il appel la fonction bas
tt.listen()
'''
'''
# start loop
#tt.goto(15,-285)
#print(cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[0],cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[1])
tt.goto(cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[0],cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[1]) #cell2pixel duzelince burayi da duzelt
 #pour s'arreter quand on a fini le labyrinthe on fait quoi ?????
#tt.mainloop()

print(liste_chemin)
'''

def suivreChemin(li):
    i = 0
    error = 0
    cellule = 30
    while i < len(li):          #je donne les ordres des caracteres dans la liste à une valeur i et je vais controller si li[i] est egale à une fonction de deplacement,si pas on s'arrete et print "error"
        if li[i][0] == "g" and (typeCellule(pixel2cell((tt.xcor()-cellule),tt.ycor())[0],pixel2cell((tt.xcor()-cellule),tt.ycor())[1],dicoJeu)  != ("mur") and  typeCellule(pixel2cell((tt.xcor()-cellule),tt.ycor())[0],pixel2cell((tt.xcor()-cellule),tt.ycor())[1],dicoJeu)  !="hors du labyrinthe"):             #même code que fonctions de gauche
            gauche(30)
        elif li[i][0] == "d" and (typeCellule(pixel2cell((tt.xcor() + cellule), tt.ycor())[0],pixel2cell((tt.xcor() + cellule), tt.ycor())[1],dicoJeu) != ("mur") and typeCellule(pixel2cell((tt.xcor() + cellule), tt.ycor())[0],pixel2cell((tt.xcor() + cellule), tt.ycor())[1],dicoJeu) != "hors du labyrinthe") :      #même code que fonctions de droite
            droite(30)
        elif li[i][0] == "h" and (typeCellule(pixel2cell(tt.xcor(),(tt.ycor()+cellule))[0], pixel2cell(tt.xcor(),(tt.ycor()+cellule))[1],dicoJeu) != ("mur") and typeCellule(pixel2cell(tt.xcor(),(tt.ycor()+cellule))[0], pixel2cell(tt.xcor(),(tt.ycor()+cellule))[1],dicoJeu) !=  "hors du labyrinthe"):       #même code que fonctions de haut
            haut(30)
        elif li[i][0] == "b" and (typeCellule(pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[0], pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[1],dicoJeu) != ("mur") and typeCellule(pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[0], pixel2cell(tt.xcor() ,(tt.ycor()-cellule))[1],dicoJeu) != "hors du labyrinthe"):       #même code que fonctions de bas
            bas(30)
        else:
            print("error : mouvement demandé est impossible")
            i = len(li)
            error = 1
        i += 1
    if not error == 1:
        print("réussite : on a tout fait :) ")

def inverseChemin(li):
    li_inverse = []
    for i in range(len(li)-1,-1,-1) :#note on commence par len(li)-1 car pour prendre la derniere element du liste on doit soustraire "1" car ordre du liste commence par "0"
                                     #en commancant à la fin du liste initial on change les directions par son opposè et on le met dans un nouvel liste pour que l'orde du liste sera l'inverse.
        if li[i][0] == "g":
            li_inverse.append("d")
        elif li[i][0] == "d":
            li_inverse.append("g")
        elif li[i][0] == "h":
            li_inverse.append("b")
        elif li[i][0] == "b":
            li_inverse.append("h")
    suivreChemin(li_inverse)  #comme on a deja pris la version inverse du liste initial, on peut utiliser la fonction precedent(suivreChemin)
'''
liste_chemins = ['droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'haut', 'haut', 'haut', 'haut', 'haut', 'haut', 'haut', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'haut', 'haut', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite']
#suivreChemin(liste_chemins)
#inverseChemin(liste_chemins)
'''

#3eme partie Navigation automatique dans un labyrinthe simple
def tourne_gauche(direction_tortue):
    if direction_tortue == "droite":       #si directioin est droite en default, si il tourne 90 à gauche le directioin est maintenant haut
        return "haut"
    if direction_tortue == "gauche":
        return "bas"
    if direction_tortue == "haut":
        return "gauche"
    if direction_tortue == "bas":
        return "droite"

def bouger(carrefours, direction_tortue):
    if (len(carrefours) > 0) and ((tt.xcor(), tt.ycor()) == carrefours[-1]):

        carrefours.pop()  #pour supprimer le contenu du liste

    elif typeCellule(pixel2cell(tt.xcor(), tt.ycor())[0], pixel2cell(tt.xcor(), tt.ycor())[1], dicoJeu) == "carrefour":
        carrefours.append((tt.xcor(), tt.ycor()))
        direction_tortue = tourne_gauche(direction_tortue)


    elif typeCellule(pixel2cell(tt.xcor(), tt.ycor())[0], pixel2cell(tt.xcor(), tt.ycor())[1], dicoJeu) == "impasse":
        direction_tortue = tourne_gauche(direction_tortue)
        direction_tortue = tourne_gauche(direction_tortue)


    return direction_tortue

def explorer(cellule= 30,last = ""):
    liste_chemin_explorer = []
    direction_tortue = "droite"
    carrefours = []   #pour sauvegarder les coodrdonees du carrefour
    pas_bouger = 0    #si il ne bouge il change la direction,par ex si il ne bouge 2 fois il tourne gauche 2 fois
    while typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) != "sortie": #il continue jusqu'a la sortie
        dans_carrefour = typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "carrefour"  #controller si le tortue dans carrefour ou pas
        print("dans_carrefour",dans_carrefour)  #pour tester (si le code marche)
        print("pas bouger",pas_bouger)
        print("direction",direction_tortue)

        if typeCellule(pixel2cell(tt.xcor(),tt.ycor())[0],pixel2cell(tt.xcor(),tt.ycor())[1],dicoJeu) == "impasse":   #controller si le tortue dans impasse ou pas
            pas_bouger = 0 # on reset chaque fois le pas_bouger car il a deja bouge

        if dans_carrefour :
            pas_bouger = 0
        print("pas bouger 2", pas_bouger)  #pour tester (si le code marche)

        if direction_tortue == "droite": #on fais ca pour chaque direction
            if droite(cellule) == "ca marche":
                liste_chemin_explorer.append(direction_tortue)  #liste des mouvements(succes)
                direction_tortue = bouger(carrefours, direction_tortue)
                pas_bouger = 0
            else:
                if dans_carrefour:
                    direction_tortue = tourne_gauche(direction_tortue)  #tourner 3 fois a gauche  pour que tourtue tourne a droite
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)

                else:
                    pas_bouger += 1
                    if pas_bouger > 1:
                        # direction_tortue = tourne_gauche(direction_tortue)
                        direction_tortue = tourne_gauche(direction_tortue)
                        pas_bouger = 0
                    direction_tortue = tourne_gauche(direction_tortue)



        elif direction_tortue == "gauche":
            if gauche(cellule) == "ca marche":
                liste_chemin_explorer.append(direction_tortue)
                direction_tortue = bouger(carrefours, direction_tortue)
                pas_bouger = 0
            else:
                if dans_carrefour:
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)

                else:
                    pas_bouger += 1
                    if pas_bouger > 1 :
                        #direction_tortue = tourne_gauche(direction_tortue)
                        direction_tortue = tourne_gauche(direction_tortue)
                        pas_bouger = 0
                    direction_tortue = tourne_gauche(direction_tortue)


        elif direction_tortue == "bas":
            if bas(cellule) == "ca marche":
                liste_chemin_explorer.append(direction_tortue)
                direction_tortue = bouger(carrefours, direction_tortue)
                pas_bouger = 0
            else:
                if dans_carrefour:
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)

                else:
                    pas_bouger += 1
                    if pas_bouger > 1 :
                        #direction_tortue = tourne_gauche(direction_tortue)
                        direction_tortue = tourne_gauche(direction_tortue)
                        pas_bouger = 0
                    direction_tortue = tourne_gauche(direction_tortue)



        elif direction_tortue == "haut":
            if haut(cellule) == "ca marche":
                liste_chemin_explorer.append(direction_tortue)
                direction_tortue = bouger(carrefours, direction_tortue)
                pas_bouger = 0
            else:
                if dans_carrefour:
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)
                    direction_tortue = tourne_gauche(direction_tortue)
                else:
                    pas_bouger += 1
                    if pas_bouger > 1 :
                        #direction_tortue = tourne_gauche(direction_tortue)
                        direction_tortue = tourne_gauche(direction_tortue)
                        pas_bouger = 0
                    direction_tortue = tourne_gauche(direction_tortue)
    return liste_chemin_explorer




#Quatrième partie
#Extensions

def button(x,y):              #button pour retourner à la entree
    if x<165 and x>105 and y<135 and y > 75:
        tt.goto(cell2pixel(dicoJeu["mazeIn"][1] + 1, dicoJeu["mazeIn"][0] + 1)[0],cell2pixel(dicoJeu["mazeIn"][1] + 1, dicoJeu["mazeIn"][0] + 1)[1])
    #button pour lancer l’exploration automatique
    elif x < 245 and x > 185 and y < 135 and y > 75:
        liste_chemins_explorer = explorer()
        print(liste_chemins_explorer)
        inverseChemin(liste_chemins_explorer)

    #pour lancer l’exploration manuel
    elif x <325 and x >265 and y < 135 and y > 75:
        tt.onkeypress(gauche, "Left")  # si user press le button left il appel la fonction gauche
        tt.onkeypress(droite, "Right")  # si user press le right left il appel la fonction droite
        tt.onkeypress(haut, "Up")  # si user press le button up il appel la fonction haut
        tt.onkeypress(bas, "Down")  # si user press le button down il appel la fonction bas
        tt.listen()



if __name__ == "__main__":




    tt.up()  # pour que tortue ne marque pas un ligne en arrirèe plan
    tt.shape("turtle")
    tt.color("black")
    tt.shapesize(1)
    liste_chemin = []

    nom_fichier = input("Ecrivez le nom du fichier : ")
    print(labyFromFile(nom_fichier))
    laby, mazeIn, mazeOut = (labyFromFile(nom_fichier))

    dicoJeu = {'laby': laby, 'mazeIn': mazeIn, 'mazeOut': mazeOut, "coin_superieur(x)": 0, "coin_superieur(y)": 30,"longueur_cellule": 30}


    afficheGraphique(dicoJeu)






    #tt.onscreenclick(testClic) #pour teste le fonction testclic on utilise ca
    #tt.mainloop()     #pour clicker plusieur fois
    #start loop
    # tt.goto(15,-285)
    # print(cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[0],cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[1])
    tt.up()    # si on veut voire le chemin ,add hashtag
    tt.goto(cell2pixel(dicoJeu["mazeIn"][1] + 1, dicoJeu["mazeIn"][0] + 1)[0],cell2pixel(dicoJeu["mazeIn"][1] + 1, dicoJeu["mazeIn"][0] + 1)[1])  #pour que tortue commence par la entree du labyrinthe
    # pour s'arreter quand on a fini le labyrinthe on fait quoi ?????
    # tt.mainloop()
    # key bindings
    '''
    tt.onkeypress(gauche, "Left")      #si user press le button left il appel la fonction gauche
    tt.onkeypress(droite, "Right")     #si user press le right left il appel la fonction droite
    tt.onkeypress(haut, "Up")          #si user press le button up il appel la fonction haut
    tt.onkeypress(bas, "Down")         #si user press le button down il appel la fonction bas
    tt.listen()
    '''
    # start loop
    #tt.goto(15,-285)
    #print(cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[0],cell2pixel(dicoJeu["mazeIn"][1]+1,dicoJeu["mazeIn"][0]+1)[1])

    #tt.mainloop()


    liste_chemins = ['droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite',
                     'droite', 'droite', 'droite', 'droite', 'haut', 'haut', 'haut', 'haut', 'haut', 'haut', 'haut',
                     'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'gauche', 'haut',
                     'haut', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite', 'droite',
                     'droite']
    # suivreChemin(liste_chemins)
    # inverseChemin(liste_chemins)

    #liste_chemins_explorer = explorer()
    #print(liste_chemins_explorer)
    '''
    print(cell2pixel(4,-1))
    print(cell2pixel(4, -3))
    print(cell2pixel(6, -1))
    print(cell2pixel(6, -3))
    '''



    tt.onscreenclick(button)

    tt.mainloop()











# ***************************** AVIS DE COPYRIGHT ******************************
#
#     English translation hereinafter.
#
#     Ce  document est  mis à  disposition sous  LICENCE Creative  Commons
#   « Attribution - Pas d'utilisation commerciale - Partage dans les Mêmes
#   Conditions 4.0 International » (CC BY-NC-SA  4.0) dont les termes sont
#   détaillés  dans  le  fichier  CC-BY-NC-SA-4.0.txt  situé dans le sous-
#   répertoire LICENSES, ou bien sur :
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
#     Selon  les  conditions  résumées   ci-dessous,  vous  êtes  autorisé
#   à  partager  (copier, distribuer,  communiquer  ce  document par  tous
#   moyens et sous tous formats),  et adapter (remixer, transformer, créer
#   à partir de ce document) :
#     * Attribution : vous devez créditer l'Oeuvre (nom du créateur et des
#     personnes  à attribuer,  notice explicative  des droits  et crédits,
#     notice  de non-responsabilité  et lien  vers l'Oeuvre),  intégrer un
#     lien  vers la  licence  et  indiquer si  des  modifications ont  été
#     effectuées  à  l'Oeuvre  (et   conserver  les  indications  sur  les
#     précédentes modifications). Vous devez indiquer ces informations par
#     tous les moyens raisonnables,  sans toutefois suggérer que l'Offrant
#     vous  soutient ou  soutient  la  façon dont  vous  avez utilisé  son
#     Oeuvre.
#     * Pas d’Utilisation Commerciale  : vous n'êtes pas  autorisé à faire
#     un usage commercial  de cet document, tout ou partie  du matériel le
#     composant.
#     * Partage dans les Mêmes Conditions :  dans le cas où vous effectuez
#     un  remix, que  vous  transformez,  ou créez  à  partir du  matériel
#     composant l'Oeuvre originale, vous  devez diffuser l'Oeuvre modifiée
#     dans les  même conditions, c'est  à dire  avec la même  licence avec
#     laquelle l'Oeuvre originale a été diffusée.
#   Pas  de  restrictions  complémentaires  :  vous  n'êtes  pas  autorisé
#   à  appliquer des  conditions  légales ou  des  mesures techniques  qui
#   restreindraient  légalement  autrui  à   utiliser  l'Oeuvre  dans  les
#   conditions décrites par la licence.
#
#     Notez qu'aucune garantie n'est donnée.  Il se peut que la licence ne
#   vous  donne   pas  toutes  les  permissions   nécessaires  pour  votre
#   utilisation. Par exemple, certains droits  comme les droits moraux, le
#   droit des données personnelles et le droit à l'image sont susceptibles
#   de limiter votre utilisation.
#
#     Le résumé  ci-dessus n'indique  que certaines  des dispositions
#   clé de la licence.  Ce n'est  pas la licence, dont vous auriez dû
#   recevoir une  copie en même  temps que  ce document. Dans  le cas
#   contraire,   l'intégralité  de   la   licence  se   trouve  à   :
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
# ****************************** COPYRIGHT NOTICE ******************************
#
#     French translation above.
#
#     This document  is LICENSED  under Creative  Commons «  Attribution -
#   NonCommercial - ShareAlike 4.0 International » (CC BY-NC-SA 4.0) whose
#   terms are detailed in the file CC-BY-NC-SA-4.0.txt located in the sub-
#   directory LICENSES, as well as in :
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
#     Under the  terms and  conditions summarised below,  you are  free to
#   share (copy, redistribute  this document in any medium  or format) and
#   adapt (remix, transform, and build upon this document):
#     * Attribution: you must give appropriate credit (name of the creator
#     and  attribution  parties,  license notice,  disclaimer  notice  and
#     a link to the material), provide a link to the license, and indicate
#     if  changes  were  made  (and   retain  an  indication  of  previous
#     modifications). You may  do so in any reasonable manner,  but not in
#     any way that suggests the licensor endorses you or your use.
#     * NonCommercial:  you  may  not  use  the  material  for  commercial
#     purposes.
#     * ShareAlike: if you  remix, transform, or build  upon the material,
#     you must distribute your contributions under the same license as the
#     original.
#   No  additional  restrictions:  you  may   not  apply  legal  terms  or
#   technological  measures  that  legally   restrict  others  from  doing
#   anything the license permits.
#
#     Note that no warranties are given.  The license may not give you all
#   of  the permissions  necessary for  your intended  use.  For  example,
#   other rights such as publicity, privacy, or moral rights may limit how
#   you use the material.
#
#     The above summary highlights some of the key features and terms
#   of the  actual license.  It is  not the license; you  should have
#   received  a copy  of the  License along  with this  document; you
#   should carefully  review all of  the terms and conditions  of the
#   actual    license   before    using   the    licensed   material:
#   http://creativecommons.org/licenses/by-nc-sa/4.0
#
# ******************************************************************************
