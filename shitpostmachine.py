# Catware Shitpost Machine
#
from http.server import HTTPServer, SimpleHTTPRequestHandler
from random import choice, randint
from os import getenv
from string import ascii_letters as letters

from searchimages import ImgSearch

imgSearch = ImgSearch()

search_keywords = "бомбандировка, военный самолет, боеголовки, воронеж бомбить, флаг воронежа, nuclear explosion," \
                  " bombardment".split(", ")
list_randwords = "мать, говно, воронеж, бомбить, ебал, сука, пиздец, ахахахах, улелелел, АУЕАУЕАУЕ, ауеауеауе, гандон," \
                 " веды, ведический, база, базированный, БПАЗА!, Б А З А, чзх, ведает, славяноарийство, славвяно арий," \
                 " либерасты, евреи, семясвечник, пятница, шаббат шалом, бомбить воронеж, воронеж, бомбить, ракеты," \
                 " удар".split( ", ")
list_concate = "йо,ви,ах,ауе,ыыыы".split(",")
list_additional = "через,с помощью,в,как".split(",")
list_people = "президент, фриспик, евреи, пидорасы, геи, коммунисты, либерасты, базисты".split(",")
list_actions = "разбомбил(-a),стёр(-а),разъебал(-ла),насрал(-а)".split(",")
list_commands = "apt,ping,mutter,dnf,sudo,nano,vim,pacman,xbps-install,mount,umount,systemctl,useradd,firefox," \
                "sddm,rm,cd,suda,doas,anal,vi,elinks,python3,java,ruby,nginx,rc-update,rc-service,sv,yum,apk,nmap," \
                "cp,ln,echo,tee,cat,tac".split(",")
list_flags = "--install --fix-missing --aye -rf --verbose --update --deep_dark_fanstasy --add --remove --unmerge"\
    .split(" ")
list_params = "install ЧЕСНОК purge delete".split(" ")
list_formats = "txt rtf conf py rb html css js deb rpm tar.gz tar tar.bz2 mp3 mp4 avi png jpg bmp exe elf".split(" ")
tags = "h1,h2,h3,h4,h5,h6,strong,i,strike,pre".split(",")

typical_form = """ <form>
  <p><b>{}</b></p>
  <p><input type="radio" name="answer" value="a1">{}<Br>
  <input type="radio" name="answer" value="a2">{}<Br>
  <input type="radio" name="answer" value="a3">{} {}</p>
  <p><input type="submit"></p>
 </form>"""


def filter(text):
    ch = choice(["fuck", "registry", "words", "rev"])
    r = ""
    if ch == "fuck":
        for x in text:
            ch2 = choice([True, False, False, False, False, False])
            if ch2:
                r += ""
            else:
                r += x
    if ch == "registry":
        for x in text:
            ch2 = choice([True, False])
            if ch2:
                r += x.upper()
            else:
                r += x
    if ch == "words":
        lst = []
        for x in text.split(" "):
            ch2 = choice([True, False])
            if ch2:
                lst.append(x.upper())
            else:
                lst.append(x)
        r = " ".join(lst)
    if ch == "rev":
        r = r[::-1]
    return r


def createmarque():
    aye = "<marque {} scrolldelay='{}' truespeed>".format(genstyle(), genshitpost())
    aye += "</marque>"
    return aye


def genstyle():
    aye = "style='"
    aye += "position: absolute;color: \#" + choice(letters) + choice(letters) + choice(letters) + choice(
        letters) + choice(letters) + choice(letters) + "; "
    aye += "font-size: " + str(randint(14, 64)) + "px;"
    aye += "padding: " + str(randint(0, 15)) + "px;"
    aye += "border: " + str(randint(0, 5)) + "px solid;"
    aye += "margin: " + str(randint(1, 15)) + "px;"
    aye += "background: \#" + choice(letters) + choice(letters) + choice(letters) + choice(letters) + choice(
        letters) + choice(letters) + ";"
    if choice([True, False]):
        aye += "box-shadow: 0 0 10px rgba(0,0,0,0.5);"
    if choice([True, False]):
        aye += "backdrop-filter: blur({}px);".format(str(randint(50, 150)))
    if choice([True, False]):
        aye += "font-family: lobSter;"
    aye += "align: " + choice("center | justify | left | right | start | end".split(" | ")) + ";"
    if choice([True, False]):
        aye += "right: " + str(randint(1, 90)) + "%;"
        aye += "bottom: " + str(randint(1, 90)) + "%;"
    aye += "'"
    return aye


def gencolorz():
    amd = ["red", "violet", "indigo", "yellow", "white", "black", "blue", "orange", "green", "brown"]
    lst = []
    for x in range(7):
        lst.append(choice(amd))
        return ",".join(lst)


def writefile(text, target):
    file = open(target, "w", encoding="utf-8")
    file.write(text)
    file.close()


def genshitpost():
    global list_flags, list_params, list_randwords, list_commands, list_people, list_actions, list_flags,\
        list_formats, list_concate, list_additional
    res = ""
    list_flags.append("--" + choice(list_randwords))
    list_flags.append("--" + choice(list_randwords) + '="' + choice(list_randwords) + '"')
    list_flags.append("")
    list_params.append(choice(list_randwords) + "." + choice(list_formats))
    list_params.append(choice(list_randwords))
    list_params.append("/" + choice(list_randwords) + "/" + choice(list_randwords))
    list_params.append(
        "/" + choice(list_randwords) + "/" + choice(list_randwords) + "/" + choice(list_randwords) + "." + choice(
            list_formats))
    gentype = choice("randomwords,action,command".split(","))

    def randomwords(count):
        res = ""
        for x in range(count):
            res += choice(list_randwords) + " "
        return str(choice(list_concate) * randint(1, 10))

    if gentype == "randomwords":
        res += randomwords(randint(1, 10))

    if gentype == "action":
        pass
    if gentype == "command":
        res = ""
        ch = choice([1, 2, 3])
        res = "{} {} {}".format(choice(list_commands), choice(list_params), choice(list_flags))
        if ch == 1:
            res += " | " + "{} {}".format(choice(list_commands), choice(list_flags))
        if ch == 2:
            res += " >> " + choice(list_params)
        if ch == 3:
            pass
    if choice([True, False]):
        res = filter(res)
    return res


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        SimpleHTTPRequestHandler.__init__(self, *args, **kwargs, directory='public')

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = '''<html><head>
                   <meta charset="utf-8">
                   <title>'''

            html += genshitpost() + "</title><link rel='stylesheet' href='/styles.css'><link rel='stylesheet' " \
                                    "href='https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css'>" \
                                    "</head><body><div id='white'><div id='button'><img src='button.webp' " \
                                    "id='one'></div><div id='dno'><img src='dno.webp' id='two'>" \
                                    "</div></div><script src='main.js'></script><p>"

            for x in range(randint(50, 550)):
                ch = choice(["form", "marque", "tag", "tag", "tag", "tag", "image", "image", "image", "image"])
                if ch == "tag":
                    tag = choice(tags)
                    module = "<" + tag + " " + genstyle() + " class='{}'>".format(choice(
                        "animated shake infinite,trololo anim0,animated bounce infinite,animeted fadeIn "
                        "infinite,animated jello infinite,animated flip infinite".split(
                            ","))) + genshitpost() + "</" + tag + ">"
                    if choice([True, False]):
                        module = "<font color='" + choice(
                            "red,black,yellow,brown,blue,green,gray".split(",")) + "'>" + module + "</font>"
                    html += module
                if ch == "form":
                    html += typical_form.format(genshitpost(), genshitpost(), genshitpost(), genshitpost(),
                                                genshitpost())
                if ch == "marque":
                    html += createmarque()
                if ch == "image":
                    div_id = randint(0, 999999)
                    html += f'<img class="anim{randint(0, 3)}" id="{div_id}"></img><script>(async () => ' + '{'\
                            + f'document.getElementById("{div_id}").src = ' \
                              f'"{choice(imgSearch.fetch(choice(search_keywords)))}"' + '})()</script>'
            html += "</p></body></html>"
            self.wfile.write(html.encode('utf-8'))
        else:
            SimpleHTTPRequestHandler.do_GET(self)


PORT = int(getenv('PORT') or 12345)
httpd = HTTPServer(('0.0.0.0', PORT), Handler)
print(f'Открывай в браузере http://127.0.0.1:{PORT}')
httpd.serve_forever()
