import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
from PyQt5.QtCore import QUrl


#QMainWindow that support a menu bar, toolbars, and status bar out of the box
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Setting the window size
        self.setMinimumSize(QSize(420, 140))    
        self.setWindowTitle("PyQt HTML to PDF Convertor") 
        
        #setting the input box
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Enter Path:')
        self.line = QLineEdit(self)

        #setting the dimension and placement of input box
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        #setting the convert button
        pybutton = QPushButton('Convert', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

#Method initiated when convert button is clicked
    def clickMethod(self):
        loader = QtWebEngineWidgets.QWebEngineView()
        loader.setZoomFactor(1)
        loader.page().pdfPrintingFinished.connect(lambda *args: print('finished:', args))
        loader.load(QtCore.QUrl(self.line.text()))

        def emit_pdf(finished):
            loader.show()
            loader.page().printToPdf("test.pdf")
            mbox = QMessageBox()

            mbox.setText("Your HTML has been converted to PDF file")
            mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mbox.exec_()

        loader.loadFinished.connect(emit_pdf)


if __name__ == '__main__':
# You need one (and only one) QApplication instance to create an application object.
# Pass in sys.argv to allow command line arguments for your app.
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()

#sys.exit() method ensures that the main loop is safely exited
    sys.exit(app.exec_())

