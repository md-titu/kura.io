#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kura'
SITENAME = u'kura.io'
SITEURL = 'https://kura.io'

THEME = 'kura.io'
TIMEZONE = 'Europe/London'

GITHUB_URL = 'https://github.com/kura'
TWITTER_URL = 'https://twitter.com/kuramanga'
GOOGLE_ANALYTICS = 'UA-12479444-1'
DISQUS_SITENAME = "syslogtv"

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = u'en'

MENUITEMS = ()

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'c/{slug}'
CATEGORY_SAVE_AS = 'c/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 't/{slug}'
TAG_SAVE_AS = 't/{slug}/index.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

STATIC_PATHS = ['images', 'files', 'slides', 'extra/robots.txt',
                'extra/favicon.ico', ]

EXTRA_PATH_METADATA = {
    'files': {'path': 'files'},
    'images': {'path': 'images'},
    'slides': {'path': 'slides'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',
                     '404'))

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATH = "plugins/"
PLUGINS = [
    # ...
    'assets',
    'pelican_gist',
    'archive_unique_dates',
    'sitemap',
    # 'gzip_cache',
    'pelican_vimeo',
    'pelican_youtube',
    'tipue_search',
    # 'pdf',
    # ...
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily',
    }
}
