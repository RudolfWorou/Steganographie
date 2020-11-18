# STEGANOGRAPHIE

#travail avec une image de taille 1450*1034 soit 1499300 pixels

# Modules nécéssaires

from PIL.Image import* 
from numpy import*

#Importation des fichiers necéssaires

i1=open("C:/Users/Rudolf/Desktop/data/Tipe/nature.jpg")
i2=open("C:/Users/Rudolf/Desktop/data/Tipe/bateau.jpg")
new=open("C:/Users/Rudolf/Desktop/data/Tipe/new.png")
new3=open("C:/Users/Rudolf/Desktop/data/Tipe/new3.png")
test=open("C:/Users/Rudolf/Desktop/data/Tipe/Sunrise.jpg")
new2=open("C:/Users/Rudolf/Desktop/data/Tipe/new2.png")
i_crible=open("C:/Users/Rudolf/Desktop/data/Tipe/new_crible.png")
i4=open("C:/Users/Rudolf/Desktop/data/Tipe/discrete_logarithm.png")
test2=open("C:/Users/Rudolf/Desktop/data/Tipe/velo.JPG")
im_adpt=open("C:/Users/Rudolf/Desktop/data/Tipe/adaptative_Lsb.png")




# Premier test pour afficher une image

def afficher_image(im):
    
    Image.show(im)

# Détermination de la taille d'une image

def taille_image(im):
    return im.size
    
# Modification d'un pixel précis de l'image

def modifier_pixel(x,y,r,v,b):
    i2=open("C:/Users/Rudolf/Desktop/data/Tipe/bo.png")
    
    i2.putpixel((x,y),(r,v,b))
    
# Ecriture en base 2 sous 8 bits d'un entier

def binaire(x):
    L=[]
    x_=x
    while x_>0:
        L.append(x_%2)
        x_//=2
    if len(L)<8:
        for i in range(len(L),8):
            L.append(0)
        return L
    return L

# Obtention de la valeur d'un entier à partir de son écriture en base 2

def valeur(L):
    n=0
    for i in range(len(L)):
        n+=L[i]*2**i
    return n

# Ici on cherche à remplacer les bits de poids faible de l'image de base par ceux de l'image à cachée
# On modifie donc les trois derniers bits pour des raisons de qualité

def imbrication_binaire_5_3(L,G):
    return[G[5],G[6],G[7],L[3],L[4],L[5],L[6],L[7]]

# Cette fonction récupère les trois derniers bits de poids faible et les modifies en bits de poids fort
# Elle permettra de récupérer les informations cachés dans les bits de bois faibles de l'image

def recuperation_3(L):
    return [0,0,0,0,1,L[0],L[1],L[2]]
    
# On cache une image im2 dans l'image im1 grâce aux bits de poids faible de im1

def imbriquer_images(im1,im2):
    
    (n,p)=taille_image(im1)
    izza3=im1
    for x in range(n):
        for y in range(p):
            a=im1.getpixel((x,y))
            b=im2.getpixel((x,y))
            
            # Imbrication de chaque uplet du pixel par la méthode précédente afin d'obtenir l'image stéganographiée
            
            r=valeur(imbrication_binaire_5_3(binaire(a[0]),binaire(b[0])))
            v=valeur(imbrication_binaire_5_3(binaire(a[1]),binaire(b[1])))
            b=valeur(imbrication_binaire_5_3(binaire(a[2]),binaire(b[2])))
            izza3.putpixel((x,y),(r,v,b))
            
    # Affichage
    
    izza3.save("C:/Users/Rudolf/Desktop/data/Tipe/new.png")
    Image.show(izza3)

# On décode ici une image codée avec la méthode précédente

def decodage_image(im):
    (n,p)=taille_image(im)
    iaz3=im
    for x in range(n):
        for y in range(p):
            a=im.getpixel((x,y))
            
            #Utilisation de la fonction récupération précédente pour obtenir l'image cachée
            
            r=valeur(recuperation_3(binaire(a[0])))
            v=valeur(recuperation_3(binaire(a[1])))
            b=valeur(recuperation_3(binaire(a[2])))
            iaz3.putpixel((x,y),(r,v,b))
            
    #Affichage
    
    iaz3.save("C:/Users/Rudolf/Desktop/data/Tipe/new2.png")
    Image.show(iaz3)
            
# Cachons y du texte dans cette image


# Fonction permettant de renversé une liste

def renverser(L):
    for i in range(len(L)//2):
        (L[i],L[len(L)-i-1])=(L[len(L)-i-1],L[i])

# Ecriture en binaire d'une liste de chaine de caractères

def binaire_texte(L):
    G=[]
    for i in range(len(L)):
        G.append(binaire(ord(L[i])))
    return G

# Le choix des imbrications est fait de façon à loger tout les bits d'un caractère dans un pixel

# Imbrication ici des trois derniers bits de poids faible dans l'uplet rouge

def imbriquer_bloc1(L,G):
    return[G[0],G[1],G[2],L[3],L[4],L[5],L[6],L[7]]
    
# Imbrication ici des trois bits suivant dans l'uplet vert

def imbriquer_bloc2(L,G):
    return[G[3],G[4],G[5],L[3],L[4],L[5],L[6],L[7]]
    
# Imbrication ici des deux bits de poids fort dans l'uplet vert  
  
def imbriquer_bloc3(L,G):
    return[G[6],G[7],L[2],L[3],L[4],L[5],L[6],L[7]]
    
# Finalisation de l'intégration du texte L à l'image im

def imbriquer_texte(im,L):
    (n,p)=taille_image(im)
    iaaz3=im
    
    # Utile pour cerner la fin du message
    
    L+="~~~"
    
    # Obtention de la liste binaire du texte
    
    G=binaire_texte(L)
    renverser(G)
    
    # Evidemment on doit s'assurer que le texte ne dépasse pas la capacité de stockage de l'image
    
    if len(G)> n*p:
        return False
    else:
        for x in range(n):
            for y in range(p):
                a=im.getpixel((x,y))
                if G!=[]:
                    A=G.pop()
                    
                    # Imbrication précédemment énoncées
                    
                    r=valeur(imbriquer_bloc1(binaire(a[0]),A))
                    v=valeur(imbriquer_bloc2(binaire(a[1]),A))
                    b=valeur(imbriquer_bloc3(binaire(a[2]),A))
                    iaaz3.putpixel((x,y),(r,v,b))
                else:
                    iaaz3.putpixel((x,y),a)        
                    
    #Affichage
    
        iaaz3.save("C:/Users/Rudolf/Desktop/data/Tipe/new3.png")
        Image.show(iaaz3)
        
# On essai ensuite de décoder le texte intégré dans notre image


def decoder_texte(im):
    L=""
    (n,p)=taille_image(im)
    
    for x in range(n):
        for y in range(p):
            a=im.getpixel((x,y))
            
        # Récupération adaptée en fonction de l'imbrication
        
            L+=chr(valeur([binaire(a[0])[0],binaire(a[0])[1],binaire(a[0])[2],binaire(a[1])[0],binaire(a[1])[1],binaire(a[1])[2],binaire(a[2])[0],binaire(a[2])[1]]))
    
    # Création d'un fichier texte 
    
    # Ouverture
    
    fichier=builtins.open("C:/Users/Rudolf/Desktop/data/Tipe/fichier.txt","w")
    
    # Ecriture
    
    for i in range(142):
        if L[i]!="~" and L[i+1]!="~" and L[i+2]!="~" :
            fichier.write(L[i])
    #Fermerture
    
    fichier.close()
            
# Analyse d'une image quelconque pour déterminer les occurences de la lettre e

def occurence_e(im):
    
    nb=0
    (n,p)=taille_image(im)
    
    for x in range(n):
        for y in range(p):
            a=im.getpixel((x,y))
            if ord("e")==valeur([binaire(a[0])[0],binaire(a[0])[1],binaire(a[0])[2],binaire(a[1])[0],binaire(a[1])[1],binaire(a[1])[2],binaire(a[2])[0],binaire(a[2])[1]]):
                nb+=1
    return nb
    
#Une Méthode de stéganalyse de la méthode LSB

#Un pixel pair remplacé par un pixel noir et un impair par un pixel blanc dans l'image stéganographiée

def lsb(n):
    if n%2==0:
        return 0
    return 255


def LSB(im):
    (n,p)=taille_image(im)
    ieea3=im
    for x in range(n):
        for y in range(p):
            a=im.getpixel((x,y))
            (r,v,b)=(lsb(a[0]),lsb(a[1]),lsb(a[2]))
            ieea3.putpixel((x,y),(r,v,b))
            
        # Affichage
        
    ieea3.save("C:/Users/Rudolf/Desktop/data/Tipe/LSB.png")
    Image.show(ieea3)
    
#La Deuxième méthode trivial d'attaque consiste à remplacé les bits de poids faible en bits de poids fort

def BitFaibleEnFort(n):
    return([0,0,0,0,0,0,0,binaire(n)[0]])
    
def AttaqueLSB(im):
    (n,p)=taille_image(im)
    i5=im
    for x in range(n):
        for y in range(p):
            a=im.getpixel((x,y))
            (r,v,b)=(valeur(BitFaibleEnFort(a[0])),valeur(BitFaibleEnFort(a[1])),valeur(BitFaibleEnFort(a[2])))
            i5.putpixel((x,y),(r,v,b))
            
    #Affichage
    
    i5.save("C:/Users/Rudolf/Desktop/data/Tipe/AttaqueLSB.png")
    Image.show(i5)
    
# Méthode du Logarithme discret pour une insertion aléatoire des données

# Ecriture en base 10 d'un nombre

def base10(x):
    L=[]
    x_=x
    while x_>0:
        L.append(x_%10)
        x_//=10
    return L
    
#Vérifie si un nombre est premier

def est_premier(n):
    d=2
    if n<2:
        return False
    else:
        while d**2<=n:
            if n%d==0:
                return False
            d+=1
        return True
        
# Cherche le premier nombre premier après n
        
def nombre_premier_apres(n):
    i=n
    while not est_premier(i):
        i+=1
    return i
    
# Exponentiation rapide

def puissance(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==0:
        y= puissance(x,n//2)
        return y*y
    else:
        z=puissance(x,(n-1)//2)
        return x*z*z
  
# Occurence d'un terme dans une liste
 
def occurence(l,L):
    nb=0
    for a in L:
        if l==a:
            nb+=1
    return nb    
      
# Finalisation de la méthode du logarithme discret avec une clé k

def discreteLogarithm(k,L,im):
    
    # Chaine de caractère en binaire
    
    m=binaire_texte(L)
    m_taille= len(m)*len(m[0])
    
    # Ecriture en base 10 de la clé afin de déterminer le nombre de chiffres qu'il contient noté x
    
    K=base10(k)
    x=0
    for i in range(len(K)):
        x+=K[i]
        
        # Choix d'un pixel de départ en fonction de x
        
    a=3*x
    
    #Détermination du premier nombre premier après k
    
    p=nombre_premier_apres(k); V=[1]; W=[p]
    
    for i in range(0,m_taille):
        
        xi=puissance(x,i+1) # puissance successive de x 
        
        V.append(xi%p) # reste de la division euclidienne par p des puissances de x: indice des pixels à modifier
        
        W.append((xi%p)%3) # reste de x%p par 3: choix entre les trois bits de poids faible à modifier
        
    (n,p)=taille_image(im)
    im4=im
    
    # Vérification que la liste V n'a pas d'occurence
    
    for l in V[1:]:
        if occurence(l,V)!=1:
            print(l , occurence(l,V))
          
    # Adaptation de la mémoire de stockage
    
    if m_taille> 3*n*p or k<= m_taille or k>=3*n*p:
        return False
    else:
        I=[]; P=[]
        for x in range(n):
            for y in range(p):
                
                # obtention des données des pixels de l'image
                
                pl=im.getpixel((x,y))
                P.append((x,y))
                P.append((x,y))
                P.append((x,y))
                I.append(binaire(pl[0]))
                I.append(binaire(pl[1]))
                I.append(binaire(pl[2]))
                
        # intégration du texte dans les pixels choisis
        
        for j in range(0, m_taille):
            I[V[j+1]][W[j+1]]=m[j//8][j%8]
            lo=V[j+1]%3
            pmp=im.getpixel(P[V[j+1]])
            if lo==0:
                r=valeur(I[V[j+1]])
                v=pmp[1]
                b=pmp[2]
                im4.putpixel(P[V[j+1]],(r,v,b))
            elif lo==1:
                r1=pmp[0]
                v1=valeur(I[V[j+1]])
                b1=pmp[2]
                im4.putpixel(P[V[j+1]],(r1,v1,b1))
            elif lo==2:
                r2=pmp[0]
                v2=pmp[1]
                b2=valeur(I[V[j+1]])
                im4.putpixel(P[V[j+1]],(r2,v2,b2))

        #Affichage        
        im4.save("C:/Users/Rudolf/Desktop/data/Tipe/discrete_logarithm.png")
        Image.show(im4)
          
# Decoder une image stéganographiée avec la méthode du logarithme discret grâce à la clé k

def decode_image_LD(k, im):
    
    # Obtention des données utiles grâce à k
    
    K=base10(k)
    x=0
    for i in range(len(K)):
        x+=K[i]
    a=3*x; p=nombre_premier_apres(k)
    V=[1]; W=[p]
    m=k//100
    for i in range(0,m):
        xi=puissance(x,(i+1))
        V.append(xi%p)
        W.append((xi%p)%3)
    (n,p)=taille_image(im)
    
    I=[]
    for x in range(n):
        for y in range(p):
            pl=im.getpixel((x,y))
            I.append(binaire(pl[0]))
            I.append(binaire(pl[1]))
            I.append(binaire(pl[2]))
    
    # Simple récupération des caractères au niveau des pixels requis
    
    L=[[0 for i in range(8)] for j in range(m//8)]
    for j in range(0,m):
        L[j//8][j%8]=I[V[j+1]][W[j+1]]
    
    M=""
    for l in range(len(L)):
        M+=chr(valeur(L[l]))
    return M

# Stéganographie adaptative 

# Gammes de pixels 

def gamme(n):
    if 0<=n<=15:
        return 3
    elif 16<=n<=31:
        return 4
    elif 32<=n<=255:
        return 5
    else:
        return False

#Insertion de k éléments du message m dans L

def inserer(m,k,L):
    for i in range(k):
        if len(m)>=k:
            a=m.pop()
            L[i]=a
    return L
    
# Finalistaion de la méthode de stéganographie adaptative

def adaptative_LSB(im,L):
    
    m=binaire_texte(L)
    m_taille= len(m)*len(m[0])
    mge=[]#message
    for i in range(m_taille):
        mge.append(m[i//8][i%8])
    renverser(mge)
    (n,p)=taille_image(im)
    im4=im
    
    # Scindé l'image en blocs de deux pixels
    Bloc=[] ; D=[]; I=[] ; G=[]
    for x in range(n-1):
        for y in range(p-1):
            I.append((x,y))
            a=im.getpixel((x,y)) ; b=im.getpixel((x,y+1))
            r1=binaire(a[0]); v1=binaire(a[1]); b1=binaire(a[2]); r2=binaire(b[0]); v2=binaire(b[1]); b2=binaire(b[2])
            Bloc.append([(r1,v1,b1),(r2,v2,b2)])
            i1=abs(b[0]-a[0]) ; i2=abs(b[1]-a[1]) ; i3=abs(b[2]-a[2])
            D.append([i1,i2,i3])
            G.append([gamme(i1),gamme(i2),gamme(i3)])
    
    if mge!=[]:
        i=0
        while i<len(mge):
            r1=valeur(inserer(mge,G[i][0],Bloc[i][0][0]))
            
            r2=valeur(inserer(mge,G[i][0],Bloc[i][1][0]))
            v1=valeur(inserer(mge,G[i][1],Bloc[i][0][1]))
            v2=valeur(inserer(mge,G[i][1],Bloc[i][1][1]))
            b1=valeur(inserer(mge,G[i][2],Bloc[i][0][2]))
            b2=valeur(inserer(mge,G[i][2],Bloc[i][1][2]))
            (x,y)=I[i]
            im4.putpixel((x,y),(r1,v1,b1))
            im4.putpixel((x,y+1),(r2,v2,b2))
            i+=1
            
    #Affichage
    
    im4.save("C:/Users/Rudolf/Desktop/data/Tipe/adaptative_Lsb.png")
    Image.show(im4)
    
# Décodage de la méthode de stéganographie adapatative

def decode_adaptative_LSB(im):
        
    G=binaire_texte(L)
    renverser(G)
    if len(G)> n*p:
        return False
    else:
        i=0
        while fibonacci(r,i*):
            for y in range(p):
                
                a=i1.getpixel((x,y))
                if G!=[]:
                    A=G.pop()
                    r=valeur(imbriquer_bloc1(binaire(a[0]),A))
                    v=valeur(imbriquer_bloc2(binaire(a[1]),A))
                    b=valeur(imbriquer_bloc3(binaire(a[2]),A))
                    i3.putpixel((x,y),(r,v,b))
                else:
                    i3.putpixel((x,y),a) 
                        
            # Affichage
            
        i3.save("C:/Users/Rudolf/Desktop/data/Tipe/new3.png")
        Image.show(i3)



                





