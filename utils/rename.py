import glob
import html
import os

for file in glob.glob('clawed/*'):
    file_esc = html.unescape(file)
    if file != file_esc:
        os.rename(file, file_esc)
