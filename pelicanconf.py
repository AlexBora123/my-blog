THEME = 'notmyidea' 

SITEURL = 'https://spiralofcode.vercel.app'

RELATIVE_URLS = False

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

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
