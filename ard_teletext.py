import requests
import html

def ardtext(link):
    holesite = requests.get(link).text
    holesite = holesite.split(">")
    gettxt = False
    teletext = ""
    for ele in holesite:
        if "ardtext_classic" in ele:
            gettxt = True
        if gettxt == True:
            if "</nobr" in ele:
                teletext+=ele.replace("</nobr","")
            if "</div" in ele:
                teletext+="\n"
            if "</a" in ele:
                teletext+=ele.replace("</a","")
            if "<a onclick" in ele:
                teletext+=ele.split("<")[0]
            if "teleTextNavigation" in ele:
                break

    teletext = html.unescape(teletext)
    print(chr(27) + "[2J")
    print(teletext)

if __name__ == "__main__":
    site = 100
    sub = 1
    while site != 999:
           link = "http://www.ard-text.de/index.php?page="+str(site)+"&sub="+str(sub)
           ardtext(link)
           inputstr = input("Seite:"+str(site)+" Sub: "+str(sub)+" > xxx/Ret/Blnk/i/j/999\n")
           if inputstr == "i":
                site = site - 1
                sub = 1
           elif inputstr == "":
                site = site + 1
                sub = 1
           elif inputstr == "j":
                sub = sub - 1
           elif inputstr == " ":
                sub = sub + 1
           else:
               site = int(inputstr)
                sub = 1

if __name__ == "__main__":
    input_page()

