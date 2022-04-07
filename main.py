#! usr/bin/python
import os, sys, time, requests
try:
	import colorama
except:
	os.system("pip install colorama")
	
from colorama import Back

R = Back.RED
w = "\033[1;0m"
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
def banner():
	print(f"""{y}
   ____        _      __   {r} ___       __  __         
{y}  / __/_______(_)__  / /_ {r} / _ \___  / /_/ /____ ____
{y} _\ \/ __/ __/ / _ \/ __/{r} / ___/ _ \/ __/ __/ -_) __/
{y}/___/\__/_/ /_/ .__/\__/{r} /_/   \___/\__/\__/\__/_/   {y}V {w}[{r}1.1{w}]
{y}             /_/
""")

	print (f" {r}[{y}#{r}] {w}Script Potter")
	print (f" {r}[{y}*{r}] {w}Download")

def fut():
	print(f"""
 {r}* {w}[{R}{y} Select {w}] {r}*{w}
{r}[{y}1{r}] {y}SpammerV2 {w}[{r}New{w}]
{r}[{y}2{r}] {y}SpamMsg {w}[{r}New{w}]
{r}[{y}3{r}] {y}WebSCP {w}[{r}New{w}]
{r}[{y}4{r}] {y}Attack Net
{r}[{y}5{r}] {y}Spammer
{r}[{y}6{r}] {y}IP-Search
{r}[{y}7{r}] {y}Email Message
{r}[{y}8{r}] {y}SUPER
{r}[{y}0{r}] {w}Update {g}Check
{r}[{y}Q{r}] Exit
{r}[{y}MSG{r}] {g}» {w}Send {r}Message {w}To {g}Potter «
""")
os.system("clear")
banner()
fut()
f = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
print()
try:
	os.system("pkg install tor")
except:
	pass
#==================== Number1
if f == "1" or f == "01":
	os.system("clear")
	print(f"""{y}
 _____                             {r}_____ ___ 
{y}|   __|___ ___ _____ _____ ___ ___{r}|  |  |_  |
{y}|__   | . | .'|     |     | -_|  _{r}|  |  |  _|
{y}|_____|  _|__,|_|_|_|_|_|_|___|_| {r} \___/|___|
{y}      |_|
 {r}[{y}#{r}] {y}Spammer{r}V2 {w}[{r}New{w}]
	""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	print()
	if select == "1":
		try:
			time.sleep(5)
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{r}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		p = input(f"{r}[{y}${r}]{y}» {w}Phone {r}: {w}")
		if run == "y":
			os.system(f"python 2VremremmapS.py {p}")
			print(f"{r}[{y}*{r}] {w}Return {g}Home")
			time.sleep(4)
			os.system("python main.py")
		else:
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number2
if f == "2" or f == "02":
	os.system("clear")
	print(f"""{y}
 _____               {r}_____         
{y}|   __|___ ___ _____{r}|     |___ ___ 
{y}|__   | . | .'|    {r} | | | |_ -| . |
{y}|_____|  _|__,|_|_|_{r}|_|_|_|___|_  |
{y}      |_|                   {r}  |___|
 {r}[{y}#{r}] {y}Spam{r} Message {w}[{r}New{w}]
	""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	print()
	if select == "1":
		try:
			time.sleep(5)
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{r}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("python gsMmapS.py")
			print(f"{r}[{y}*{r}] {w}Return {g}Home")
			time.sleep(4)
			os.system("python main.py")
		else:
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number3
if f == "3" or f == "03":
	os.system("clear")
	print(f"""{y}
 _ _ _     _   {r}_____ _____ _____ 
{y}| | | |___| |_{r}|   __|     |  _  |
{y}| | | | -_| . {r}|__   |   --|   __|
{y}|_____|___|___{r}|_____|_____|__|   
 {r}[{y}#{r}] {y}Web {r}Scraping {w}[{r}New{w}]
""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	if select == "1":
		try:
			os.system("bash 3-install.sh")
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{r}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("python WebSCP.py")
			os.system("bash 3.sh")
			os.system("python main.py")
		else:
			os.system("bash 3.sh")
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number4
if f == "4" or f == "04":
	os.system("clear")
	print(f"""{y}
 _____ _   _           _     {r} _____     _   
{y}|  _  | |_| |_ ___ ___| |_ {r}  |   | |___| |_ 
{y}|     |  _|  _| .'|  _| '_|{r}  | | | | -_|  _|
{y}|__|__|_| |_| |__,|___|_,_| {r} |_|___|___|_|  
 {r}[{y}#{r}] {y}Attack {r}Net
	""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	if select == "1":
		try:
			os.system("bash 4-install.sh")
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{r}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("pkg install perl")
			print(f"{r}[{y}#{r}] {r}Command")
			print(f"{r}[{y}*{r}] {w}perl net.pl <ip> <port> 65500 0")
			sys.exit()
			os.system("bash 4.sh")
			os.system("python main.py")
		else:
			os.system("bash 4.sh")
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number5
if f == "5" or f == "05":
	os.system("clear")
	print(f"""{y}
 _____                             
{y}|   __|___ ___ _____ {r}_____ ___ ___ 
{y}|__   | . | .'|     {r}|     | -_|  _|
{y}|_____|  _|__,|_|_|_{r}|_|_|_|___|_|  
{y}      |_| 
 {r}[{y}#{r}] {y}Spam{r}mer
	""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	if select == "1":
		try:
			time.sleep(5)
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{g}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("python remmapS.py")
			os.system("python main.py")
		else:
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number6
if f == "6" or f == "06":
	os.system("clear")
	print(f"""{y}
 _____ _____   {r} _____                 _   
{y}|     |  _  | {r} |   __|___ ___ ___ ___| |_ 
{y}|-   -|   __|{r}  |__   | -_| .'|  _|  _|   |
{y}|_____|__|   {r}  |_____|___|__,|_| |___|_|_|
 {r}[{y}#{r}] {y}IP {r}Search
""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	if select == "1":
		try:
			os.system("bash 6-install.sh")
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{r}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("cd IP && python run.py")
			os.system("nash 6.sh")
			os.system("python main.py")
		else:
			os.system("cd Bash && bash 6.sh")
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number7
if f == "7" or f == "07":
	os.system("clear")
	print(f"""{y}
 _____ _____    {r}_____                         
{y}|   __|     | {r} |     |___ ___ ___ ___ ___ ___ 
{y}|   __| | | |  {r}| | | | -_|_ -|_ -| .'| . | -_|
{y}|_____|_|_|_| {r} |_|_|_|___|___|___|__,|_  |___|
                                     |___|    
 {r}[{y}#{r}]{y} Email {r}Message
	""")
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	if select == "1":
		try:
			os.system("bash 7-install.sh")
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{r}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("cd em && python run.py")
			os.system("bash 7.sh")
		else:
			os.system("bash 7.sh")
			os.system("python main.py")
	else:
		os.system("python main.py")
#==================== Number8
if f == "8" or f == "08":
	os.system("clear")
	print(f"""{y}
 _____ _____ {r}_____ _____ _____ 
{y}|   __|  | {r} |  _  |   __| __  |
{y}|__   |  | {r} |   __|   __|    -|
{y}|_____|_____{r}|__|  |_____|__|__|
 {r}[{y}#{r}] {y}SU{r}PER
                               """)
	print(f"{r}[{y}1{r}] {w}Download")
	print(f"{r}[{y}Q{r}] {y}Home")
	select = input(f"{r}[{y}${r}]{y}» Select {r}: {w}")
	if select == "1":
		try:
			os.system("bash 8-install.sh")
			print(f"{r}[{y}*{r}] {w}Install [{g}Done{w}]")
		except:
			print(f"{r}[{y}*{r}] {w}Install [{g}Fall{w}]")
			sys.exit()
		run = input(f"{r}[{y}${r}]{y}» Run? {w}[{y}Y/N{w}] {r}: {w}")
		if run == "y":
			os.system("cd SUPER && python run.py")
			os.system("bash 8.sh")
		else:
			os.system("bash 8.sh")
			os.system("python main.py")
	else:
		os.system("python main.py")
# System=====================
#==================== Number0
if f == "0":
	os.system("clear")
	print(f"""{y}
 _____       {r}_     _       
{y}|  |  |___{r} _| |___| |_ ___ 
{y}|  |  | . {r}| . | .'|  _| -_|
{y}|_____|  _{r}|___|__,|_| |___|
{y}      |_| {r}[{y}#{r}] {y}Up{r}date
""")
	try:
		os.system("bash 0-install.sh")
		print(f"{r}[{y}+{r}]{w} Reset {w}[{g}Done{w}] & {g}Setup")
	except:
		print(f"{r}[{y}+{r}]{w} Reset {w}[{r}!{w}]")
	time.sleep(3)
#Exit ================
if f == "Q" or f == "q":
	os.system("clear")
	sys.exit()
#msg =================
if f == "msg" or f == "MSG":
	os.system("clear")
	print(f"""{y}
 _____           _  {r}  _____ _____ _____ 
{y}|   __|___ ___ _| | {r} |     |   __|   __|
{y}|__   | -_|   | . |  {r}| | | |__   |  |  |
{y}|_____|___|_|_|___| {r} |_|_|_|_____|_____|
{r}[{y}#{r}] {g}Send Message""")
	message = input(f"{r}[{y}${r}]{y}» Message {r}: {w}")
	print()
	def api(): #         time.sleep(1.00000000000)
		user = "Mozilla/5.0 (Linux; Android 5.1; OPPO F1s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36" #         time.sleep(1.00000000000)
		#         time.sleep(1.00000000000)
		cookie = "datr=VGmKYamVAs889HFSNg0D8KkJ;sb=yJeaYT7gZiRDs-RlCYA3kCai;c_user=100077668905009;xs=20%3AAuSgG9IFVHD-5Q%3A2%3A1648364307%3A-1%3A13426;fr=0jcrUBmtvGgBjVOBI.AWWjPlu96iR8pL7cm3o8wXJx_y0.Bh-Lyd.Ti.AAA.0.0.BiQqE5.AWWiQuvx9v4;m_pixel_ratio=2;wd=360x566;x-referer=eyJyIjoiL21lc3NhZ2VzL3JlYWQvP3RpZD1jaWQuYy4xMDAwNDg0MDI5NjgzNTclM0ExMDAwNzc2Njg5MDUwMDkmZW50cnlwb2ludD1qZXdlbCZzdXJmYWNlX2hpZXJhcmNoeT11bmtub3duIiwiaCI6Ii9tZXNzYWdlcy9yZWFkLz90aWQ9Y2lkLmMuMTAwMDQ4NDAyOTY4MzU3JTNBMTAwMDc3NjY4OTA1MDA5JmVudHJ5cG9pbnQ9amV3ZWwmc3VyZmFjZV9oaWVyYXJjaHk9dW5rbm93biIsInMiOiJtIn0%3D" #         time.sleep(1.00000000000)
		head = {
		   "Host": "m.facebook.com", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "content-length": "593", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "sec-ch-ua-mobile": "?1", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "user-agent": f"{user}", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "content-type": "application/x-www-form-urlencoded", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "accept": "*/*", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "origin": "https://m.facebook.com", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "sec-fetch-site": "same-origin", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "sec-fetch-mode": "cors", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "sec-fetch-dest": "empty", #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "referer": "https://m.facebook.com/messages/read/?tid=cid.c.100048402968357%3A100077668905009&entrypoint=jewel&surface_hierarchy=unknown", #         time.sleep(1.00000000000) #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		   "cookie": f"{cookie}" #         time.sleep(1.00000000000)
#         time.sleep(1.00000000000)
		}
		try:
			requests.post("https://m.facebook.com/messages/send/?icm=1&entrypoint=jewel&surface_hierarchy=unknown&refid=12", headers=head, data=f"tids=cid.c.100048402968357%3A100077668905009&wwwupp=C3&ids%5B100048402968357%5D=100048402968357&body={message}&waterfall_source=message&action_time=1649208699016&fb_dtsg=AQFNRwRN5I94gvE%3A20%3A1648364307&jazoest=21916&lsd=hEP5GUZtl-ZvJQc3AGnoW8&__dyn=1KQEGiFoO2G69U-4UpwGzVQ2mml3onxGi5EO9wHxG9xu3Za363u2W3q327HzE24xm6Uhx61Zw9m3y4o5a1nwWwbm3C3y1gCwSxu0om787u2W1Jwt8-0nSUS2K2G0FU5y6E52229wcq0C9EdE2IzUuw9O1Aw9-2i1qw8W1uwa-7U88138bodEGdw46wbS1bwzw&__csr=&__req=10&__a=AYkSVNykSo3JoLTwKfwRz3cr-DLLoSVV8YEFWzVMsrQcHqOlEiJtgKK29RfZhpkY3tYIkcZxlgZwbYNjfq2FP86H0nGqIbGDVnKC0of4X7-Ekg&__user=100077668905009") #         time.sleep(1.00000000000)
			print(f"{r}[{y}#{r}] {y}Message {r}» {w}[{g}SEND{w}]")
		except:
			print(f"{r}[{y}#{r}] {y}Message {r}» {w}[{r}!{w}]")
	api()
#         time.sleep(1.00000000000)
	print(f"{r}[{y}*{r}] {w}Return {g}Home")
	time.sleep(4)
	os.system("python main.py")
		
print(f"{r}[{y}?{r}] {w}{f} {g}Not Found")
time.sleep(3)
os.system("python main.py")

"""
Nice ( ͡° ͜ʖ ͡°)
"""