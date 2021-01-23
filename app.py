import sys
import numpy as np

from PySide2 import QtWidgets
from PySide2.QtGui import QFont

from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.setWindowTitle("Function Plotter")
        self.layout = QtWidgets.QGridLayout(self._main)

        # Create Labels and Textboxs
        self.label1 = QtWidgets.QLabel(self._main)
        self.label1.setText("Enter the function equation:")
        self.label1.setFont(QFont('Arial', 13)) 

        self.textBox1 = QtWidgets.QLineEdit(self._main)        
        self.textBox1.setFont(QFont('Arial', 13)) 
        self.textBox1.setToolTip("Equation must be function of x varible. The operators supported are: + - / * ^.")
        # self.textBox1.editingFinished.connect(self.checkTextBox1Status)

        self.label2 = QtWidgets.QLabel(self._main)
        self.label2.setText("Enter the minimum value:")
        self.label2.setFont(QFont('Arial', 13)) 

        self.textBox2 = QtWidgets.QLineEdit(self._main)        
        self.textBox2.setFont(QFont('Arial', 13))
        # self.textBox2.editingFinished.connect(self.checkTextBox2Status)

        self.label3 = QtWidgets.QLabel(self._main)
        self.label3.setText("Enter the maximum value:")
        self.label3.setFont(QFont('Arial', 13)) 

        self.textBox3 = QtWidgets.QLineEdit(self._main)        
        self.textBox3.setFont(QFont('Arial', 13))
        # self.textBox3.editingFinished.connect(self.checkTextBox3Status)

        # Create button
        self.button = QtWidgets.QPushButton('Plot', self._main)
        self.button.setFont(QFont('Arial', 13))
        self.button.setToolTip('Press to plot')
        self.button.clicked.connect(self.on_click)
        
        # Create MessageBox for errors
        self.mbox = QtWidgets.QMessageBox()

        # Create Figure    
        self.static_canvas = FigureCanvas(Figure(figsize=(8, 5)))
        # self.addToolBar(NavigationToolbar(self.static_canvas, self))

        # Add Widgets
        self.layout.addWidget( self.label1, 0, 0)
        self.layout.addWidget( self.textBox1, 0, 1)
        self.layout.addWidget( self.label2, 1,0)
        self.layout.addWidget( self.textBox2, 1,1)
        self.layout.addWidget( self.label3, 2,0)
        self.layout.addWidget( self.textBox3, 2,1)
        self.layout.addWidget( self.button, 3,0,1,0)
        self.layout.addWidget( self.static_canvas, 4,0,1,0)

    def dialog(self, msg):
        self.mbox = QtWidgets.QMessageBox()
        self.mbox.setText(msg)
        self.mbox.setWindowTitle("Error")
        self.mbox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.mbox.exec_()

    def checkTextBox1Status(self):
        status = True
        if self.textBox1.text() == "":
            self.dialog("Enter the function equation")
            self.textBox1.setFocus()
            status = False
        else:
            for i in self.textBox1.text():
                if i.isdigit() or i==' ' or i == 'x' or i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
                    continue
                self.dialog("Equation must be function of x varible. And the supported operators are: + - / * ^.")
                self.textBox1.setFocus()
                status = False
                break
        return status


    def checkTextBox2Status(self):
        s = True
        if self.textBox2.text() == "":
            self.dialog("Enter the minimum value")
            self.textBox2.setFocus()
            s = False
        else:
            try:
                float(self.textBox2.text())
            except:
                self.dialog("The minimum value have to be a number")
                self.textBox2.setFocus()
                s = False
        return s

    def checkTextBox3Status(self):
        s = True
        if self.textBox3.text() == "":
            self.dialog("Enter the maximum value")
            self.textBox3.setFocus()
            s = False
        else:
            try:
                float(self.textBox3.text())
            except:
                self.dialog("The maximum value have to be a number")
                self.textBox3.setFocus()
                s = False
        return s

    def calEquation(self, equation, x):
        return eval(equation, {'x': x})

    def on_click(self):
        if self.checkTextBox1Status() and self.checkTextBox2Status() and self.checkTextBox3Status():
            equation = self.textBox1.text()
            equation = equation.replace('^', '**')

            intial = float(self.textBox2.text())
            end = float(self.textBox3.text())
            t = np.arange(intial, end, 0.1)
            
            self.static_canvas = FigureCanvas(Figure(figsize=(8, 5)))
            self.layout.addWidget( self.static_canvas, 4,0,1,0)

            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.set(title="Function Plotting", xlabel=r'$x$', ylabel=r'$f(x)$')
            self._static_ax.plot(t, self.calEquation(equation, t), ".")


if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()