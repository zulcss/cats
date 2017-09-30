import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('/app/data', 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join('/app/data', 'db_repository')
