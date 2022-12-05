from src.gui.views.generated.main_window import Ui_MainWindow
# Only needed for access to command line arguments
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.


class MainWindow(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        self.setupUi(window)  # type:ignore
        window.show()
        app.exec_()
