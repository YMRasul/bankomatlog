from pathlib import Path
from unionjrnfiles import unionjrn
from createlogfiles import createlog,filesx
from  obrlogfiles import  obrlog

BASE_DIR = Path(__file__).resolve().parent

if __name__ == '__main__':
    IN  = BASE_DIR  / 'in/'
    OUT = BASE_DIR  / 'out/'
    XLS = BASE_DIR  / 'RESULT/'


    unionjrn(IN,OUT,'union.txt')             # Объединение .jrn файлов
    createlog('union.txt',OUT,'CLEAR CASH')  #  Разбивание на log файлов  по слову  'CLEAR CASH'

    files = filesx(OUT,'.log')               # Отсортированы по имени файла
    obrlog(OUT,files,XLS)                    # Обработка log файлов

