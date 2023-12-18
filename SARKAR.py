import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
SARKAR=platform.architecture()[0]
if SARKAR=="32bit":__import__("SARKAR32")
elif SARKAR=="64bit":__import__("SARKAR64")
