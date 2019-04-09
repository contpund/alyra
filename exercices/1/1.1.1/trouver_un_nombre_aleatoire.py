from random import randint

rand = randint(1, 100) 
# print("chiffre à trouver :",rand)

rand_i_p = rand + 11
rand_i_tp = rand + 6
rand_s_p = rand - 11
rand_s_tp = rand - 6


try:
    Try = int(input('Entrez un nombre : '))
except ValueError:
        print("Entrez un nombre")



while True:
    if rand == Try:
        print("C'est la bonne réponse.")
        break    
    
    if Try > rand:

        print("La bonne réponse est inférieure à" ,Try)
        
        if Try < rand_i_p and Try >= rand_i_tp:
            print("Continue c'est proche ( 6 à 10)")
        elif Try < rand_i_p and Try <= rand_i_tp:
            print("Continue trés c'est proche (<=5)")
        
    elif Try < rand:
        print("La bonne réponse est supérieure à" ,Try )
        
        if Try > rand_s_p and Try <= rand_s_tp:
            print("Continue c'est proche ( 6 à 10)")
        elif Try > rand_s_p and Try >= rand_s_tp:
            print("Continue trés c'est proche (5>=)")
        
    try:    
        Try = int(input('Entrez un nombre : '))

    except ValueError:
        print("Entrez un nombre")