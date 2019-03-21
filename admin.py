 #!/usr/bin/env python
# -*- coding: UTF-8 -*-

ztack = """
 \033[97m#####################################
\033[97m|\033[95m*** Admin Panel Finder ***
\033[97m|\033[96mAuthor : \033[94mStar  
\033[97m|\033[97m\033[93mShootz : \033[98mSunda Cyber Army\033[00m   
\033[97m|\033[92mNote : Jika TidaK Ketemu Disarankan Untuk \n\033[97m|\033[92mMenganti/merubah Page Admin List Yg Tersedia\033[97m
|\033[97m#####################################\033[00m
"""
	
import datetime
from urllib2 import Request, urlopen, URLError, HTTPError, os, sys, time 

os.system("clear")
def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	print
	print ztack
	print
	print "Example : \033[93msca.id\033[00m or \033[93mwww.sca.id"
	print "\033[00m"
try:
	print bcolors.YELLOW + "\n\t[*] Checking the website " +  site + bcolors.ENDC
  print bcolors.YELLOW + "\t[*] Scanning: " + site + bcolors.ENDC + "\n"
            

            # This will Loop through Word List to get Admin Page
            wordfile = open("link.txt", "r")
            wordlist = wordfile.readlines()

            for word in wordlist:
                admin = word.strip("\n")
                admin = "/" + admin
                target = site + wordlist
                print bcolors.YELLOW + "[*] Checking: " + target + bcolors.ENDC
                connection = httplib.HTTPConnection(site)
                connection.request("GET", admin)
                response = connection.getresponse()


                # Deciding the Response Status and Print out the result!....
                if response.status == 200:
                    print bcolors.GREEN + "\n\n\t+------------------------------------------------------+" + bcolors.ENDC
                    print "%s %s" % (bcolors.GREEN + "\t[!] Admin Page Found >> " + bcolors.ENDC, bcolors.GREEN + target + bcolors.ENDC)
                    print bcolors.GREEN + "\t+------------------------------------------------------+\n" + bcolors.ENDC
                    raw_input(bcolors.YELLOW + "[*] Press enter to continue.\n" + bcolors.ENDC)

                elif response.status == 302:
                    print bcolors.RED + "[!] 302 Object moved temporarily.\n" + bcolors.ENDC

                elif response.status == 404:
                    print bcolors.RED + "[!] 404 Web Page Not Found.\n" + bcolors.ENDC

                elif response.status == 410:
                    print bcolors.RED + "[!] 410 Object removed permanently.\n" + bcolors.ENDC
                
                else:
                    print "%s %s %s %s" % (bcolors.RED + "Unknown Response: " + bcolors.ENDC, bcolors.RED + response.status + bcolors.ENDC, "\n", bcolors.RED + host + bcolors.ENDC)
                connection.close() # After fun jobs, we are closing connection.

        except (httplib.HTTPResponse, socket.error):
            print bcolors.RED + "\n\t[!] Session Cancelled, An Error Occured." + bcolors.ENDC
            print bcolors.RED + "\t[!] Check Your Internet Connection" + bcolors.ENDC
        except (KeyboardInterrupt, SystemExit):
            print bcolors.RED + "\t[!] Session Interrupted and Cancelled." + bcolors.ENDC

findAdmin()
