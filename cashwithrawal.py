def kup(st):
    ln = len(st)
    ind = (st.find("A"),st.find("B"),st.find("C"),st.find("D"))
    kp = [0,0,0,0]
    for i in range(len(ind)):
        j = ind[i]
        if j == -1:
            kp[i] = 0
        else:
            s = ''
            m = j + 2
            while (not(st[m:m+1]==' ') and  m<ln):
                s = s + st[m:m+1]
                m = m + 1
            kp[i] = int(s)
    return kp

def cashWith(txt,str1):
    i = 0
    nm = []
    while i<len(txt):
        if str1 in txt[i]:
            nm.append(i)
        i = i + 1
    return nm

def cashWithObr(txt,m):
    taken = 'CASH TAKEN'
    n = len(m)
    ms = []

    for i in range(n):
        m1 = m[i] - 1
        k6 = m[i] + 6

        st1 = txt[m[i] + 1]  # Дата и время
        st2 = txt[m[i] + 2]  # Номер карты
        st3 = txt[m[i] + 3]  # Сумма
        d = st3[17:]
        smm = d[:d.find(' UZS')].strip().replace(' ', '')

        st4 = txt[m[i] + 4][19:]  # количество купюр
        msk = kup(st4)


        if (taken in txt[m1]) or (taken in txt[k6]):
            sboy = 0
        else:
            sboy = 1

        ms.append([sboy,st1[:8], st1[21:29], st2[15:31], float(smm),msk[0],msk[1],msk[2],msk[3]])

    return ms