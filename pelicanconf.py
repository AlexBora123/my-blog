# 1. Add a basic theme so Pelican doesn't get confused
THEME = 'notmyidea' 

# 2. Set your new URL (the one we picked earlier)
SITEURL = 'https://spiralofcode.vercel.app'

# 3. Make sure this is False for production
RELATIVE_URLS = False

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME_TEMPLATES_OVERRIDES = ['templates']

DEFAULT_PAGINATION = 10

CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
