"""
    Simple module to return a list of citation keys from a TeX document.
    
    Here was my use case:
    
        My thesis consisted of already published papers. I wanted a single
        bibliography, rather than one for each paper.  So, my task was to 
        construct a single .bib file containing all my references.
        
    Example: Determine how many unique citations are in chapter 1.
    
        $ python citations.py ../chapter1/chapter1.tex | wc -l
        32

    Example: Determine the unique citations in all chapters.
    
        $ python citations.py `find ../ -name "*.tex"`
        
"""

import os, sys
import re


def get_citations(fns):
    cited = set([])
    regex1 = re.compile(r'\cite{([0-9A-Za-z,]+)}')
    regex2 = re.compile(r'\cite\[.*?\]{([0-9A-Za-z,]+)}')
    for fn in fns:
        with open(fn) as fh:
            matches = re.findall(regex1, fh.read())
            for match in matches:
                cited.update(match.split(','))
            fh.seek(0)
            matches = re.findall(regex2, fh.read())
            for match in matches:
                cited.update(match.split(','))

    return cited

def main():
    try:
        fns = sys.argv[1:]
    except IndexError:
        print "usage: python {0} TEXFILE1 [TEXFILE2] [...]".format(__file__)
        sys.exit(1)

    cited = get_citations(fns)
    for key in sorted(cited):
        print key    
    
if __name__ == '__main__':
    main()
