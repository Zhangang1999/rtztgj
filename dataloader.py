import os
path = "E:\桌面文件\image"
list_dir = os.listdir(path)
tmp=0
with open("C:\\Users\lenovo\Documents\WeChat Files\wxid_94x909g7q3nb22\FileStorage\File\\2021-05\\mpii_list.txt") as f:
    for i in f:
        if i.split(" ")[0] in list_dir:
            print(i.split(" ")[0])
            tmp = tmp+1
print(tmp)
print(len(list_dir))