# Task "Потоковая запись в файлы"

import time
import threading

def duration(func):
    def wrapper(*args, **kwargs):
        started_at = time.time()
        func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Время рабты потоков {elapsed} секунд')
    return wrapper


def wite_words(word_count, file_name):
    x = "У попа была собака..."
    num = 1
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'{x} # {num} \n')
            num += 1
            time.sleep(0.01)
    print(f'Завершилась запись в файл {file_name}')

@duration
def main_flow():
    wite_words(10, 'example1.txt')
    wite_words(30, 'example2.txt')
    wite_words(200, 'example3.txt')
    wite_words(100, 'example4.txt')

@duration
def other_flows():
    thread1 = threading.Thread(target= wite_words(10, 'example5.txt'))
    thread2 = threading.Thread(target= wite_words(30, 'example6.txt'))
    thread3 = threading.Thread(target= wite_words(200, 'example7.txt'))
    thread4 = threading.Thread(target= wite_words(100, 'example8.txt'))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


main_flow()
other_flows()


