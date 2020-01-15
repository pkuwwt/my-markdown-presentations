
# Bat recipes

---

## Add opener in right click menu

  * Just need to edit the registry

```bat
reg add "HKEY_CLASSES_ROOT\*\shell\open_with_xxx\command" /f /ve /t REG_SZ "C:\Windows\xxx.exe %%1"
```

  * This command add an item `HKEY_CLASSES_ROOT\*\shell\open_with_xxx\command`, and set the default value as `C:\Windows\xxx.exe %1`

---

## Set network interface

  * Setup the `ip`, `net mask`, and `gateway`
```bat
netsh interface ip set address "Local Area Connection" static 192.168.1.100 255.255.255.0 192.169.1.1
netsh int ip show config
```

---

## Setup port forwarding

  * Port 445 of the samba server may be blocked, and changed to 5139. But windows mounts samba disk can only use port 445, so we can forward local 445 port to remote 5139.
```bat
netsh interface portproxy add v4tov4 listenaddress=127.0.0.1 listenport=445 connectaddress=192.168.1.100 connectport=5139
```

---

## Mount sambda disk

  * Use the 445 port
```bat
net use Z: \\192.168.1.100\sambda
```

