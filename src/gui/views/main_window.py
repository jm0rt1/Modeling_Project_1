from src.gui.models.model import Model
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
        self.display_button.clicked.connect(  # type:ignore
            self.clicked_display_button)
        self.team_combobox.currentIndexChanged.connect(  # type:ignore
            self.team_selected)
        self.year_line_edit.textEdited.connect(  # type:ignore
            self.year_line_edit_changed)
        # connect models
        self.team_combobox.setModel(self.model.team_list_model)  # type:ignore
        self.game_number_combobox.setModel(  # type:ignore
            self.model.games_combobox_model)
        self.display_table.setModel(self.model.displayed_game)  # type:ignore

    def year_line_edit_changed(self, text: str):
        if text.isdigit() and len(text) == 4:
            try:
                _ = int(text)
            except:
                return
            self.team_selected()  # type:ignore

    def run(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        self.setupUi(window)  # type:ignore
        window.show()
        self.__initialize()
        app.exec_()

    def clicked_display_button(self):
        self.model.displayed_game.clear()
        self.model.displayed_game.populate(
            self.model.games[self.game_number_combobox.currentIndex()])

    def team_selected(self):
        if self.year_line_edit.text().isdigit() and len(self.year_line_edit.text()) == 4:
            year = int(self.year_line_edit.text())
            name = self.team_combobox.currentText()
            self.model.load_data_from_snoozle_server(year, name)
