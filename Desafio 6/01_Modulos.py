
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Printar o Sistema Operacional que voce esta usando:
print(sys.platform)

# Printar a versão de Python que voce esta usando:
print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Printar a process Id atual
print(os.getpid())

# Printar o atual diretório:
print(os.getcwd())

# Printar o nome da maquina
print(os.uname().nodename)