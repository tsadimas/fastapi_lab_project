import sqlalchemy
import databases


# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
        "notes",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("text", sqlalchemy.String),
        sqlalchemy.Column("completed", sqlalchemy.Boolean),
        )

engine = sqlalchemy.create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
        )

metadata.create_all(engine)
