

import os
import re
import shutil
oldnamepattern = re.compile(r"""^.*截图(.*).png$""", re.VERBOSE)
i=0
for name in os.listdir('D:\\桌面\\新建文件夹\\新建文件夹\\'):
    mo = oldnamepattern.search(name)
    if mo == None:
        continue
    i+=1
    newname = chr(i+64)+'.png'
    absworkdir = os.path.abspath('D:\\桌面\\新建文件夹\\新建文件夹\\')
    name = os.path.join(absworkdir, name)
    newname = os.path.join(absworkdir, newname)
    print('renaming "%s" to "%s"...' % (name, newname))
    shutil.move(name, newname)
