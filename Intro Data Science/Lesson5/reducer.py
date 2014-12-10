import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    aadhaar_generated = 0
    old_key = None

    for line in sys.stdin:
        data =  line.strip().split("\t")

        if len(data) != 2:
            continue
        this_key, count = data

        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, aadhaar_generated)
            aadhaar_generated = 0
        old_key = this_key
        aadhaar_generated += float(count)
    if old_key != None:
        print "{0}\t{1}".format(old_key, aadhaar_generated)


reducer()
