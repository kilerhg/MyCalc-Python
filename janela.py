from interface import *
from funcoes import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def main(ui):
    ui.txt1.setValidator(QDoubleValidator(0.99,99.99,2))
    ui.txt2.setValidator(QDoubleValidator(0.99,99.99,2))

    def func_somar():
        n1 = ui.txt1.text()
        n2 = ui.txt2.text()
        if verifica_numero(n1) == True and verifica_numero(n2) == True:
            n1 = br_to_us(n1)
            n2 = br_to_us(n2)
            n1 = float(n1)
            n2 = float(n2)
            resultado = soma(n1,n2)
            ui.txt_resultado.setText(resultado)
        else:
            ui.txt_resultado.setText('Digite Dois Numeros Corretamente')

    ui.botao.clicked.connect(func_somar)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())