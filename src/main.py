"""
main.py

Primary App Engine app handler

"""

import logging
import sys, os

# Workaround for httplib2 bug.
# http://code.google.com/p/googleappengine/issues/detail?id=5064
sys.modules['ssl'] = None

package_dir = "packages"
sys.path.insert(0, package_dir)

# Allow unzipped packages to be imported
# from packages folder

# Append zip archives to path for zipimport

for filename in os.listdir(package_dir):
    if filename.endswith((".zip", ".egg")):
        sys.path.insert(0, "%s/%s" % (package_dir, filename))



from wsgiref.handlers import CGIHandler

from application.settings import DEBUG_MODE
from application.app import app


def main():
    if DEBUG_MODE:
        # Run debugged app
        logging.getLogger().setLevel(logging.DEBUG)
        from werkzeug_debugger_appengine import get_debugged_app
        app.debug=True
        debugged_app = get_debugged_app(app)
        CGIHandler().run(debugged_app)
    else:
        # Run production app
        from google.appengine.ext.webapp.util import run_wsgi_app
        run_wsgi_app(app)


# Use App Engine app caching
if __name__ == "__main__":
    main()

