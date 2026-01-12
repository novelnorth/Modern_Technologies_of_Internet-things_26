import time
import os
from datetime import datetime
from config import *

def read_sensor():
    """Читает значение уровня масляных паров из файла"""
    if not os.path.exists(SENSOR_FILE):
        return 0
    with open(SENSOR_FILE, 'r') as f:
        try:
            level = int(f.read().strip())
            return level
        except ValueError:
            return 0

def write_sensor(value):
    """Записывает значение уровня в файл (эмуляция датчика)"""
    with open(SENSOR_FILE, 'w') as f:
        f.write(str(value))

def write_timestamp():
    """Записывает текущее время в файл"""
    with open(TIMESTAMP_FILE, 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def log_alert(level):
    """Записывает уведомление в лог-файл"""
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now()}] Критический уровень загрязнения: {level}%\n")

def check_and_alert():
    """Проверяет уровень загрязнения и отправляет уведомление при необходимости"""
    level = read_sensor()
    if level >= CRITICAL_LEVEL:
        print(f"❌ КРИТИЧЕСКИЙ УРОВЕНЬ: {level}%")
        log_alert(level)
    elif level >= WARNING_LEVEL:
        print(f"⚠️  ПРЕДУПРЕЖДЕНИЕ: {level}%")
    else:
        print(f"✅ Уровень нормальный: {level}%")

def simulate_sensor():
    """Имитация работы датчика — генерирует случайное значение"""
    import random
    current_level = read_sensor()
    new_level = max(0, min(100, current_level + random.randint(-5, 10)))
    write_sensor(new_level)
    write_timestamp()
    return new_level

def main():
    print("Запуск системы мониторинга загрязнения масляными парами...")
    while True:
        level = simulate_sensor()
        check_and_alert()
        time.sleep(5)  # Проверка каждые 5 секунд

if __name__ == "__main__":
    main()
