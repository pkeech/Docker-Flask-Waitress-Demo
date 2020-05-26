## IMPORT MODULES
from app import create_app
from waitress import serve
from paste.translogger import TransLogger

## START FLASK APPLICATION WITH WAITRESS
if __name__ == "__main__":
    app = create_app()
    serve(TransLogger(app), listen='*:80')