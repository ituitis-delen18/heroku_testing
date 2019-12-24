from bottle import Bottle, request, static_file

def index_page():
    return "Hello WOrld"

def create_app():
    app = Bottle()
    app.route("/", "GET", index_page)
    return app
application = create_app()
application.run(debug = True)
