#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SemanticScuttle2shaarli.py
#

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
# 
# Copyright (C) 2012 Olivier DOSSMANN 
#  <blankoworld@wanadoo.fr>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.

# Libraries
import sys
from BeautifulSoup import BeautifulSoup
import lxml.etree as ET

# Variables
sourcefile = 'mylinks.html'
targetfile = 'to_shaarli.html'

def main():
  """
  Extract data from 'sourcefile' and create 'targetfile' with all data:
  - title
  - description
  - creation date
  - tags
  """
  # Open source file
  try:
    f = open(sourcefile, 'rb')
  except IOError, e:
    print(e)
    return 1
  try:
    text = f.read()
  except ValueError, e:
    print(e)
    return 1
  finally:
    f.close()

  # Parse source file content
  soup = BeautifulSoup(text)
  links = soup.findAll('dt')
  html_links = []
  if not links:
    print("No links found!")
    return 0
  print("Process %s links…" % (len(links),))
  for num,link in enumerate(links):
    if not link.a:
      continue
    print("\t%s" % (num + 1))
    # Fetch data
    title = link.a.string or ''
    description = link.a.get('description', '')
    tags = link.a.get('tags', '')
    if tags == 'system:unfiled':
      tags = ''
    date = link.a.get('add_date', False)
    url = link.a.get('href', False)
    # Create HTML element
    print "HREF: %s, TAGS: %s" % (url, tags)
    a = ET.Element('A', {'HREF': str(url), 'ADD_DATE': str(date), 'PRIVATE': '0', 'TAGS': unicode(tags)})
    a.text = title
    html_links.append((a, description.encode('utf-8')))

  # Prepare target file start
  comment = ET.Comment("This is an automatically generated file.\n\
    It will be read and overwritten.\n\
    DO NOT EDIT!")
  meta = ET.Element('META', {'HTTP-EQUIV': "Content-Type", 'CONTENT': "text/html; charset=UTF-8"})
  element = ET.Element('TITLE', {})
  element.text = 'Bookmarks'

  # Write result
  try:
    t = open(targetfile, 'w')
  except IOError, e:
    print(e)
    return 1
  try:
    for tag in [comment, meta, element]:
      if tag == comment: 
        t.write(ET.tostring(tag, doctype='<!DOCTYPE NETSCAPE-Bookmark-file-1>') + '\n')
        continue
      t.write(ET.tostring(tag) + '\n')
    
    # Create bookmarks
    t.write('<DL>\n')
    for el in html_links:
      if len(el) >= 1:
        t.write("<DT>" + ET.tostring(el[0]) + '\n')
      if len(el) > 0 and el[1] != '':
        t.write("<DD>%s" % (el[1],) + '\n')
    t.write('</DL>')
  except ValueError, e:
    print(e)
    return 1
  finally:
    t.close()
  return 0

if __name__ == '__main__':
  sys.exit(main())
