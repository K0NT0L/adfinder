#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
from urllib2 import Request, urlopen, URLError, HTTPError, os, sys, time 

os.system("clear")
def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

def Credit():
      Space(5); print "\033[97m####################################"
      Space(5); print "\033[97m|\033[95m*** Admin Panel Finder ***"
      Space(5); print "\033[97m|\033[96mAuthor : \033[94mStar "
      Space(5); print "\033[97m|\033[97m\033[93mShootz : \033[98mSunda Cyber Army\033[00m"
      Space(5); print "\033[97m|\033[92mNote : Jika TidaK Ketemu Disarankan Untuk"
      Space(5); print "\033[97m|\033[92mMenganti/merubah Page Admin List Yg Tersedia\033[97m" 
      Space(5); print "|\033[97m#####################################\033[00m"

def findAdmin():
	f = open("link.txt","r");
	print
	print
	print "Example : \033[93mhttps://www.SCA.co.id\033[00m or \033[93mwww.SCA.co.id"
	print "\033[00m"
	f = open("link.txt","r");
	link = raw_input("Enter : \033[95m")
	print "\033[00m"
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link
Credit()
findAdmin()