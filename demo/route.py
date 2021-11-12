from index import app

@app.route('/test')
def hello_test():
    return 'Hello Test!'

from demo.Film import film_bp
app.register_blueprint(film_bp)