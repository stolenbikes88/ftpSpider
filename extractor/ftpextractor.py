#!/usr/bin/python
import sys, os, argparse, urllib2,json
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

		# Check if refs/heads is in the file
		if('save_before_upload' in answer):
                    data = json.loads(answer)
		    # Write match to OUTPUTFILE
		    #fHandle = open(OUTPUTFILE,'a')
		    #fHandle.write(domain + ", sftp-config.json, "+req.headers.get('content-length')+"\n")
		    #fHandle.close()
		    #print("[*] Found config: " + domain)
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
