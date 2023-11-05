from temp import Enregistrement
import hashlib
import re
import matplotlib.pyplot as plt
import pandas as pd
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
var="False"
def isValid(email):
    global var
    if re.fullmatch(regex, email):
        print("Valid email")
        var="True"
    else:
        print("\n")
        
def cesar():
    # algorithme cesar
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    msg=input("donner un message a chiffrer:")
    msg=msg.upper()
    key=int(input("donner la clé de décalage:"))
    chiffrer=''
    
    for i in msg:
        chiffrer+=alphabet[(alphabet.index(i)+key)%26]
    print(chiffrer)
    alphabet='ZYXWVUTSRQPONMLKJIHGFEDCBA'
    msg=input("donner le message a déchiffrer:")
    msg=msg.upper()
    key=int(input("donner la clé de décalage:"))
    déchiffrer=''
    
    for i in msg:
        déchiffrer+=alphabet[(alphabet.index(i)+key)%26]
    print(déchiffrer)
    
def menuA():
    mot=input("Entrez mot a haché sha256")
    choix = input("Entrez A pour hacher le mot et B pour l'attaque par dictionnaire")
    if choix=="A":
        a_string=mot
        hashed_string=hashlib.sha256(a_string.encode('utf-8')).hexdigest()
        print("le mot haché est : ",hashed_string)
    elif choix==2:
        with open("dictionnaire.txt.txt","r") as dictionnaire:
            for ligne in dictionnaire:
                if mot==ligne:
                    print("mot trouvé dans le dictionnaire: ", ligne)
                    print("attaque par dictionnaire terminée")
        
        
    
def menuC():
    import csv
    print("voici votre menu c ")
    choi=input("Entrez A pour afficher le dataset sous forme de dictionnaire et B pour afficher les courbes")
    if choi=="A":
        with open("2_james_harden_shot_chart_2023.csv",newline="") as csvfile:
            csvr=csv.DictReader(csvfile)
            for row in csvr:
                print(row)
                
    elif choi=="B":
        print("choix B")
        data=pd.read_csv("2_james_harden_shot_chart_2023.csv")
        plt.figure(figsize=(10,6))
        plt.plot(data["top"],data["left"],label="Courbe")
        plt.xlabel("Axe x")
        plt.ylabel("Axe y")
        plt.show()
        
        
    
def Menu():
    print("A-donner un mot a haché\n\t Haché le mot par sha256\n\t attaquer par dictionnaire le mot inséré\n\t revenir au menu\n\t B- décalage par cesar\n\t a-donnez un mot a chiffer\n\t cesar dans les 26 lettres\n\t b-chiffrer le message(a)\n\t c-déchiffrer le message(b)\n\t d-revenir au menu principal\n\t")
    lettre=input("Entrez A , B ou C ")
    if lettre=="B":
        cesar()
    elif lettre=="A":
        menuA()
    elif lettre=="C":
        menuC()
    
    
    
        
def mdp():
    global email
    def enregistrement(passwordn,email):
        with open("benji.txt",'a') as fichier:
            a_string=passwordn
            hashed_string=hashlib.sha256(a_string.encode('utf-8')).hexdigest()
            v=f"\n{email} {hashed_string}"
            fichier.write(v)
            print("indentifiant ajouter avec succès") 
           
            mot_hache="passwordn"
                                          
                    

        
    

                              
                        
   
    import string
    import random
    password=""
    a=int(input("Entrez 1 pour mot de passe automatique et 2 pour mot de passe manuel"))

    l2=[]
    l3=[]
    list_punctuation=[]
    list_lowercase=[]
    list_uppercase=[]
    list_digits=[]

    
    
    if a==1:
        b=random.choice(string.punctuation)
        c=random.choice(string.ascii_lowercase)
        d=random.choice(string.ascii_uppercase)
        e=random.choice(string.digits)
        f=random.choice(string.punctuation)
        g=random.choice(string.ascii_lowercase)
        h=random.choice(string.ascii_uppercase)        
        i=random.choice(string.digits)    
        password=list(b+c+d+e+f+g+h+i)
        random.shuffle(password)
        passwordm="".join(password)
        print(passwordm)
    elif a==2:
        var_punctuation="False"
        var_lower="False"
        var_digits="False"
        var_upper="False"
        while True:
            passwordn=input("entrez votre mot de passe")
            if len(passwordn)>=8:
                print("votre mot de passe est:",passwordn)
                for k in passwordn:
                    for l in string.punctuation:
                        if k==l:
                            var_punctuation="True"
                        
                            
                    for m in string.ascii_lowercase:
                        if k==m:
                            var_lower="True"
                        
                            
                    for n in string.ascii_uppercase:
                        if k==n:
                            var_upper="True"
                        
                            
                    for o in string.digits:
                        if k==o:
                            var_digits="True"
                    
                            
                
            if var_punctuation=="False"and var_lower=="False" and var_upper=="False" and var_digits=="False":
                print("mot de passe ne contient ni caracteres speciaux , ni majuscule , ni minuscule ,ni nombre")
            elif var_punctuation=="False" and var_lower=="True"and var_upper=="True" and var_digits=="True":
                print("il manque une punctuation dans votre mot de passe")
            elif var_punctuation=="True" and var_lower=="False" and var_upper=="True" and var_digits=="True":
                print("il manque un caractere minuscule dans votre mot de passe")
            elif var_punctuation=="True" and var_lower=="True" and var_upper=="False" and var_digits=="True":
                print("il manque un caractere majuscule dans votre mot de passe")
            elif var_punctuation=="True" and var_lower=="True" and var_upper=="True" and var_digits=="False":
                print("il manque un nombre dans votre mot de passe ")
            elif var_punctuation=="False" and var_lower=="False" and var_upper=="True" and var_digits=="True":
                print("il manque une punctuation et un caractere minuscule dans votre mot de passe")
            elif var_punctuation=="False" and var_lower=="False" and var_upper=="False" and var_digits=="True":
                print("il manque une punctuation , un caractere minuscule , un caractere majuscule")
            elif var_punctuation=="True" and var_lower=="False" and var_upper=="False" and var_digits=="False":
                print("il manque un caractere minuscule , un caractere majuscule , un nombre")
            elif var_punctuation=="False" and var_lower=="True" and var_upper=="False" and var_digits=="False":
                print("il manque une punctuation ,un caractere majuscule ,un nombre")
            elif var_punctuation=="False" and var_lower=="False" and var_upper=="True" and var_digits=="False":
                print("il manque une punctuation , un caractere minuscule , un nombre")
            elif var_punctuation=="False" and var_lower=="True" and var_upper=="False" and var_digits=="True":
                print("il manque une punctuation et un caractere majuscule")    
            elif var_punctuation=="False" and var_lower=="True" and var_upper=="True" and var_digits=="False":
                print("il manque une punctuation et un nombre")
            elif var_punctuation=="True"and var_lower=="True" and var_upper=="False" and var_digits=="False":
                print("il manque un caractere majuscule et un nombre ")
            elif var_punctuation=="True" and var_lower=="False" and var_upper=="True" and var_digits=="False":
                print("il manque un caractere majuscule et un nombre")
            elif var_punctuation=="True" and var_lower=="False" and var_upper=="False" and var_digits=="True":
                print("il manque un caractere minuscule et un caractere majuscue")
            elif var_punctuation=="True" and var_lower=="True" and var_upper=="True" and var_digits=="True":
                print("mot de passe","passwordn","acccepté")
                enregistrement(email,passwordn)
                break
            
                
        else:
            print("entrez un mot de passe d'une longueur 8 caractere")
    else:
        print("merci d'introduire un choix valide")
credentials={"pirates1": "azerty1","pirates2": "azerty2"}
def authenticate(username,passwordn):
    
    if username in credentials and credentials[username]==passwordn:
        return True
    else:
        return False
    
def tdbut():
    print("Enregistrement:")
    while True: 
        email=input("entrez_votre_email:")
        isValid(email)
        if var=="True":
            mdp()
            break

def debut():
    username=input("nom d'utilisateur:")
    passwordn=input("mot de passe")
    a_string=passwordn
    hashed_string=hashlib.sha256(a_string.encode('utf-8')).hexdigest()
    if authenticate(username, passwordn):
        print("Authentification reussie.")
        Menu()
    else:
        print("Authentification échouée.")
        tdbut()

debut()

    

         
    
    
                        
         
        
      






   

                
                                                                       