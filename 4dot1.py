import re

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            total = 0
            count = 0

            for line in fh:
                match = re.findall(r'\d+', line)
                if match:
                    try:
                        total += float(match[0])
                        count += 1
                    except ValueError:
                        print(f"Неможливо створити число: {match[0]}")

        average = total / count if count > 0 else 0
        return total, average

    except FileNotFoundError:
        print(f"Файл не знайден: {path}")
        return 0, 0
    except IOError:
        print("Помилка при роботі з файлом")
        return 0, 0
    



total, average = total_salary("E:\\Git\\PROJECTS\\4dz\\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
