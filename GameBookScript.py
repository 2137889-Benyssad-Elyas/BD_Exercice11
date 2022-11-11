import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier MainWindow.py
from MonGameBook import Ui_MainWindow

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
        cocher = True
        if self.choix1.isChecked == cocher:
            self.textChapitre.setText('choix1')
        if self.choix2:
            self.textChapitre.setText('choix2')
        if self.choix3:
            self.textChapitre.setText('choix3')

        


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()