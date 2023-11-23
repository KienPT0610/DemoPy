path = 'data.txt'

dictionary = {
    'A+' : 4.0,
    'A' : 3.7,
    'B+' : 3.5,
    'B' : 3.0,
    'C+' : 2.5,
    'C' : 2.0,
    'D+' : 1.5,
    'D' : 1.0,
    'F' : 0.0
}

def save(line):
    try:
        f = open(path, 'a', encoding='utf8')
        f.writelines(line)
        f.writelines('\n')
        f.close()
    except:
        pass

def read():
    ds = []
    try:
        f = open(path, 'r', encoding='utf8')
        for i in f:
            data=i.strip()
            arr=data.split('-')
            ds.append(arr)
        f.close()
    except:
        pass
    return ds

