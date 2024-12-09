from app import create_app, db  # Importa la fábrica de la app y la instancia de la base de datos
from flask_migrate import upgrade

# Crea la aplicación utilizando la fábrica
app = create_app()

# Opción para inicializar datos de prueba
def seed_data():
    from app.models import User, Question  # Importa tus modelos
    admin_user = User(username="admin", email="admin@studentoverflow.com", password="admin123")
    sample_question = Question(title="¿Cómo configuro Flask?", body="Tengo problemas con mi app Flask.", user=admin_user)
    db.session.add(admin_user)
    db.session.add(sample_question)
    db.session.commit()

# Punto de entrada principal
if __name__ == "__main__":
    # Aplica migraciones al iniciar (opcional, útil en desarrollo)
    with app.app_context():
        upgrade()
        # seed_data()  # Descomentar si quieres llenar la base de datos con datos de prueba

    # Levanta la aplicación
    app.run(debug=True)
