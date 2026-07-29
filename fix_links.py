import os
import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace href="/" with href="./"
    content = content.replace('href="/"', 'href="./"')
    # Replace href="/#..." with href="./#..."
    content = content.replace('href="/#', 'href="./#')
    # Replace href="/pagename" with href="pagename"
    content = re.sub(r'href="/([a-zA-Z0-9_-]+)(#.*)?"', r'href="\1\2"', content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Updated links to be relative for GitHub Pages.")
