import os
def opr(txt,word,n,f_out):
    while not (word in txt[n]):
        n = n + 1
    f_out.write(txt[n])
    n = n + 1
    while  ((n < len(txt)) and (not word in txt[n])):
        f_out.write(txt[n])
        n = n + 1
    return n
#
def createlog(unionfile,dir_out,word):
    txtUnion = dir_out / unionfile
    with open(txtUnion, 'r') as f:  # Открыть файл для чтения
        txt = [line for line in f]
    i = 0
    k = 0
    while (i < len(txt)):
        k = k + 1
        cash = 'cash' +f"{str(k):0>3}" + '.log'
        with open(dir_out / cash, 'w') as f_out:  # Открыть файл для записи
            i = opr(txt,word,i,f_out)
    print('2-этап logfiles')
    return None

def filesx(pathLog,prz):
    log_files = []
    for file in os.listdir(pathLog):
        if file.endswith(prz):
            log_files.append(file)
    return sorted(log_files)
