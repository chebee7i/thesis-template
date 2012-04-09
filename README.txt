
PhD Thesis @ University of California, Davis
============================================



Usage
-----

(1) Enter the correct user variables in the file:

        settings/phdsetup.tex, 
        
    such as the dissertation title and author name.

(2) To compile the entire dissertation, compile the file dissertation.tex.
    For example:
    
        cd dissertation
        pdflatex disseration.tex
    

(3) To compile the required standalone one-page abstract, compile the file
    pqil-abstract.tex. For example,
    
        cd abstract
        pdflatex pqil-abstract.tex



Optional Usage
--------------

* To compile any of the preliminary sections, such as the acknowledgements, 
  compile the file. For example:
  
        cd prelim
        pdflatex acknowledgments.tex
        
  The page numbers will be in the correct format, but will always start from 1 
  when compiling each section individually.

* To compile individual chapters, compile the file ./chapter#/chapter#.tex. 
  For example:

        cd chapter1
        pdflatex chapter1.tex
        
  This will include the bibliography at the end so that the references are 
  correct. The chapter and page numbers will always start from 1 when compiling
  individual chapters, but will be correctly numbered when compiling the entire
  dissertation.



Figures
-------

When inserting images as figures, be sure to reference the file correctly, 
or dissertation.tex will not properly compile. Since all files are compiled
within a subdirectory, a correct reference will relatively enter the root
directory and then redescend back to the image file. For example:

    \begin{figure}
    \centering
    \includegraphics[width=5in,height=3.5in]{../chapter1/blorp.eps}
    \caption{Example figure.}
    \label{fig:example}
    \end{figure}

Referencing the figure as "../chapter1/blorp.eps" allows both chapter1.tex 
and dissertation.tex find your file. 

The package "epstopdf" will take care of converting your *.eps files to *.pdf 
files for proper viewing.



Customization
-------------

To add additional chapters, create a folder "chapter#" with the 
file "chapter#.tex" as follows:

    \input{../settings/boilerplate}

    \chapter{Chapter Name}
    Text.

    \input{../settings/boilerplate}

Then, in the file ./dissertation/dissertation.tex, add the line:

    \input{../chapter#/chapter#}


