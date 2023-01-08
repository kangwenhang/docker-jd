####
import requests
import time
import subprocess
import re

def main():
    attempts=0
    success = False
    g,g1,agent,mtp_addr = socks5_decide()
    pm2stop = "pm2 stop tgbot"
    pm2start = "pm2 start tgbot"
    url = "https://www.google.com/"
    proxies = {
      g,
       g1
    }
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko)Version/5.1 Safari/534.50'}
    while attempts < 3 and not success:
        a = pm2_status()
        b = "stopped"
        c = "online"
        try:
            if agent == False :
                resp = requests.get(url,headers=headers,timeout=40)
                if resp.status_code == 200 and b in a:
                    subprocess.run(pm2start, shell=True)
                    success = True
                elif resp.status_code == 200 and c in a:
                    success = True
            elif agent == True and mtp_addr == False:
                resp = requests.get(url,headers=headers,proxies=proxies,timeout=40)
                if resp.status_code == 200 and b in a:
                    subprocess.run(pm2start, shell=True)
                    success = True
                elif resp.status_code == 200 and c in a:
                    success = True
            else:
                break
        except:
            attempts += 1
            time.sleep(5)
            if attempts == 3 and c in a:
                subprocess.run(pm2stop, shell=True)

def pm2_status():
    pm2status = "pm2 describe tgbot"
    p = subprocess.run(pm2status,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    return p.stdout

def socks5_decide():
    desStr1 = 'proxy_addr:'
    desStr2 = 'proxy_port:' 
    desStr3 = 'http_addr:' 
    desStr4 = 'http_port:' 
    desStr5 = 'mtp_addr:' 
    agent = True
    mtp_addr = False
    e = open("config.yml","r",encoding='utf-8')
    data = e.readlines()
    e.close
    for line in data:
        if desStr1 in line:
            f = line
    str_re1 = f.split("\"")[1]
    if len(str_re1) == 0:
        for line in data:
            if desStr3 in line:
                f = line
        str_re1 = f.split("\"")[1]
        if len(str_re1) == 0:
            agent = False
            for line in data:
                if desStr5 in line:
                    f = line
            str_re1 = f.split("\"")[1]
            if len(str_re1) == 0:
                agent = False
            else:
                agent = True
                mtp_addr = True
        else:
            for line in data:
                if desStr4 in line:
                    f = line
            str_re2 = f.split("\"")[1]
            g = "'http'" + ":" + "'http://" + str_re1 + ":" + str_re2 + "'"
            g1 = "'https'" + ":" + "'https://" + str_re1 + ":" + str_re2 + "'"
    else:
        for line in data:
            if desStr2 in line:
                f = line
        str_re2 = f.split("\"")[1]
        g = "'http'" + ":" + "'socks5://" + str_re1 + ":" + str_re2 + "'"
        g1 = "'https'" + ":" + "'socks5://" + str_re1 + ":" + str_re2 + "'"
    return g,g1,agent,mtp_addr

if __name__ == '__main__':
    main()
