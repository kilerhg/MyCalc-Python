from interface import *
from funcoes import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def main(ui):

    def teste():
        print('TESTE')

    def func_resultado(resultado):
        resultado = str(resultado)
        ui.txt_resultado.setText(resultado)

    def func_somar():
        n1,n2 = receber_valores(ui)
        resultado = soma(n1,n2)
        func_resultado(resultado)

    def func_subtrair():
        n1,n2 = receber_valores(ui)
        resultado = subtrair(n1,n2)
        func_resultado(resultado)


    def func_multiplicar():
        n1,n2 = receber_valores(ui)
        resultado = multiplicar(n1,n2)
        func_resultado(resultado)

    def func_dividir():
        n1,n2 = receber_valores(ui)
        resultado = dividir(n1,n2)
        func_resultado(resultado)

    ui.centralwidget.returnPressed.connect(teste)
    ui.txt1.setValidator(QDoubleValidator(0.99,99.99,2))
    ui.txt2.setValidator(QDoubleValidator(0.99,99.99,2))

    ui.botao_somar.clicked.connect(func_somar)
    ui.botao_subtrair.clicked.connect(func_subtrair)
    ui.botao_multiplicar.clicked.connect(func_multiplicar)
    ui.botao_dividir.clicked.connect(func_dividir)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())