from typing import Generator, Any
import subprocess

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from app.db.models.user import User
from starlette.testclient import TestClient
from app.db.session import get_db
import os
from app.main import app


test_engine = create_engine(
    "postgresql://postgres_test:postgres_test@localhost:5442/dsh_db_users_test",
    future=True,
)

test_session = sessionmaker(bind=test_engine, expire_on_commit=False)

CLEAN_TABLES = [
    "users",
]


@pytest.fixture(scope="session", autouse=True)
def run_migration():
    if not os.path.exists("tests/alembic"):
        os.system("alembic init tests/alembic")

    subprocess.run(
        "alembic -c tests/alembic.ini revision --autogenerate -m 'test running migrations'"
    )
    os.system("alembic -c tests/alembic.ini upgrade heads")


@pytest.fixture(scope="function")
def db():
    engine = create_engine(
        "postgresql://postgres_test:postgres_test@localhost:5442/dsh_db_users_test",
        future=True,
    )
    _Session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)
    session = _Session()
    yield session
    session.close()


@pytest.fixture(scope="function", autouse=True)
def clean_tables(db):
    with db as session:
        with session.begin():
            for table in CLEAN_TABLES:
                session.execute(text(f"""TRUNCATE TABLE {table};"""))


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    def _get_test_db():
        try:
            with test_session() as session:
                yield session
                session.close()
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture()
def create_user_in_db():
    def wrapper(
        user_id,
        username,
        email,
        hashed_password,
        session: Session,
    ):
        user = User(
            user_id=user_id,
            username=username,
            email=email,
            hashed_password=hashed_password,
        )

        with session as db:
            db.add(user)
            db.commit()
            db.flush()

    return wrapper
