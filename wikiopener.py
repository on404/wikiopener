import subprocess ,datetime ,os ,time, random
last = subprocess.getstatusoutput("last -4 | awk 'NR==3{print $4, $5 ,$6}'")
date = f"{datetime.datetime.now():%a %b %-d}"
if not (date in last):
    for i in range(3):
        output = str(subprocess.getstatusoutput("ping 9.9.9.9 -c 4"))
        if ("unreachable" in output):
            time.sleep(300)
        else:
            home = "https://he.wikipedia.org/wiki/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99"
            srand = "https://he.wikipedia.org/wiki/%D7%9E%D7%99%D7%95%D7%97%D7%93:Random#/random"
            os.system("open '{}' '{}'".format(home, srand))
            break
exit()