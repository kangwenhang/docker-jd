####
import requests
import time
import subprocess

def main():
    attempts=0
    success = False
    pm2stop = "pm2 stop tgbot"
    pm2start = "pm2 start tgbot"
    url = "https://www.google.com/"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko)Version/5.1 Safari/534.50'}
    while attempts < 3 and not success:
        a = pm2_status()
        b = "stopped"
        c = "online"
        try:
            resp = requests.get(url,headers=headers,timeout=40)
            if resp.status_code == 200 and b in a:
                subprocess.run(pm2start, shell=True)
                success = True
            elif resp.status_code == 200 and c in a:
                success = True
        except:
            attempts += 1
            time.sleep(5)
            if attempts == 3 and c in a:
                subprocess.run(pm2stop, shell=True)

def pm2_status():
    pm2status = "pm2 describe tgbot"
    p = subprocess.run(pm2status,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    return p.stdout

if __name__ == '__main__':
    main()
