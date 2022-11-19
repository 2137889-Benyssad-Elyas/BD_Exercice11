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
    mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre =" + str(chapitreActuel))
    requeteTexte = mycursor.fetchone()
    return str(requeteTexte,)

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
from MonGamebookv5 import Ui_MainWindow

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit
        self.boutonContinuer.toggled.connect(self.continuer) 
        self.chapitre = 1
        #self.bouttonCommencer.toggled.connect(self.commencer)
        self.recupererNomArme()
        self.recupererNomKai()
        self.chargerPartie()


    def recupererNomArme(self):
        _translate = QtCore.QCoreApplication.translate
        mycursor.execute("SELECT nom FROM arme")
        requeteTabNomArme = mycursor.fetchall()
        tabNomArme = list(sum(requeteTabNomArme, ()))
        c = 0
        for arme in tabNomArme:
            self.comboBox.setItemText(c, _translate("MainWindow", tabNomArme[c]))
            self.comboBox_2.setItemText(c, _translate("MainWindow", tabNomArme[c]))
            c = c + 1 

    def recupererNomKai(self):
        _translate = QtCore.QCoreApplication.translate
        mycursor.execute("SELECT nom FROM discipline_kai")
        requeteTabNomKai = mycursor.fetchall()
        tabNomkai = list(sum(requeteTabNomKai, ()))
        c = 0
        for arme in tabNomkai:
            self.comboBox_3.setItemText(c, _translate("MainWindow", tabNomkai[c]))
            self.comboBox_4.setItemText(c, _translate("MainWindow", tabNomkai[c]))
            c = c + 1 

    
    # On défini la fonction qu'on avait déclaré pour le clique sur le bouton
    def continuer(self):
        _translate = QtCore.QCoreApplication.translate
        tabChapitreSuivant = recupererChapitreSuivant(self.chapitre)
        tailleTab = recupererTailleTableau(tabChapitreSuivant)
        texte = recupererTexteChapitreActuel(self.chapitre)
        self.textChapitre.setText(texte)

        match tailleTab:
            case 0:
                print("fin du game")
            case 1:
                self.choix1.setText(_translate("MainWindow", str(tabChapitreSuivant[0])))
                self.choix2.setVisible(False)
                self.choix3.setVisible(False)
                self.choix4.setVisible(False)
            case 2:
                self.choix1.setText(_translate("MainWindow", str(tabChapitreSuivant[0])))
                self.choix2.setText(_translate("MainWindow", str(tabChapitreSuivant[1])))
                self.choix3.setVisible(False)
                self.choix4.setVisible(False)
            case 3:
                self.choix1.setText(_translate("MainWindow", str(tabChapitreSuivant[0])))
                self.choix2.setText(_translate("MainWindow", str(tabChapitreSuivant[1])))
                self.choix3.setText(_translate("MainWindow", str(tabChapitreSuivant[2])))
                self.choix4.setVisible(False)
            case 4:
                self.choix1.setText(_translate("MainWindow", str(tabChapitreSuivant[0])))
                self.choix2.setText(_translate("MainWindow", str(tabChapitreSuivant[1])))
                self.choix3.setText(_translate("MainWindow", str(tabChapitreSuivant[2])))
                self.choix4.setText(_translate("MainWindow", str(tabChapitreSuivant[3])))

        if tailleTab == 0:
            print("fin du game")
        if self.choix1.isChecked():
            self.chapitre = tabChapitreSuivant[0]
            recupererTexteChapitreActuel(self.chapitre)
        if self.choix2.isChecked():
            self.chapitre = tabChapitreSuivant[1]
            recupererTexteChapitreActuel(self.chapitre)
        if self.choix3.isChecked():
            self.chapitre = tabChapitreSuivant[2]
            recupererTexteChapitreActuel(self.chapitre)
        if self.choix4.isChecked():
            self.chapitre = tabChapitreSuivant[3]
            recupererTexteChapitreActuel(self.chapitre)


    def commencer(self):
        _translate = QtCore.QCoreApplication.translate
        nomJoueur = self.lineEdit_NomPerso.text()
        habiliteJoueur = self.spinBox_Habilite.text()
        enduranceJoueur = self.spinBox_Endurance.text()

        self.label_joueurActuel.setText(_translate("MainWindow", str(nomJoueur)))
        self.label_habiliteActuel.setText(_translate("MainWindow", str(habiliteJoueur)))
        self.label_enduranceActuel.setText(_translate("MainWindow", str(enduranceJoueur)))

        tabChapitreSuivant = recupererChapitreSuivant(1)
        texte = recupererTexteChapitreActuel(1)
        self.textChapitre.setText(texte)
        self.choix1.setText(_translate("MainWindow", str(tabChapitreSuivant[0])))
        self.choix2.setText(_translate("MainWindow", str(tabChapitreSuivant[1])))
        self.choix3.setText(_translate("MainWindow", str(tabChapitreSuivant[2])))
        self.choix4.setVisible(False)
        

    def sauvegarder(self):
        _translate = QtCore.QCoreApplication.translate
        nomJoueur = self.label_joueurActuel.text()
        habiliteJoueur = self.label_habiliteActuel.text()
        enduranceJoueur = self.label_enduranceActuel.text()
        bourseActuelle = self.spinBox_bourse.text()
        mycursor.execute("INSERT INTO feuille_aventure (nom_joueur, habilite, endurance, bourse) VALUES (%s, %s, %s, %s)", (nomJoueur, habiliteJoueur , enduranceJoueur , bourseActuelle))
        mydb.commit()
        self.chargerPartie()
        self.label_info.setText(_translate("MainWindow", "La partie a bien été sauvegardée"))

    def supprimer(self):
        _translate = QtCore.QCoreApplication.translate
        joueur = self.comboBox_ChargerPartie.currentText()
        mycursor.execute("DELETE FROM feuille_aventure WHERE nom_joueur ='" + joueur + "'")
        mydb.commit()
        self.chargerPartie()
        self.label_info.setText(_translate("MainWindow", "La partie a bien été supprimée"))
    
    def chargerPartie(self):
        _translate = QtCore.QCoreApplication.translate
        mycursor.execute("SELECT nom_joueur FROM feuille_aventure")
        requeteTabNomJoueur = mycursor.fetchall()
        tabNomJoueur = list(sum(requeteTabNomJoueur, ()))
        c = 0
        for nom in tabNomJoueur:
            self.comboBox_ChargerPartie.setItemText(c, _translate("MainWindow", tabNomJoueur[c]))
            c = c + 1 


    #def recupererDonneKai(self):
        

    #def recupererDonneArmes(self):
        



app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()