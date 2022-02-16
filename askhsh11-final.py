import requests
import json
from scipy.stats import entropy as en
import pandas as pd

req = requests.get("https://drand.cloudflare.com/public/latest")

periexomeno = req.text 
periexomeno_se_le3iko = json.loads(periexomeno)

round = periexomeno_se_le3iko['round']
kwdikas = ""
for i in range (20):
    url = f"https://drand.cloudflare.com/public/{round}"
    req2 = requests.get(url)

    periexomeno2 = req2.text 
    periexomeno2_se_le3iko = json.loads(periexomeno2) 

    randomness = periexomeno2_se_le3iko['randomness']
    last20 = randomness[len(randomness)- 20 : len(randomness)]
    
    kwdikas = kwdikas + last20 
    round-=1 

kwdikashex=[]
for i in range(len(kwdikas)):
    kwdikashex.append(kwdikas[i])

kwdikashex = pd.Series(kwdikashex)

data=en(kwdikashex.value_counts())
print(data)