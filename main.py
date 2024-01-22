import os
import shutil
from pathlib import Path
from unionjrnfiles import unionjrn
from createlogfiles import createlog,filesx
from  obrlogfiles import  obrlog

BASE_DIR = Path(__file__).resolve().parent

if __name__ == '__main__':
    IN  = BASE_DIR  / 'IN/'
    OUT = BASE_DIR  / 'OUT/'
    XLS = BASE_DIR  / 'RESULT/'

    if not Path(IN).exists():
        os.mkdir(IN)

    if Path(OUT).exists():
        shutil.rmtree(OUT)
    os.mkdir(OUT)

    if Path(XLS).exists():
        shutil.rmtree(XLS)
    os.mkdir(XLS)


    unionjrn(IN,OUT,'union.txt')             # Объединение .jrn файлов
    createlog('union.txt',OUT,'CLEAR CASH')  #  Разбивание на log файлов  по слову  'CLEAR CASH'

    files = filesx(OUT,'.log')               # Отсортированы по имени файла
    n = obrlog(OUT,files,XLS)                # Обработка log файлов
    print(f"Количество заправок = {n}")

