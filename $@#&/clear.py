import time
import os

# disk 1
os.system("start cmd /k {help}")
time.sleep(1)
os.system('cmd /k "select disk 1"')
time.sleep(1)
os.system('cmd /k "clean"')
time.sleep(1)
os.system('cmd /k "convert gpt"')
time.sleep(1)
os.system('cmd /k "select volume 3"')
time.sleep(1)
os.system('cmd /k "format quick FS=NTFS label=New2U"')
time.sleep(1)
os.system('cmd /k "assign letter="U""')
time.sleep(3)
os.system('cmd /c "help"')

# disk 2
os.system("start cmd /k {help}")
time.sleep(1)
os.system('cmd /k "select disk 2"')
time.sleep(1)
os.system('cmd /k "clean"')
time.sleep(1)
os.system('cmd /k "convert gpt"')
time.sleep(1)
os.system('cmd /k "select volume 3"')
time.sleep(1)
os.system('cmd /k "format quick FS=NTFS label=New2U"')
time.sleep(1)
os.system('cmd /k "assign letter="U""')
time.sleep(3)
os.system('cmd /c "help"')

# disk 3
os.system("start cmd /k {help}")
time.sleep(1)
os.system('cmd /k "select disk 3"')
time.sleep(1)
os.system('cmd /k "clean"')
time.sleep(1)
os.system('cmd /k "convert gpt"')
time.sleep(1)
os.system('cmd /k "select volume 3"')
time.sleep(1)
os.system('cmd /k "format quick FS=NTFS label=New2U"')
time.sleep(1)
os.system('cmd /k "assign letter="U""')
time.sleep(3)
os.system('cmd /c "help"')