import sys

import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from mainui import Ui_MainWindow


class COFFE(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect("coffee.sqlite")
        self.cur = self.conn.cursor()
        self.init_ui()

    def init_ui(self):
        data = self.cur.execute("""SELECT * FROM Coffee""").fetchall()

        self.CoffeeTable.setRowCount(len(data))
        self.CoffeeTable.setColumnCount(len(data[0]))
        self.CoffeeTable.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'тип', 'описание', 'цена', 'объем упаковки'])

        for i, lis in enumerate(data):
            for j, item in enumerate(lis):
                dat = str(item)
                if j == 1:
                    dat = self.cur.execute(f"""SELECT sort FROM sorts
WHERE id = {lis[1]}""").fetchall()[0][0]
                elif j == 2:
                    dat = self.cur.execute(f"""SELECT name FROM degree
WHERE id = {lis[2]}""").fetchall()[0][0]
                elif j == 3:
                    dat = self.cur.execute(f"""SELECT name FROM types
WHERE id = {lis[3]}""").fetchall()[0][0]

                item_widget = QTableWidgetItem(dat)
                self.CoffeeTable.setItem(i, j, item_widget)


if __name__ == "__main__":
    print("""\x1b[31m=================================================\x1b[0m
\x1b[32mThis program was created with \x1b[0m\x1b[31m♡\x1b[0m\x1b[32m by \x1b[0m\x1b[34mFlamesC0der\x1b[0m

https://github.com/FlamesC0der\x1b[0m
\x1b[31m=================================================\x1b[0m""")
    app = QApplication(sys.argv)
    ex = COFFE()
    ex.show()
    sys.exit(app.exec())
