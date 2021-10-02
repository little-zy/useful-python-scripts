
import os
import re
import shutil
oldnamepattern=re.compile(r"""^(\d)Chapter(.*)$""",re.VERBOSE)
for name in os.listdir('.'):
    mo=oldnamepattern.search(name)
    if mo==None :
        continue
    numpart=mo.group(1)
    nampart=mo.group(2)
    newname='Chapter'+numpart+nampart
    absworkdir=os.path.abspath('.')
    name=os.path.join(absworkdir,name)
    newname=os.path.join(absworkdir,newname)
    print('renaming "%s" to "%s"...'%(name,newname))
    shutil.move(name,newname)
    