import sys
import webbrowser
import os
import pathlib
import requests
import json
import webbrowser


def joke():
    f = r"http://api.icndb.com/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)
    result = tt["value"]["joke"]
    sys.stdout = open('JokeForToday.html','w')

    print ("<html>")
    print ("<h1 style=text-align:center;color:red;font-size:90><b>CHUCK NORRIS RANDOM JOKE FOR THE DAY</b></h1>")
    print ("<p style=text-align:center;color:blue;font-size:60>%s</p>" % result)
    print ("</html>")
    webbrowser.get('firefox').open('JokeForToday.html', new=2)

joke()

