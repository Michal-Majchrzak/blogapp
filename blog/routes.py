from blog import app


@app.route('/')
def print_hello():
    return 'Hello World!'
