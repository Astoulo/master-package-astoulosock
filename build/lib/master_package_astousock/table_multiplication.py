#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    Implémentation de la table de multiplication de la valeur saisie
 
    Usage:
 
    >>> from .table_multiplication import multiplication
    >>> multiplication()
""" 
__all__ = ['multiplication']

def multiplication():
    valeur = int(input("Entrez une valeur positive pour générer la table de multiplication:"))
    if(valeur > 0):

        print(valeur , "* 1 =" , valeur *1)
        print(valeur , "* 2 =" , valeur *2)
        print(valeur , "* 3 =" , valeur *3)
        print(valeur , "* 4 =" , valeur *4)
        print(valeur , "* 5 =" , valeur *5)
        print(valeur , "* 6 =" , valeur *6)
        print(valeur , "* 7 =" , valeur *7)
        print(valeur , "* 8 =" , valeur *8)
        print(valeur , "* 9 =" , valeur *9)
        print(valeur , "* 10 =" , valeur *10)
        print(valeur , "* 11 =" , valeur *11)
        print(valeur , "* 12 =" , valeur *12)
    else:
        print("veuillez entrer une valeur positive")

if __name__ == "__main__":
    multiplication()