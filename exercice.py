#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def order(values: list = None) -> list:
    values=list([])
    for i in range(10) :
        entrez=input("Entrez une valeur : ")
        if entrez.isdigit()==True :
            values.append(float(entrez))
        else:
            values.append(entrez)
        values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        word1=input("Le 1er Mot : ")
        word2=input("Le 2eme Mot : ")
        somme_word1=0
        somme_word2=0
        for chr in word1 :
            somme_word1 += ord(chr)
        for chr in word2 :
            somme_word2 += ord(chr)
        if somme_word1==somme_word2 :    
            return True
        else :
            return False


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    meilleure_moyenne=0
    etudiant=""
    for element in student_grades :
        moyenne = sum(student_grades[element])/len(student_grades[element])
        if moyenne > meilleure_moyenne :
            meilleure_moyenne= moyenne
            etudiant=element
    
    return {etudiant : meilleure_moyenne}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    List={}
    for element in sentence :
        if sentence.count(element) >5 :
            List[element]=sentence.count(element)
        sorted_List=sorted(List.items(),key=lambda x:x[1],reverse=True)

    return sorted_List


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom_recette=input("entrez le nom de recette")
    ingredients= input("entrez les ingrendients separess d'espace")
    ingredients=ingredients.split()
    return {nom_recette: ingredients}



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette=input("entrez le nom de la recette")
    if recette in ingredients :
        print()


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
