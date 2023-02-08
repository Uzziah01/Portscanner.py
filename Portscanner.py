# Simple Port Scanner Project.
import socket
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def scan(target, ports):
    print('\n' + Fore.YELLOW + ' 🔍 Starting Scan For ' + str(target) + " ...")
    print('\n' + "%-17s %s" % (titleClosed, titleOpen))
    for port in range(1, ports):
        scan_port(target, port)


# Headings
titleClosed = 'Closed Ports'
titleOpen = 'Open Ports'

# Data value
Closed_Ports = (Fore.RED + "[-]"), "Port "
Open_Ports = (Fore.GREEN + "[+]"), "Port "


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(("%-17s" % Fore.GREEN + "[+]"), "Port " + str(port))
        sock.close()
    except:
        print(("%s" % Fore.RED + "[-]"), "Port " + str(port))


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
    print(Fore.YELLOW + "[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)

else:
    scan(targets, ports)
