# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:49:07 2021

Test and document creation of a github project

@author: e4hgurge
"""
import datetime
stf="%d%b%y"
sep=" --- "

logfilename="gitlog.txt"
logactions=False
printactions=True

if logactions:
    logfile=open(logfilename,"w")

def getday(y,m,d):
    """
        Call with ``y`` (year), ``m`` (month), and ``d`` (day). The 
        returned value is a date string ending with a separator.

        **Example**
            >>> getday(2021,5,21)
            >>> "20May21 --- "

    """
    return datetime.datetime(y,m,d).strftime(stf)+sep 

def la(s):
    if printactions:
        print(s)
    if logactions:
        logfile.write(s+"\n")
        

#
t=getday(2021,5,20)
la(t+"New Folder: H:\My Documents\git\helloworld")
la(t+"'git init': Initialise empty git repository")
la(t+"Create README.md using a text editor")
la(t+"'git add README.md' : Stage the README file")
la(t+"Create a file PRIVATE.txt as a file to be ignored")
la(t+"Create '.gitignore' using a text editor with 'PRIVATE.txt' on its first line")
la(t+"'git status' to confirm that 'git' ignores PRIVATE.txt")
la(t+"'git add .gitignore' : Stage the file '.gitignore'")
la(t+"'git commit -am \"First Commit\"")
la(t+"Login to github and create a new empty repository on 'github.com' named 'helloworld'.")
la(t+"\ngit remote add origin https://github.com/Gurgenci/helloworld.git (needs local git credential to have been set before)\
\ngit branch -M main\ngit push -u origin main")
la(t+"Start VS Code on 'helloworld' folder and start a terminal (windows powershell)")
la(t+"'mkdir docs'   The docs folder will contain all documentation.")
la(t+"'cd docs'  --> we are now in 'H:\My Documents\git\helloworld\docs'")
la(t+"pip install sphinx (unless you already have done so)")
la(t+"'sphinx-quickstart' and then answer questions:\n\
> Separate source and build directories (y/n) [n] : y\n\
> Project name: helloworld\n> Author name(s) : Hal Gurgenci\n\
> Project release []: May 2021\n\
> Project language [en]: \n\
This creates an initial directory structure")
la(t+"Edit 'conf.py' in 'docs\source' folder as follows:")
la("\textensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest','sphinx.ext.mathjax',\
'sphinx.ext.viewcode']")
la(t+"'./make html' : To create a scaffold to hold all documentation")
la(t+"Edit 'index.rst' and set the title to 'Helloworld as a tutorial for github documentation'")
la(t+"Create the LICENSE.rst file in 'docs' folder with my one-line title and MIT License text")
la(t+"Ornamental changes to index.rst")
#
t=datetime.datetime(2021,5,21).strftime(stf)+sep 
la(t+"Create 'api.tst' in 'docs' folder.  It includes:\n\
helloworld API reference\n\
========================\n\
\n\
.. automodule:: helloworld\n\
    :members:\n\
")
la(t+"Add 'api.rst' to the toctree in 'index.rst'.  'a' should align with the letter 't' of 'toctree'")
la(t+"Add the 'helloworld.py' path to 'conf.py' so that sphinx can find it:\n\
\tsys.path.insert(0, os.path.abspath('..\\..'))")
la(t+"'git add docs'")
la(t+"'git commit -am 'adding the first commit with documentation'")
la(t+"'git push origin main")
la(t+"Go to 'https://readthedocs.org/' and register if you do not have an account")
la(t+"Import a project and pick 'helloworld' from github to import\n\
\tReadTheDocs did not accept helloworld as a suitable project name so I entered 'HelloWorldDocumentation'\n\
\tas the name of the project in 'ReadTheDocs'.  It does not have to be same name as in 'github'.")
la(t+"Build the document using the latest github version")
la(t+"This creates the web page 'https://helloworlddocumentation.readthedocs.io/en/latest/'")
la("I add this address to README.md and this concludes the documentation")
#
#
if logactions:
    logfile.close()

