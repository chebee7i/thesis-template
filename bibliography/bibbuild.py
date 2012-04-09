"""
    Simple module to build a new sorted Bibtex file from cited works.
    
    Example: Build a new sorted bibtex file from cited works.
    
        $ python bibbuild.py ../chapter3/existing.bib `find ../ -name "*.tex"` > new.bib
        
"""
import sys

import citations
import bibextract

def main():
    try:
        bibfile = sys.argv[1]
        texfiles = sys.argv[2:]
    except IndexError:
        print "usage: python {0} BIBFILE TEXFILE1 [TEXFILE2] [...]".format(__file__)
        sys.exit(1)

    cited = sorted(citations.get_citations(texfiles))
    bibentries = bibextract.simple_parse(bibfile)
    entries = [bibentries[key] for key in cited]
    print '\n\n'.join(entries)
    
if __name__ == '__main__':
    main()
