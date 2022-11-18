import sys
import mysql.connector  

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Exercice11_LDVELH"
)
mycursor = mydb.cursor()


def recupererTexteChapitreActuel(chapitreActuel):
    mycursor.execute("SELECT texte FROM chapitre WHERE id =" + str(chapitreActuel))
    requeteTexte = mycursor.fetchone()
    return str(requeteTexte)

#retourne le tableau des prochain chapitre de celui passer en parametre
def recupererChapitreSuivant(numChapitre):
    mycursor.execute("SELECT no_chapitre_destination FROM lien_chapitre INNER JOIN chapitre ON no_chapitre_origine = no_chapitre WHERE no_chapitre = " + str(numChapitre))
    requeteChapitreSuivant = mycursor.fetchall()
    tabChapitreSuivant = list(sum(requeteChapitreSuivant, ())) 
    return tabChapitreSuivant
#retourne la taille du tableau passer en parametre
def recupererTailleTableau(tab):
    nombreChapitreSuivant = len(tab)
    return nombreChapitreSuivant
     
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier MainWindow.py
from MonGamBookV3 import Ui_MainWindow

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit
        self.boutonContinuer.toggled.connect(self.continuer) 
        self.bouttonCommencer.toggled.connect(self.commencer)

    
    
    
    # On défini la fonction qu'on avait déclaré pour le clique sur le bouton
    def continuer(self):
        _translate = QtCore.QCoreApplication.translate
        c = recupererChapitreSuivant(chapitre)
        tailleTab = recupererTailleTableau(c)
        texte = recupererTexteChapitreActuel(chapitre)
        self.textChapitre.setText(texte)

        match tailleTab:
            case 0:
                return
            case 1:
                self.choix1.setText(_translate("MainWindow", str(c[0])))
                self.choix2.setVisible(False)
                self.choix3.setVisible(False)
                #self.choix4.setVisible(False)
            case 2:
                self.choix1.setText(_translate("MainWindow", str(c[0])))
                self.choix2.setText(_translate("MainWindow", str(c[1])))
                self.choix3.setVisible(False)
                #self.choix4.setVisible(False)
            case 3:
                self.choix1.setText(_translate("MainWindow", str(c[0])))
                self.choix2.setText(_translate("MainWindow", str(c[1])))
                self.choix3.setText(_translate("MainWindow", str(c[2])))
                #self.choix4.setVisible(False)
            case 4:
                self.choix1.setText(_translate("MainWindow", str(c[0])))
                self.choix2.setText(_translate("MainWindow", str(c[1])))
                self.choix3.setText(_translate("MainWindow", str(c[2])))
                #self.choix4.setText(_translate("MainWindow", str(c[3])))

        if self.choix1.isChecked():
            chapitre = c[0]
            recupererTexteChapitreActuel(chapitre)
        if self.choix2.isChecked():
            chapitre = c[1]
            recupererTexteChapitreActuel(chapitre)
        if self.choix3.isChecked():
            chapitre = c[2]
            recupererTexteChapitreActuel(chapitre)
        #if self.choix3.isChecked():
            #chapitreActuel = c[0]
            #recupererTexteChapitreActuel()


    def commencer(self):
        return "test"


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()