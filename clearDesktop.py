import os, time, shutil
from tkinter import *
from tkinter.messagebox import showinfo                         # for show a message
day = time.strftime('%a', time.localtime())[:-1]                #know which day today

#files and links (setup)
notBanned = ('desktop.ini', )                                   #value creates list of files which can exist on the desktop
workDir = r"C:\\\Desktop"                                       #value creates folder where is the desktop
studentTrash = r"C:\\\Documents\Trash"                          #value creates folder where are trashes from desktop
vm=r"C:\\\VirtualBox VMs"                                       #value creates folderwhere are virtual boxes (it's only for me)
allDelFiles = list()                                            #valuer creates list of removed files

#function clear your desktop
def clearDesktop(day,notBanned,workDir,studentTrash):
    dirMon = os.listdir(path=workDir)                           #if today is Monday all files move to Trash
    for d in dirMon:
        if day =='Tue' or day == 'Thu':
            if d not in notBanned:
                delDir = workDir+'\\'+d
                shutil.move(delDir, studentTrash)
                #print(d, 'file is moved')
    dirFr = os.listdir(path=studentTrash)
    for d in dirFr:                                             #if today is Friday all files remove from Trash
        if day == 'Fr':
            try:
                if os.path.isdir(studentTrash + '\\' + d):
                    delDir = studentTrash + '\\' + d
                    shutil.rmtree(path=delDir)
                    allDelFiles.append(d)
                    #print(d, 'folder is removed')
                elif os.path.isfile(studentTrash + '\\' + d):
                    delDir = studentTrash + '\\' + d
                    os.remove(path=delDir)
                    allDelFiles.append(d)
            except PermissionError:
                continue

#function clear VMs
def delVM(vm):
    vms = os.listdir(path=vm)
    for d in vms:
        allDelFiles.append(d)
        delDir = vm + '\\' + d
        shutil.rmtree(path=delDir)
        print(d, 'folder is removed')

if __name__ == "__main__":
    try:
        #if folder /Trash exist
        if day == 'Mon' or day == 'Fr':
            clearDesktop(day, notBanned, workDir, studentTrash)
            delVM(vm)
            #Please your title and message
            showinfo(title='Файлы удалены',
                     message="Обращаю Ваше внимание!!!\nСтуденты хранят свои файлы в папке: 'Документы'.\nС рабочего стола ВСЕ ФАЙЛЫ и ВИРТУАЛЬНЫЕ МАШИНЫ из 'стандартной директории' будут удалены.\nВиртуальные машин храняться на Вашей флешке.\nУдаленные файлы: %s" % allDelFiles)
    except FileNotFoundError:
        #if folder /Trash doesn't exist
        os.mkdir(r"C:\\\Documents\Trash")                       #it creates folder /Trash
        if day == 'Mon' or day == 'Fr':
            clearDesktop(day, notBanned, workDir, studentTrash)
            delVM(vm)
            # Please your title and message
            showinfo(title='Файлы удалены',
                     message="Обращаю Ваше внимание!!!\nСтуденты хранят свои файлы в папке: 'Документы'.\nС рабочего стола ВСЕ ФАЙЛЫ и ВИРТУАЛЬНЫЕ МАШИНЫ из 'стандартной директории' будут удалены.\nВиртуальные машин храняться на Вашей флешке.\nУдаленные файлы: %s" % allDelFiles)



