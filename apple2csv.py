#!/usr/bin/env python3

from os import listdir
from os.path import isfile, isdir, join, basename

import re
import sys

from bs4 import BeautifulSoup

import csv

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def clean_line(s):
    return s.replace("\r", "").replace("\n", "").replace(u'\ufeff', '')

if len(sys.argv) == 1:
    print('Missing path to a day of unziped apple daily htmls.')
    print('Please unzip apple-articles-plaintext-20020101-20210620.zip and provide the path to the <data>/<date> folder.') 
    exit(-1)

data_path = sys.argv[1]

folder_name = basename(data_path)
if not re.match('20\d{6}', folder_name):
    print('Please unzip apple-articles-plaintext-20020101-20210620.zip and provide the path to the <data>/<date> folder.') 
    print('Provided path:', folder_name)
    exit(-1)

# daily_paths = [join(data_path, f) for f in listdir(data_path) if isdir(join(data_path, f))]

daily_paths = []
directory_index_path = data_path + '/index.html'
with open(directory_index_path) as f:
    directory_index_string = f.read()
article_soup = BeautifulSoup(directory_index_string, 'html.parser')

for link in article_soup.find_all('a'):
    link_target = link.get('href')
    if link_target.endswith('index.html'):
        folder = link_target.split('/')[0]
        daily_paths.append(join(data_path, folder))
    else:
        eprint('Unknown link tag:', link)

if len(sys.argv) == 2:
    eprint('Missing output path.')
    exit(-1)

output_path = sys.argv[2] + '/' + folder_name + '.csv'

id = 0
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    if len(daily_paths) > 0:
        csvwriter.writerow(['key', 'date', 'article_daily_id', 'title', 'text'])

    for daily_path in daily_paths:
        try:
            html_path = daily_path + '/index.html'
            if not isfile(html_path):
                eprint('File is not an html:', html_path)
                continue
            
            with open(html_path) as f:
                html_string = f.read()
            
            article_soup = BeautifulSoup(html_string, 'html.parser')

            date = folder_name
            title = clean_line(article_soup.title.text)

            for data in article_soup(['title']):
                data.decompose()
            
            text = clean_line(' '.join(article_soup.strings))

            key = date + '-' + str(id)

            csvwriter.writerow([key, date, id, title, text])
        except Exception as ex:
            eprint("Error parsing", daily_path , ex)
        id += 1

print('Created', output_path)
