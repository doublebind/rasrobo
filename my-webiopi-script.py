import webiopi
import os
import urllib.parse  # python3
#import urllib       # python2

@webiopi.macro
def jtalk(text):
        #text_decode = urllib.unquote(text)    #python2
        text_decode = urllib.parse.unquote(text)    #python3
        os.system("/home/pi/jtalk.sh " + text_decode)
