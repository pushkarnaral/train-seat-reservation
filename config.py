class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use your preferred database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'  # Replace with a random secret key
    JWT_SECRET_KEY = 'jwt-secret-key'  # Replace with a random JWT secret key
    CORS_HEADERS = 'Content-Type'