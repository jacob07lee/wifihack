import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('euc-kr', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "모든 사용자 프로필" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('euc-kr', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "키 콘텐츠" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")