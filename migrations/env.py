from alembic import context
from app.main import Base
from sqlalchemy import create_engine

target_metadata = Base.metadata

def run_migrations_online():
    connectable = create_engine(context.config.get_main_option("sqlalchemy.url"))
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
