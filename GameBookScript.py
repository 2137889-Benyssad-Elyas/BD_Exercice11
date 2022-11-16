import sys
import mysql.connector  

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Exercice11_LDVELH"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT texte FROM chapitre WHERE id = 1")
requete = mycursor.fetchall()

from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier MainWindow.py
from MonGameBookV2 import Ui_MainWindow

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit
        self.boutonContinuer.clicked.connect(self.continuer)

    # On défini la fonction qu'on avait déclaré pour le clique sur le bouton
    def continuer(self):
        
        if self.choix1.isChecked():
            self.textChapitre.setText(requete[0][0])
        if self.choix2.isChecked():
           self.textChapitre.setText('choix2')
        if self.choix3.isChecked():
           self.textChapitre.setText('choix3')

        


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()