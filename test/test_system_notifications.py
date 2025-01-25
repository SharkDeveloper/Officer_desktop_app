import time
from win11toast import toast  # Уведомление для Windows 11
from plyer import notification  # Кросс-платформенные уведомления
from win10toast import ToastNotifier  # Уведомления для Windows 10/11
import win32api  # Уведомления через win32api
import win32con  # Для win32api

# Уведомление через win11toast (для Windows 11)
def notify_win11toast():
    print("Тест уведомления через win11toast...")
    toast('Hello Python🐍', "Уведомление через win11toast")
    time.sleep(2)

# Уведомление через plyer (кросс-платформенное)
def notify_plyer():
    print("Тест уведомления через plyer...")

    time.sleep(2)

# Уведомление через win10toast (для Windows 10/11)
def notify_win10toast():
    print("Тест уведомления через win10toast...")
    toaster = ToastNotifier()
    toaster.show_toast("Уведомление через win10toast", "Это тестовое уведомление", duration=10)
    time.sleep(2)

# Уведомление через win32api (старый способ)
def notify_win32api():
    print("Тест уведомления через win32api...")
    message = "Это уведомление через win32api"
    title = "Уведомление win32api"
    win32api.MessageBox(0, message, title, win32con.MB_OK)
    time.sleep(2)

def test_notifications():
    print("Запуск теста уведомлений...\n")

    # Проверка через win11toast
    notify_win11toast()

    # Проверка через plyer
    notify_plyer()

    # Проверка через win10toast
    notify_win10toast()

    # Проверка через win32api
    notify_win32api()

    print("Тест завершен. Если вы увидели уведомления, значит метод работает.")

if __name__ == "__main__":
    test_notifications()
