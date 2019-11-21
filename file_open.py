f = open(r'D:\PythonPro\file_open.py', 'r')
for l in f.readlines():
    print(l, end='')
f.close()