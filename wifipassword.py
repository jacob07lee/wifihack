import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'networks']).decode('euc-kr').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "SSID" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan','show', 'networks']).decode('euc-kr').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "인증" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")