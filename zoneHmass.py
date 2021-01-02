#!/usr/bin/python39

import os
try:
  import requests,re,sys
except:
  os.system('pip install requests')
  quit('Jalankan ulang skrip')
  
pil = sys.argv

if len(pil) == 3:
  domains = open(pil[1],'r').read().splitlines()
  attacker = pil[2]
  for you in domains:
    data = {
      'defacer': attacker,
      'domain1': you,
      'hackmode': 1,
      'reason': 1
      }
    post = requests.post('http://www.zone-h.com/notify/single',data).text
    if re.match('/color=\"red\">OK<\/font><\/li>/',post):
      print(you,'-> \033[32;1mOK')
      continue
    else:
      print(you,'-> \033[31;1mERROR')
      continue
else:
  print("""
(/) -------------
(/) --------
(/)    ZoneH Mirrorring
(/)    By: EtcAug10
(/)    version: 1.0
(/) --------
(/) -------------

USAGE:
  python3 zoneHmass.py [SITES] [ATTACKER]
Example:
  python3 zoneHmass.py depes.txt AryaKun
  
{/} HAPPY HACKING {\}
  """)

# Code made by 100% Gabut People