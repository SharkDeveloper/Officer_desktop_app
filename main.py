import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QDate
from PySide6.QtGui import QColor
from plyer import notification

from ui.main_page import Ui_MainWindow  
from src.db.setup import initialize_database


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Пример задач
        tasks = [
            {
                'title': 'Сделать отчет',
                'deadline': QDate(2025, 1, 30),
                'status': 'Ожидают выполнения',
                'description': 'Необходимо сделать отчет о проделанной работе.',
                'materials': 'Пример отчета, ссылка на документацию.'
            },
            {
                'title': 'Подготовить презентацию',
                'deadline': QDate(2025, 1, 25),
                'status': 'Запланированные',
                'description': 'Подготовить презентацию для встречи.',
                'materials': 'Тема: "Будущее технологий". Использовать слайды из библиотеки.'
            },
        ]

        # Обновление таблицы задач
        self.updateTaskTable(tasks)

        # Пример перехода на страницу с деталями задачи
        self.tableWidget.cellDoubleClicked.connect(lambda row, column: self.displayTaskDetails(tasks[row]))

        # Обработчики событий
        self.addButton.clicked.connect(self.addTaskButtonClicked)
        self.refreshButton.clicked.connect(self.refreshButtonClicked)
        
        self.show_system_notification("Title","Hello World!")


    def updateTaskTable(self, tasks):
        """ Update the task table with tasks. Tasks is a list of dictionaries. """
        self.tableWidget.setRowCount(len(tasks))
        for row, task in enumerate(tasks):
            title_item = QTableWidgetItem(task['title'])
            deadline_item = QTableWidgetItem(task['deadline'].toString('yyyy-MM-dd'))
            status_item = QTableWidgetItem(task['status'])
            description_item = QTableWidgetItem(task['description'])

            self.tableWidget.setItem(row, 0, title_item)
            self.tableWidget.setItem(row, 1, deadline_item)
            self.tableWidget.setItem(row, 2, status_item)
            self.tableWidget.setItem(row, 3, description_item)

            # Apply row color based on deadline
            if task['deadline'] < QDate.currentDate():  # Past date - red
                self.tableWidget.item(row, 1).setBackground(QColor(255, 0, 0))
            elif task['deadline'] < QDate.currentDate().addDays(2):  # Near future - yellow
                self.tableWidget.item(row, 1).setBackground(QColor(255, 255, 0))

    def show_system_notification(self, title, message):
        """Display a system notification in Windows."""
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="Officer Desktop App",
                timeout=10  # seconds
            )
        except Exception as e:
            print(f"Error showing notification: {e}")


if __name__ == "__main__":
    initialize_database()
    app = QApplication(sys.argv)
    with open("./static/styles.qss", "r") as style_file:
        app.setStyleSheet(style_file.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
