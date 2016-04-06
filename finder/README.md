ftpFinder
==============
This python script identifies websites with publicly accessible ```sftp-config.json``` files.

#Usage

```
> python ftpfinder.py -h
usage: ftpfinder.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-t THREADS]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        input file
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        output file
  -t THREADS, --threads THREADS
                        threads
```

The input file should contain the targets one per line. 
The script will output discovered domains in the form of ```[*] Found: DOMAIN``` to stdout. 
