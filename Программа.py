import numpy as np
from PyQt5 import QtWidgets
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from zadanie import Ui_MainWindow
import sys


class plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(plot, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.verticalLayout.addWidget(self.canvas)


    def btnClicked(self):
        try:
            self.figure.clear()
            fnc = self.ui.lineEdit.text()
            x_ot = float(self.ui.ot.text())
            x_do = float(self.ui.do_2.text())
            n = max(100, 10 * (x_do - x_ot))
            range_x = np.linspace(x_ot, x_do, n)
            fnc = fnc.replace('**', '**')
            y = eval(fnc, {'x': range_x, 'sin': np.sin, 'cos': np.cos,
                           'tan': np.tan, 'sqrt': np.sqrt,
                           'log': np.log, 'exp': np.exp, 'pi': np.pi})
            ax = self.figure.add_subplot(111)
            ax.plot(range_x, y)
            ax.grid(True)
            self.canvas.draw()

        except ValueError as s:
            QtWidgets.QMessageBox.critical(self, "Ошибка!",
                                           f"Некорректные данные {str(s)}")

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = plot()
    window.show()
    sys.exit(app.exec_())