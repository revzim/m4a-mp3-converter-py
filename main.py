import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout

# IMPORT CONVERTER CLASS FROM conv.py
from conv import Converter

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("M4A to MP3")
        self.layout = QVBoxLayout()
        self.setAcceptDrops(True)
        self.converter = Converter()
        self.labelText = "Drag And Drop A Sound Byte File To Convert!"
        self.label = QLabel(self.labelText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self.resize(400, 400)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            full_file_path = url.toLocalFile()
            print("Converting: {}".format(full_file_path))
            self.labelText = "{0}\nConverting: {1}....".format(self.labelText, full_file_path)
            self.label.setText(self.labelText)
            # CONVERT
            self.converter.convertToMP3(full_file_path)
            self.labelText = "Converted {0}.{1} successfully.".format(self.converter.file_name, self.converter.output_type)
            self.label.setText(self.labelText)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
