# -*- coding: utf-8 -*-

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate
from .task_page import TaskDetailsPage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Stack widget for navigation between pages
        self.stackWidget = QStackedWidget(self.centralwidget)
        self.stackWidget.setObjectName(u"stackWidget")
        self.stackWidget.setGeometry(QRect(0, 0, 800, 600))

        # First page - Important tasks
        self.pageTasks = QWidget(self.stackWidget)
        self.pageTasks.setObjectName(u"pageTasks")

        # Table for tasks
        self.tableWidget = QTableWidget(self.pageTasks)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 50, 700, 400))

        # Set up the table
        self.tableWidget.setColumnCount(4)  # Title, Deadline, Status, Description
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Дата выполнения", "Статус", "Описание"])

        # Buttons
        self.addButton = QPushButton(self.pageTasks)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(50, 470, 150, 30))
        self.addButton.setText(u"Добавить задачу")

        self.refreshButton = QPushButton(self.pageTasks)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(600, 470, 150, 30))
        self.refreshButton.setText(u"Обновить список задач")

        # Second page - Task details (Imported from the other file)
        self.pageTaskDetails = TaskDetailsPage(self.stackWidget, self)
        
        # Add pages to the stack widget
        self.stackWidget.addWidget(self.pageTasks)
        self.stackWidget.addWidget(self.pageTaskDetails)

        # Initial page set to Task list
        self.stackWidget.setCurrentIndex(0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Officer Scheduler ", None))

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

    def displayTaskDetails(self, task):
        """ Display task details in the second page. """
        self.pageTaskDetails.displayTaskDetails(task)
        self.stackWidget.setCurrentIndex(1)

    def addTaskButtonClicked(self):
        """ Handle the Add Task button click event. """
        pass  # Add task functionality

    def refreshButtonClicked(self):
        """ Handle the Refresh button click event. """
        pass  # Refresh task list functionality

    def updateTask(self, task):
        """ Update the task status in the task list (main page). """
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0).text() == task['title']:
                status_item = QTableWidgetItem(task['status'])
                self.tableWidget.setItem(row, 2, status_item)
                
                # Update row color based on new status
                if task['status'] == 'completed':
                    self.tableWidget.item(row, 1).setBackground(QColor(0, 255, 0))  # Green for completed
                else:
                    self.tableWidget.item(row, 1).setBackground(QColor(255, 255, 0))  # Yellow for near future
                break