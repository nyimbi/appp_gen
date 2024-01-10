"""
ATS common config module.

Created on 2019-3-3.
author: chenwen9.
"""

import imp
import os
from flask_appbuilder.security.manager import AUTH_LDAP

basedir = os.path.abspath(os.path.dirname(__file__))
from datetime import timedelta

version = imp.load_source('version', os.path.join(basedir, 'version.py'))
try:
    config_local = imp.load_source('config_local', os.path.join(basedir, 'config_local.py'))
except Exception:
    config_local = None


class config(object):
    """app common config class."""
    # Your App secret key
    SECRET_KEY = '89f861a04932329b77613bc2f7db7b73704e66d7'
    # SERVER_NAME = 'localhost:8000'
    # The SQLAlchemy connection string.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_POOL_PRE_PING = False
    SQLALCHEMY_ECHO = False
    # Flask-WTF flag for CSRF
    CSRF_ENABLED = True
    #------------------------------
    # GLOBALS FOR APP Builder
    #------------------------------
    # Uncomment to setup Your App name
    #----app running mode
    APP_MODE = 'DEV'
    APP_NAME = version.APP_NAME
    APP_VERSION = '%s:%s' % (APP_MODE, version.VERSION_STRING)
    APP_DESC = version.DESCRIPTION
    APP_AUTHOR = version.AUTHOR_NAME
    # Uncomment to setup Setup an App icon
    # APP_ICON = "static/img/logo.jpg"

    #----------------------------------------------------
    # AUTHENTICATION CONFIG
    #----------------------------------------------------
    # The authentication type
    # AUTH_OID : Is for OpenID
    # AUTH_DB : Is for database (username/password()
    # AUTH_LDAP : Is for LDAP
    # AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
    AUTH_TYPE = AUTH_LDAP

    # Uncomment to setup Full admin role name
    AUTH_ROLE_ADMIN = 'Admin'

    # Uncomment to setup Public role name, no authentication needed
    AUTH_ROLE_PUBLIC = 'Public'

    # Will allow user self registration
#     AUTH_USER_REGISTRATION = False #default is false

    # The default user self registration role
    # AUTH_USER_REGISTRATION_ROLE = "Public"

    # When using LDAP Auth, setup the ldap server
    AUTH_LDAP_SERVER = 'ldap://your-ldap-server:389/'
    AUTH_LDAP_SEARCH = 'ou=people,ou=intranet,dc=motorola,dc=com'
    AUTH_LDAP_EMAIL_FIELD = 'mail'
    AUTH_LDAP_UID_FIELD = 'motguid'
    AUTH_LDAP_FIRSTNAME_FIELD = 'givenName'
    AUTH_LDAP_LASTNAME_FIELD = 'sn'
    AUTH_USER_REGISTRATION = True
    AUTH_USER_REGISTRATION_ROLE = AUTH_ROLE_PUBLIC

    # Uncomment to setup OpenID providers example for OpenID authentication
    # OPENID_PROVIDERS = [
    #    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    #    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    #    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    #    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    #---------------------------------------------------
    # Babel config for translations
    #---------------------------------------------------
    # Setup default language
    BABEL_DEFAULT_LOCALE = 'en'
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = 'translations'
    # The allowed translation for you app
    LANGUAGES = {
        'en': {'flag':'gb', 'name':'English'},
        'pt': {'flag':'pt', 'name':'Portuguese'},
        'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
        'es': {'flag':'es', 'name':'Spanish'},
        'de': {'flag':'de', 'name':'German'},
        'zh': {'flag':'cn', 'name':'Chinese'},
        'ru': {'flag':'ru', 'name':'Russian'},
        'pl': {'flag':'pl', 'name':'Polish'}
    }
    #---------------------------------------------------
    # Image and file configuration
    #---------------------------------------------------
    # The file upload folder, when using models with files
    UPLOAD_FOLDER = os.getcwd() + '/app/static/uploads/'

    # The image upload folder, when using models with images
    IMG_UPLOAD_FOLDER = os.getcwd() + '/app/static/uploads/'

    # The image upload url, when using models with images
    IMG_UPLOAD_URL = '/static/uploads/'
    # Setup image size default is (300, 200, True)
    # IMG_SIZE = (300, 200, True)

    # Theme configuration
    # these are located on static/appbuilder/css/themes
    # you can create your own and easily use them placing them on the same dir structure to override
    # APP_THEME = "bootstrap-theme.css"  # default bootstrap
    # APP_THEME = "cerulean.css"
    # APP_THEME = "amelia.css"
    # APP_THEME = "cosmo.css"
    # APP_THEME = "cyborg.css"
    # APP_THEME = "flatly.css"
    # APP_THEME = "journal.css"
    # APP_THEME = "readable.css"
    # APP_THEME = "simplex.css"
    # APP_THEME = "slate.css"
    # APP_THEME = "spacelab.css"
    # APP_THEME = "united.css"
    # APP_THEME = "yeti.css"

    SESSION_COOKIE_NAME = "%s_session" % version.APP_NAME.lower()
    SESSION_KEY_PREFIX = "bsm"
    SESSION_TYPE = "filesystem"
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    FLASK_LOG_LEVEL = "DEBUG"
    LOG_LEVEL = "DEBUG"
    LOG_NAME = "fabadmin"
    FLASK_LOG_PATH = os.getcwd() + '/logs/fab_admin.log'

    #----addon manager register
    ADDON_MANAGERS = ['fab_addon_autodoc.manager.AutoDocManager']
    TEMPLATES_AUTO_RELOAD = True

    #----user type
    USER_TYPE_LOCAL = 'local'
    USER_TYPE_LDAP = 'ldap'
    #----common permissions
    COMMON_PERMISSIONS = ['userapikey']
    COMMON_LOCAL_USER_PERMISSION = ['userinfoedit', 'resetmypassword']
    COMMON_LOCAL_USER_VIEW = ['UserInfoEditView', 'ResetMyPasswordView']

    #---config center config items
    REDISSN = 'mymaster'
    REDISPASS = os.environ.get('REDIS_PASSWORD', config_local.REDISPASS if config_local else None)
    REDIS_URL = os.environ.get('REDIS_URL', "redis+sentinel://:{0}@localhost:26379/{1}/0".format(REDISPASS, REDISSN))
    REDIS_DECODE_RESPONSES = True
    CRED_CENTER_URL = os.environ.get('CRED_CENTER_URL', \
                                     "redis+sentinel://:{0}@localhost:26379/{1}/1".format(REDISPASS, REDISSN))
    CRED_CENTER_DECODE_RESPONSES = True
    #---security cleanup  would auto sync security data from code to DB
    SECURITY_CLEANUP = True
    AUTO_UPDATE_PERM = os.environ.get('AUTO_UPDATE_PERM', True)
    #---SPOOLER path
    SPOOLER_PATH = "/fabadmin/logs/spooler"

    # RQ
    RQ_REDIS_URL = os.environ.get('RQ_REDIS_URL', \
                                  "redis+sentinel://:{0}@localhost:26379/{1}/2".format(REDISPASS, REDISSN))
    RQ_DASHBOARD_REDIS_SENTINELS = 'localhost:26379'
    RQ_DASHBOARD_REDIS_MASTER_NAME = 'mymaster'
    RQ_DASHBOARD_REDIS_PASSWORD = REDISPASS
    RQ_DASHBOARD_REDIS_DB = '2'
    RQ_DASHBOARD_POLL_INTERVAL = 2500  # : Web interface poll period for updates in ms
    DEBUG = False  # RQ dashboard module debug config
    RQ_DASHBOARD_WEB_BACKGROUND = "black"
    RQ_DASHBOARD_DELETE_JOBS = False
    # rq scheduler dashboard
    RQ_SCHEDULER_DASHBOARD_REDIS_SENTINELS = RQ_DASHBOARD_REDIS_SENTINELS
    RQ_SCHEDULER_DASHBOARD_REDIS_MASTER_NAME = RQ_DASHBOARD_REDIS_MASTER_NAME
    RQ_SCHEDULER_DASHBOARD_REDIS_PASSWORD = REDISPASS
    RQ_SCHEDULER_DASHBOARD_REDIS_DB = '2'
    RQ_POLL_INTERVAL = 2500  # : Web interface poll period for updates in ms
    # Redis cache for fab_auth
    FAB_AUTH_REDIS_CACHE = True
    FAB_AUTH_REDIS_CACHE_SCOPE = 'REST'  # 'ALL=all kinds request|REST=RESTFul request via basic auth or RESTAPI'
    FAB_AUTH_REDIS_RPV_KEY = "fab:rpv"
    FAB_AUTH_REDIS_UAPIK_KEY = "fab:uapik"
    FAB_AUTH_KEY_REPLACE_PATTERN = r"['|\"]"