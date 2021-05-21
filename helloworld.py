# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:49:07 2021

Test and document creation of a github project

@author: e4hgurge
"""
import os, time,datetime,sys
stf="%d%b%y"
sep=" --- "

def getday(y,m,d):
    """
        Call with ``y`` (year), ``m`` (month), and ``d`` (day). The 
        returned value is a date string ending with a separator.

        **Example**
            >>> getday(2021,5,21)
            >>> "20May21 --- "

    """
    return datetime.datetime(y,m,d).strftime(stf)+sep 

#
t=getday(2021,5,20)
print(t+"New Folder: H:\My Documents\git\helloworld")
print(t+"'git init': Initialise empty git repository")
print(t+"Create README.md using a text editor")
print(t+"'git add README.md' : Stage the README file")
print(t+"Create a file PRIVATE.txt as a file to be ignored")
print(t+"Create '.gitignore' using a text editor with 'PRIVATE.txt' on its first line")
print(t+"'git status' to confirm that 'git' ignores PRIVATE.txt")
print(t+"'git add .gitignore' : Stage the file '.gitignore'")
print(t+"'git commit -am \"First Commit\"")
print(t+"Login to github and create a new empty repository on 'github.com' named 'helloworld'.")
print(t+"\ngit remote add origin https://github.com/Gurgenci/helloworld.git (needs local git credential to have been set before)\
\ngit branch -M main\ngit push -u origin main")
print(t+"Start VS Code on 'helloworld' folder and start a terminal (windows powershell)")
print(t+"'mkdir docs'   The docs folder will contain all documentation.")
print(t+"'cd docs'  --> we are now in 'H:\My Documents\git\helloworld\docs'")
print(t+"pip install sphinx (unless you already have done so)")
print(t+"'sphinx-quickstart' and then answer questions:\n\
> Separate source and build directories (y/n) [n] : y\n\
> Project name: helloworld\n> Author name(s) : Hal Gurgenci\n\
> Project release []: May 2021\n\
> Project language [en]: \n\
This creates an initial directory structure")
print(t+"Edit 'conf.py' in 'docs\source' folder as follows:")
print("\textensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest','sphinx.ext.mathjax',\
'sphinx.ext.viewcode']")
print(t+"'./make html' : To create a scaffold to hold all documentation")
print(t+"Edit 'index.rst' and set the title to 'Helloworld as a tutorial for github documentation'")
print(t+"Create the LICENSE.rst file in 'docs' folder with my one-line title and MIT License text")
print(t+"Ornamental changes to index.rst")
#
t=datetime.datetime(2021,5,21).strftime(stf)+sep 
print(t+"Create 'api.tst' in 'docs' folder.  It includes:\n\
helloworld API reference\n\
========================\n\
\n\
.. automodule:: helloworld\n\
    :members:\n\
")
print(t+"Add 'api.rst' to the toctree in 'index.rst'.  'a' should align with the letter 't' of 'toctree'")
print(t+"Add the 'helloworld.py' path to 'conf.py' so that sphinx can find it:\n\
\tsys.path.insert(0, os.path.abspath('..\\..'))")
print(t+"'git add docs'")
print(t+"'git commit -am 'adding the first commit with documentation'")
