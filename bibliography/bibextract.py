"""
    Simple module to extract bibentries from a bibfile into a dict.
    
    Example: Count entries in bibfile and save to pickle.
    
        $ python bibextract.py ../chapter3/existing.bib
    

"""

import re
import sys
import cPickle

regex = re.compile(r'{(\w+),')

def simple_parse(fn):
    entries = {}
    with open(fn) as fh:
        begin = False
        entry = []
        for line in fh.readlines():
            if line.startswith('@'):
                # new entry
                if begin:
                    # finish old entry
                    key = re.search(regex, entry[0])
                    if not key:
                        msg = "Could not find key for bibentry:\n{0}"
                        raise Exception(msg.format(entry[0]))
                    else:
                        key = key.groups()[0]
                    entries[key] = ''.join(entry).strip()
                    entry = []
                else:
                    begin = True
            entry.append(line)
    return entries

def main():
    fn = sys.argv[1]
    entries = simple_parse(fn)
    # save to file
    print len(entries)
    out = open('bibentries.pickle', 'wb')
    cPickle.dump(entries, out)

if __name__ == '__main__':
    main()
