import os

class Config:
    # Flaskアプリケーションの秘密鍵（セキュリティのためにランダムな値を設定する）
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    
    # データベースの設定
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
