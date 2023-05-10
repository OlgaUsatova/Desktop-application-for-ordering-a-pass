import sys
import traceback as tb
from interface.primary_window import PrimaryWindow
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets


# Обработчик ошибок
error_dialog = None
def exception_hook(exctype, value, traceback):
    tb.print_exception(exctype, value, traceback)  # вывод ошибки в консоль

    global error_dialog
    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.showMessage(f"Произошла ошибка: {str(value)}")  # вывод сообщения с ошибкой


sys.excepthook = exception_hook  # замена системного excepthook на свой


# ВЫЗОВ СКРИПТА ТОЛЬКО В ЭТОМ ФАЙЛЕ
if __name__ == "__main__":
    app = QApplication([])
    window = PrimaryWindow()
    window.show()
    sys.exit(app.exec())