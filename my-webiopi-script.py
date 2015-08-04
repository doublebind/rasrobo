import webiopi
import os
import urllib

@webiopi.macro
def jtalk(text):
        text_decode = urllib.unquote(text)
        os.system("/home/pi/jtalk.sh " + text_decode)
