#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    Implémentation de l'année à verifier.
 
    Usage:
 
    >>> from .annee_bissextile import annee_bissextile
    >>> annee_bissextile()
""" 
__all__ = ['annee_bissextile']
def annee_bissextile():

    annee = int(input("Entrez l'année à verifier:"))
    if(annee %4== 0 and annee%100!=0 or annee%400==0):
        print("L'année est une année bissextile!")
    else:
        print("L'année n'est pas une année bissextile!")

if __name__ == "__main__":
    annee_bissextile()