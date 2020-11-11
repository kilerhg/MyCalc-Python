from interface import *
from funcoes import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import keyboard

def main(ui):
    from time import sleep

    def func_global(ope='+'):
        global operador
        operador = ope
        receber_numero()

    def func_resultado(resultado):
        resultado = str(resultado)
        if resultado == '-0':
            resultado == '0'
        ui.txt_resultado.setText(resultado)

    def func_somar():
        func_global('+')

    def func_subtrair():
        func_global('-')

    def func_multiplicar():
        func_global('*')

    def func_dividir():
        func_global('/')

    def func_inverte():
        func_global('*-1')

    def func_potencia2():
        func_global('x^2')

    def func_raiz2():
        func_global('x^0.5')

    def func_div1():
        func_global('1/x')

    def func_porcentagem():
        func_global('%')


    def func_limpar():
        global num1
        global num2
        global operador
        operador = ''
        num1 = num2 = 0
        ui.txt_old.clear()

    def receber_numero():
        global num1
        global operador
        # 1 num1 = ui.txt1.text()
        num1 = ui.txt_resultado.text()
        # 1 ui.txt1.clear()
        ui.txt_resultado.clear()
        ui.txt_old.setText(f'{num1[0:5]: >5} {operador}')

    def func_enviar():
        global operador
        global num1
        # 1 num2 = ui.txt1.text()
        num2 = ui.txt_resultado.text()
        num1,num2 = receber_valores(ui,num1,num2)
        resultado = calculo(num1,num2,operador)
        func_resultado(resultado)
        num1 = formatar_saida(num1)
        num2 = formatar_saida(num2)
        ui.txt_old.setText(f'{num2[0:5]: >5} {operador} {num1[0:5]} =')
        # 1 ui.txt1.setText(ui.txt_resultado.text())

    # Teclado Numerico
    def conca_virgula():
        valor = str(ui.txt_resultado.text())
        if valor.count(',') == 0:
            conca(',')

    def conca_0():
        conca(0)

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
        # ui.txt1.setText(str(ui.txt1.text())+f'{valor}')
        v1 = str(ui.txt_resultado.text())
        if v1 == '0' or v1 == '-0':
            ui.txt_resultado.clear()
        ui.txt_resultado.setText(str(ui.txt_resultado.text()) + f'{valor}')
    # Filtros de entrada nas Caixas de texto
    # ui.txt1.setValidator(QDoubleValidator(0.99,99.99,2))
    ui.txt_resultado.setValidator(QDoubleValidator(0.99,99.99,2))
    # caso apertar Enter
    # ui.txt1.editingFinished.connect(teste)

    # Clicar nos Botões

    # Operações Aritmeticas

    ui.botao_somar.clicked.connect(func_somar)
    ui.botao_subtrair.clicked.connect(func_subtrair)
    ui.botao_multiplicar.clicked.connect(func_multiplicar)
    ui.botao_dividir.clicked.connect(func_dividir)
    ui.botao_potencia_quadrado.clicked.connect(func_potencia2)
    ui.botao_raiz_quadrada.clicked.connect(func_raiz2)

    # Outros

    ui.botao_enviar.clicked.connect(func_enviar)
    ui.botao_virgula.clicked.connect(conca_virgula)
    ui.botao_inverte_sinal.clicked.connect(func_inverte)
    ui.botao_1x.clicked.connect(func_div1)
    ui.botao_porcentagem.clicked.connect(func_porcentagem)
    ui.botao_limpar.clicked.connect(func_limpar)


    # Teclado Numerico
    ui.botao_0.clicked.connect(conca_0)
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

    ui.botao_0.setShortcut('0')
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
    ui.botao_17.setShortcut('delete')
    ui.botao_limpar.setShortcut('backspace')
    ui.botao_virgula.setShortcut(',')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.txt_old.setText(' '*9)
    ui.centralwidget.setFocus()
    main(ui)
    sys.exit(app.exec_())