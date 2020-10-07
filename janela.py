from interface import *
from funcoes import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import keyboard


def main(ui):

    def foco_txt():
        ui.txt.setFocus()
        print('a')

    def foco_operador():
        ui.centralwidget.setFocus()
        print('b')

    def func_global(ope='+'):
        global operador
        operador = ope
        receber_numero()
        ui.txt1.setFocus()

    def func_resultado(resultado):
        resultado = str(resultado)
        ui.txt_resultado.setText(resultado)

    def func_somar():
        func_global('+')

    def func_subtrair():
        func_global('-')

    def func_multiplicar():
        func_global('*')

    def func_dividir():
        func_global('/')

    def receber_numero():
        global num1
        global operador
        num1 = ui.txt1.text()
        ui.txt1.clear()
        ui.txt_old.setText(f'{num1[0:5]: >5} {operador}')

    def func_enviar():
        global operador
        global num1
        num2 = ui.txt1.text()
        num1,num2 = receber_valores(ui,num1,num2)
        resultado = calculo(num1,num2,operador)
        func_resultado(resultado)
        num1 = formatar_saida(num1)
        num2 = formatar_saida(num2)
        ui.txt_old.setText(f'{num2[0:5]: >5} {operador} {num1[0:5]} =')
        ui.txt1.setText(ui.txt_resultado.text())

    # Teclado Numerico
    def conca_1():
        conca(1)

    def conca_2():
        conca(2)

    def conca_3():
        conca(3)

    def conca_4():
        conca(4)

    def conca_5():
        conca(5)

    def conca_6():
        conca(6)

    def conca_7():
        conca(7)

    def conca_8():
        conca(8)

    def conca_9():
        conca(9)

    def conca(valor):
        ui.txt1.setText(str(ui.txt1.text())+f'{valor}')

    # Filtros de entrada nas Caixas de texto
    ui.txt1.setValidator(QDoubleValidator(0.99,99.99,2))

    # caso apertar Enter
    # ui.txt1.editingFinished.connect(teste)
    ui.txt1.returnPressed.connect(foco_txt)

    # Clicar nos Botões
    ui.botao_somar.clicked.connect(func_somar)
    ui.botao_subtrair.clicked.connect(func_subtrair)
    ui.botao_multiplicar.clicked.connect(func_multiplicar)
    ui.botao_dividir.clicked.connect(func_dividir)
    ui.botao_enviar.clicked.connect(func_enviar)

    # Teclado Numerico
    ui.botao_1.clicked.connect(conca_1)
    ui.botao_2.clicked.connect(conca_2)
    ui.botao_3.clicked.connect(conca_3)
    ui.botao_4.clicked.connect(conca_4)
    ui.botao_5.clicked.connect(conca_5)
    ui.botao_6.clicked.connect(conca_6)
    ui.botao_7.clicked.connect(conca_7)
    ui.botao_8.clicked.connect(conca_8)
    ui.botao_9.clicked.connect(conca_9)

    # Atalho Teclado Numerico

    ui.botao_1.setShortcut('1')
    ui.botao_2.setShortcut('2')
    ui.botao_3.setShortcut('3')
    ui.botao_4.setShortcut('4')
    ui.botao_5.setShortcut('5')
    ui.botao_6.setShortcut('6')
    ui.botao_7.setShortcut('7')
    ui.botao_8.setShortcut('8')
    ui.botao_9.setShortcut('9')

    # Atalhos
    ui.botao_somar.setShortcut('+')
    ui.botao_subtrair.setShortcut('-')
    ui.botao_dividir.setShortcut('/')
    ui.botao_multiplicar.setShortcut('*')
    ui.botao_enviar.setShortcut('enter')
    ui.botao_limpar.setShortcut('delete')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.txt_old.setText(' '*9)
    ui.txt1.setFocus()
    main(ui)
    sys.exit(app.exec_())