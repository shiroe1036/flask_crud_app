from flask import request, redirect, Blueprint, render_template, url_for
from demo.models import Film
from index import db

film_bp = Blueprint('film', __name__, template_folder='templates', url_prefix='/film')

@film_bp.route('/', methods=['GET'])
def index():
    films = Film.query.order_by(Film.id.desc()).all()
    
    return render_template('film/index.html', films=films)

@film_bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        film = Film(name=request.form['name'], coming_out=request.form['coming_out'])
        
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('film.index'))

    return render_template('film/create.html')

@film_bp.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    film = get_film(id)
    
    if request.method == 'POST':
        name = request.form['name']
        coming_out = request.form['coming_out']
    
        film.name = name
        film.coming_out = coming_out
        
        db.session.commit()
        return redirect(url_for('film.index'))
    
    return render_template('film/edit.html', film=film)

@film_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    film = get_film(id)
    
    db.session.delete(film)
    db.session.commit()
    
    return redirect(url_for('film.index'))

def get_film(idFilm):
    film = Film.query.filter_by(id=idFilm).first_or_404()
    return film