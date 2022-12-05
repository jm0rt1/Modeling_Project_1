from src.gui.models.model import Model
from src.gui.models.team_list_model import TeamListModel
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
        self.model = Model()

    def __initialize(self):
        # connect signals/slots
        self.display_button.clicked.connect(self.clicked_display_button)
        self.team_combobox.currentIndexChanged.connect(self.team_selected)
        # connect models
        self.team_combobox.setModel(TeamListModel())

    def run(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        self.setupUi(window)  # type:ignore
        window.show()
        self.__initialize()
        app.exec_()

    def clicked_display_button(self):
        pass

    def team_selected(self, index: int):
        year = int(self.year_line_edit.text())
        name = self.team_combobox.currentText()
        self.model.load_data_from_snoozle_server(year, name)
