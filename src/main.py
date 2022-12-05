from src.gui.views.main_window import MainWindow
import logging


def main():
    try:
        mw = MainWindow()
        mw.run()
    except Exception as e:
        logging.exception(e)
