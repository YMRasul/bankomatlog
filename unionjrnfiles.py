import os

def filesx(pathLog,prz):
    log_files = []
    for file in os.listdir(pathLog):
        if file.endswith(prz):
            log_files.append(file)
    return sorted(log_files)

def unionjrn(dir_in,dir_out,unionfile):
    ''' Объеденение нескольких  файлов из папки dir_in
        в один файл и сохранить в папку dir_out
    '''

    files = filesx(dir_in,'.jrn')

    with open(dir_out / unionfile, 'w') as f_out:  # Открыть файл для записи
        for fi in files:                            # пройти по списку
            f = dir_in / fi                         # взять один
            with open(f,'r') as f_in:               # Открыть файл для чтения
                f_out.write('------*------ '+fi+'\n')  # запись имени файла
                for line in f_in:
                    f_out.write(fi[:8]+': ' +line)         # Читать и записать
                f_out.write('------*------ '+fi+'\n\n')              # запись имени файла
    print("1-этап unionjrn")
    return None

