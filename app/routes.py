from flask import Blueprint, render_template, url_for, redirect, request, flash
from app.models import User, db
from flask_login import login_user, login_required, logout_user

# Define el blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Página de inicio"""
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    """Vista para iniciar sesión"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Busca el usuario por el nombre de usuario
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Usa el método check_password
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    """Cierra sesión del usuario"""
    logout_user()
    flash('Has cerrado sesión exitosamente', 'success')
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    """Vista para registrarse"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Verifica si el usuario ya existe
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('El nombre de usuario o correo electrónico ya están registrados', 'warning')
            return redirect(url_for('main.register'))

        # Crea un nuevo usuario con contraseña hasheada
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Usa el método set_password para el hash
        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso, ahora puedes iniciar sesión', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')
