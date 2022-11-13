#importer les bibliothèques print("Exo1 -----R^3-------")
import numpy as np 
import scipy.linalg as spla
#créer les vecteurs 4 vecteurs x et y et u et v et d'autres variables .
premierEspaceVectoriel="le sous espace vectoriel engendré par x et y "
deuxièmeEspaceVectoriel="le sous espace vectoriel engendré par u et v "
inclut="est inclut dans "
listX=[1,1,0]
listY=[1,0,1]
listU=[1,3,-2]
listV=[1,4,-3]
xVector=np.array(listX)
yVector=np.array(listY)
uVector=np.array(listU)
vVector=np.array(listV)
# Création des fonctions qui vont faire la décomposition .
def checkDecompoToU_V(b,vecteur):
    a=np.array([
        [uVector[0],vVector[0]],
        [uVector[1],vVector[1]],
        [uVector[2],vVector[2]]
        ])
    Q,R = np.linalg.qr(a)
    x=spla.solve_triangular(R,Q.T.dot(b),lower=False)
    print("On a "+str(vecteur)+" = "+str(round(x[0]))+" * u "+str(round(x[1]))+" * v ")
    return x
    
def checkDecompoToX_Y(b,vecteur):
    a=np.array([
        [xVector[0],yVector[0]],
        [xVector[1],yVector[1]],
        [xVector[2],yVector[2]]
        ])
    #print("a = "+a)
    Q,R = np.linalg.qr(a)
    x=spla.solve_triangular(R,Q.T.dot(b),lower=False)
    print("On a "+str(vecteur)+" = "+str(round(x[0]))+" * x "+str(round(x[1]))+" * y")
    return x
 
# Fonction qui présenter la reponse aprés la verification de la decomposition . 
def answerTheQuestion():
    try :
        xVectorCombina=checkDecompoToU_V(xVector,"x")
        yVectorCombina=checkDecompoToU_V(yVector,"y")
        print(premierEspaceVectoriel+inclut+deuxièmeEspaceVectoriel)
    except : 
        print("Vect(x,y) != Vect(u,v)") 
    try :         
        uVectorCombina=checkDecompoToX_Y(uVector,"u")
        vVectorCombina=checkDecompoToX_Y(vVector,"v")
        print(deuxièmeEspaceVectoriel+inclut+premierEspaceVectoriel)
        print("Vect(x,y) = Vect(u,v)")
    except : 
        print("Vect(x,y) != Vect(u,v)") 
    
    return 
       
answerTheQuestion()    


#Reference :  https://andreask.cs.illinois.edu/cs357-s15/public/demos/06-qr-applications/Solving%20Least-Squares%20Problems.html
