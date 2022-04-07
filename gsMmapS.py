#SpamMSG
import os, sys, requests
try:
	import colorama
except:
	os.system("pip install colorama")
	os.system("python SpamMsg.py")

from colorama import init
from colorama import Back
init()
R = Back.RED
w = "\033[1;0m"
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"

def about():
	print(f"{r}+--------------------------------------------------------+")
	print(f"{r}| About       : Spam Message                             |{w}")
	print(f"{r}| YouTube     : Potter                                   |{w}")
	print(f"{r}| Github URL  : https://github.com/PotterTer             |{w}")
	print(f"{r}+--------------------------------------------------------+{w}")
def banner():
	
	print()
	print(f'{y}          ___')
	print(f' _____   __H__         _____         ')
	print(f'|   __|___[{R}"{w}{y}]___ _____|     |___ ___ ')
	print(f"|__   | . [{R}){w}{y}] .'|     | | | |_ -| . |")
	print(f"|_____|  _[{R}'{w}{y}]__,|_|_|_|_|_|_|___|_  |")
	print(f'      |_|  V                    |___|  {r}[{w}*{r}]{w} SpamMsg {r}V{y}1.0')


banner()
about()
phone = input(f"{r}[{w}${r}]!>{w} Phone   {r}: {w}")
message = input(f"{r}[{w}${r}]!> {w}Message {r}: {w}")
print()
#┗ ─ ━ ┚ ╰ ─ ╯
resp = requests.post('https://textbelt.com/text', {
  'phone': f'+66{phone}',
  'message': f'{message}',
  'key': 'textbelt',
})
print(f"{r}[{w}#{r}]{r}> {w}SpamMsg \n{r}[{w}+{r}] {w}States{r}  : {w}[{g}✓{w}]\n{r}[{w}*{r}] {w}Phone   {r}: {w}{phone}\n{r}[{w}*{r}] {w}Message {r}: {w}{message}\n{r}[{w}*{r}] {y}Json {r}", resp.json())
