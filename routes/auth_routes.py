from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash, session

from models import db
from models.user import User


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if len(username) < 3:
            flash('Username too short.', 'danger')
            return redirect(url_for('auth.register'))

        if len(password) < 4:
            flash('Password too short.', 'danger')
            return redirect(url_for('auth.register'))

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('auth.register'))
        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Register successful.', 'success')

        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username

            flash('Login successful.', 'success')

            return redirect(url_for('dashboard.dashboard'))

        flash('Invalid credentials.', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out.', 'info')

    return redirect(url_for('auth.login'))