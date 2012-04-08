# Intro

Migrate a SemanticScuttle export file to a compatible [shaarli](http://sebsauvage.net/wiki/doku.php?id=php:shaarli "Visit official Shaarli website") import file.

# Requirements

- [BeautifulSoup4 for Python](http://www.crummy.com/software/BeautifulSoup/ "Visit official BeautifulSoup website") python-beautifulsoup package in Ubuntu 11.10
- lxml for Pythonn, python-lxml package in Ubuntu 11.10

# Configuration

In SemanticScuttle2Shaarli.py file, just edit this line:

    sourcefile = ''

with the name of the file you export from SemanticScuttle.

# Use it in 3 steps

Step 1: go to your SemanticScuttle profile and click on "Export Bookmarks in HTML". Save file to your SemanticScuttle2Shaarli directory as "mylinks.html"

Step 2: launch SemanticScuttle2Shaarli.py script in a shell

    python SemanticScuttle2Shaarli.py

Step 3: go to your Shaarli website and go to Tools > Import, then choose "to_shaarli.html" that appears in your SemanticScuttle2Shaarli directory.

Enjoy !

# Flattr this

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=blankoworld&url=https://github.com/blankoworld/SemanticScuttle2Shaarli&title=SemanticScuttle2Shaarli&language=french&tags=github&category=software "Flattr this repository!")

# Troubleshooting

Please see @ contact chapter

# Contact

I'm available here : <blankoworld@wanadoo.fr>

