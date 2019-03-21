  
# Author:    Hades.y2k
# Version:   1.0
# Date:      11/05/2015
# License:   <OpenSource GPL>

w  = '\033[0m'  
 
r  = '\033[31m'
 
o  = '\033[33m'
 
b  = '\033[34m'
 
import sys
import httplib
import socket
import time
import httplib
import os
 
def slowprint(s):
 
    for c in s + '\n':
 
        sys.stdout.write(c)
 
        sys.stdout.flush()
 
        time.sleep(8./90)
 
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

ztack = """
 \033[97m####################################################################
\033[97m|\033[95m*** Admin Panel Finder ***
\033[97m|\033[96mAuthor : \033[94mStar  
\033[97m|\033[97m\033[93mShootz : \033[98mSunda Cyber Army\033[00m   
\033[97m|\033[92mNote : Jika TidaK Ketemu Disarankan Untuk \n\033[97m|\033[92mMenganti/merubah Page Admin List Yg Tersedia\033[97m
|\033[97m####################################################################\033[00m
"""
# Real Fun Start Here!
print ""   
print ztack
print "\033[00m"
print "contoh : \033[93mwww.SCA.co.id " 
site = raw_input("Enter : \033[95m ")
print "\033[00m"
site = site.replace("http://","")
targetnya = "http://'site'"
conn = httplib.HTTPConnection(site)
conn.connect()
print (' work begin \033[96m' + site + ' ...\n\n')
print "\033[00m"
lolox = "link.txt"
pg = open("lolox", "r")
lists = explode("\r\n", baca)
ukuran = filesize(lolox)
baca = read(pg, ukuran)
log = (targetnya, lists)
try:
        for admin in pg:
        admin = admin.replace('\n\n','')
        star = '/' + admin
        hae = httplib.HTTPConnection(site)
        F.request('GET', star)
        OhYeah = F.getresponse()
        print '%s %s %s' % (admin, mtucxdz.status, mtucxdz.reason)
        if OhYeah.status == 200:
                       print "\033[98mMencoba : \033[00m%s => \033[92mDitemukan\033[00m",str(log) 
        else:
            print"Mencoba : %s => tidak di temukan",str(log) 
