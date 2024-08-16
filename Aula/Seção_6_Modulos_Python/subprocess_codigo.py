import subprocess
import sys

# Informa qual SO está na máquina
print(sys.platform)

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'
system = sys.platform

# # sys.platform = linux, linux2, darwin, win32
# Dessa forma, meu código pode funcionar em qualquer sistema operacional
if system == 'win32':
  cmd = ['ping', '127.0.0.1']
  encoding = 'cp850'

proc = subprocess.run(cmd, capture_output=True, text=True, encoding=encoding)
print()
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)