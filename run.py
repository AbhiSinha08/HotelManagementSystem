# Only for development server
# To enable automatic reload with debugging

from app import app
from livereload import Server

if __name__ == '__main__':

    app.debug = True

    server = Server(app.wsgi_app)
    server.serve(port=5000)