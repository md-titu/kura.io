#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kura'
SITENAME = 'kura.io'
SITEURL = 'https://kura.io'

THEME = 'eevee'
THEME_PRIMARY = 'indigo'
THEME_ACCENT = 'pink'

TIMEZONE = 'Europe/London'

TWITTER_USERNAME = 'kuramanga'
DISQUS_SITENAME = "syslogtv"

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%d %b %Y'

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT
}

MENUITEMS = (('Contact', '/contact/'), ('Software', '/software/'),
             ('Donate', '/donate/'),
             ('.onion', 'http://omgkuraio276g5wo.onion/'))
SOCIAL = (('Github', 'https://github.com/kura'),
          ('Twitter', 'https://twitter.com/kuramanga'),
          ('Keybase', 'https://keybase.io/kura'))
LINKS = (('blackhole.io', 'https://blackhole.io'),
         ('Yarg', 'https://kura.io/yarg'),
         ('Eevee', 'https://kura.io/eevee'),
         ('Hauntr', 'https://kura.io/hauntr'),
         ('Ghastly', 'https://kura.io/ghastly'),)
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'c/{slug}'
CATEGORY_SAVE_AS = 'c/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 't/{slug}'
TAG_SAVE_AS = 't/{slug}/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

SUMMARY_MAX_LENGTH = 150

STATIC_PATHS = ['images', 'files', 'slides', 'extra/robots.txt',
                'extra/favicon.ico', ]

EXTRA_PATH_METADATA = {
    'files': {'path': 'files'},
    'images': {'path': 'images'},
    'slides': {'path': 'slides'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = (('index', 'archives', '404'))

# Blogroll
# LINKS = ()
#
# Social widget
# SOCIAL = ()

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins/", ]
PLUGINS = [
    'assets',
    'extract_toc',
    'pelican_fontawesome',
    'pelican_gist',
    'pelican_vimeo',
    'pelican_youtube',
    'touch',
]

GIST_CACHE_ENABLED = False

USE_TWITTER_CARDS = True
USE_OPEN_GRAPH = True
