from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    # Render halaman utama
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Ambil data dari form
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validasi input
        if not username or not email or not password:
            flash('Harap isi semua kolom', 'error')
            return redirect(url_for('register'))

        # Cek apakah email sudah terdaftar
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email sudah terdaftar', 'error')
            return redirect(url_for('register'))

        # Hash password dan simpan user baru
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Tampilkan pesan sukses
        flash('Registrasi berhasil!', 'success')
        return redirect(url_for('home'))

    # Render halaman registrasi
    return render_template('register.html')

@app.route('/users')
def users():
    # Ambil semua data user
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        # Buat semua tabel di database
        db.create_all()
    # Jalankan aplikasi dalam mode debug
    app.run(debug=True)
