import requests
import colorama
from colorama import Fore
print(Fore.CYAN + "LUTS Webhook Spammer (Cntrl C to stop)")
webhook = input(Fore.CYAN+ 'Paste webhook here : ')
req = requests.get(webhook)
if "Unknown Webhook" in req.text or ', "channel_id":' not in req.text:
  print(Fore.RED + 'Invalid Webhook.')
  input()
message = input(Fore.CYAN+ 'What message to spam? : ')
username = input(Fore.CYAN+ 'Input the bots desired username : ')
data = {"content": message,
        "username": username}
message_amount = 0
try:
  while True:
    r = requests.post(webhook, data=data)
    if 'rate limited' in r.text:
      print(Fore.RED + 'Error, Ratelimited.')
    elif r.text == '':
      message_amount += 1
      print(Fore.GREEN + f"{message_amount} Messages Sent!")
    else:
      print(Fore.YELLOW + "Error sending message.")
except KeyboardInterrupt:
  print(Fore.CYAN + f'Stopping spam, {message_amount} messages sent.')
  input()
