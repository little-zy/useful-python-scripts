

import os
import shutil
'''
import os
flist = []

path = 'D:\\VS_Code_Files\\Coding\\Java\\J6'

def getFlist(path):
    global flist
    lsdir = os.listdir(path)
    # print(lsdir)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]#获取子目录
    # print(dirs)
    if dirs:
        for i in dirs:
            getFlist(os.path.join(path, i))#对所有子目录递归
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]#
    for file in files:
        flist.append(file)
    return flist

resDir = 'res'
flist = getFlist(path)
print(flist)
'''
# =================================================================================
flist = []
path = 'D:\VS_Code_Files\Coding\Python\worms' 


def getFlist(path):
    global flist
    lsdir = os.listdir(path)
    # print(lsdir)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]  # 获取子目录
    # print(dirs)
    if dirs:
        for i in dirs:
            getFlist(os.path.join(path, i))  # 对所有子目录递归
    files = [os.path.join(path, i)
             for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for file in files:
        flist.append(file)
    return flist


flist = getFlist(path)
#print(os.path)


def moveFiles(Flist, path):
    for file in Flist:
        # if not path.isfile(file):
        print('move "%s" to "%s"...\n' % (file, path))
        try:
            shutil.move(file, path)
        except:
            continue
        else:
            continue


moveFiles(flist, path)


def rddirs(path):
    lsdir = os.listdir(path)
    dirs = [os.path.join(path, i)
            for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            print(i)
            try:
                os.rmdir(i)
            finally:
                continue


rddirs(path)


'''
source_path = os.path.abspath(
    r'D:\\VS_Code_Files\\Coding\\Java\\J6')
target_path = os.path.abspath(r'D:\\VS_Code_Files\\Coding\\Java\\J6')

if not os.path.exists(target_path):
    os.makedirs(target_path)

if os.path.exists(source_path):
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(source_path):
        for file in files:
            src_file = os.path.join(root, file)
            shutil.copy(src_file, target_path)
            print(src_file)

print('copy files finished!')
'''
