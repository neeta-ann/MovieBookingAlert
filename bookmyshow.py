#waiting for the ENDGAME!!!

import urllib.request,urllib.parse,urllib.error
import re
import ssl
import webbrowser
import time

url = 'https://in.bookmyshow.com/buytickets/spider-man-far-from-home-bengaluru/movie-bang-ET00106002-MT/20190813'
while True:
     req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
     con = urllib.request.urlopen( req )
     data = con.read()
     
     pattern = b'20190813'
     if re.search(pattern,data):     
          pattern1 = b'INOX: Garuda Mall, Magrath Road'
          
          if re.search(pattern1,data):
               #BOOK THE TICKETS NOW!!
               webbrowser.open('https://in.bookmyshow.com/buytickets/spider-man-far-from-home-bengaluru/movie-bang-ET00106002-MT/20190813')
               break
     else:
          print('waiting...')
          time.sleep(300) #sleeps for 5 minutes and checks again
