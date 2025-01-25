from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton

class TaskDetailsPage(QWidget):
    def __init__(self, stackWidget, parent=None):
        super().__init__(parent)
        
        self.stackWidget = stackWidget  # Сохраняем переданный объект stackWidget
        self.mainWindow = parent  # Ссылаемся на родительское окно (MainWindow)

        # Layout and labels
        self.setObjectName("pageTaskDetails")

        self.titleLabel = QLabel(self)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setGeometry(QRect(50, 50, 700, 30))

        self.descriptionLabel = QLabel(self)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(50, 100, 700, 30))

        self.materialsLabel = QLabel(self)
        self.materialsLabel.setObjectName("materialsLabel")
        self.materialsLabel.setGeometry(QRect(50, 150, 700, 30))

        # Placeholder for task materials (could be text, images, or tables)
        self.materialsText = QTextEdit(self)
        self.materialsText.setObjectName("materialsText")
        self.materialsText.setGeometry(QRect(50, 180, 700, 300))

        self.backButton = QPushButton(self)
        self.backButton.setObjectName("backButton")
        self.backButton.setGeometry(QRect(600, 500, 150, 30))
        self.backButton.setText("Назад")
        self.backButton.clicked.connect(self.backButtonClicked)

        self.completeButton = QPushButton(self)
        self.completeButton.setObjectName("completeButton")
        self.completeButton.setGeometry(QRect(450, 500, 150, 30))
        self.completeButton.setText("Выполнено")
        self.completeButton.clicked.connect(self.completeButtonClicked)

    def displayTaskDetails(self, task):
        """ Display task details in the second page. """
        self.task = task  # Сохраняем задачу для дальнейшей работы
        self.titleLabel.setText(f"Задача: {task['title']}")
        self.descriptionLabel.setText(f"Описание: {task['description']}")
        self.materialsLabel.setText("Материалы для задачи:")
        self.materialsText.setText(task['materials'])

    def completeButtonClicked(self):
        """ Mark task as completed and update status. """
        self.task['status'] = 'Выполнено'  # Обновляем статус задачи на 'Выполнено'

        # Вызываем метод, чтобы обновить отображение на главной странице
        self.updateTaskInMainPage()

        # Переключаемся обратно на главную страницу
        self.stackWidget.setCurrentIndex(0)

    def updateTaskInMainPage(self):
        """ Update the task in the main page to reflect the completed status. """
        # Переходим к странице задач и обновляем состояние задачи в списке
        if self.mainWindow:  # Проверяем, что mainWindow существует
            # Обновляем таблицу задач с измененной задачей
            self.mainWindow.updateTaskTable([self.task])

    def backButtonClicked(self):
        """ Switch back to the tasks list page. """
        self.stackWidget.setCurrentIndex(0)
