
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from myapp.config import settings
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL=f"postgresql://kayiwa_user:R10mQMScGRZ7jO9hRQMTSnzGbuKqAwAd@dpg-cqd0u1pu0jms73e69tk0-a/kayiwa"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal= sessionmaker(autoflush=False,bind=engine)
Base= declarative_base()
def get_db():
	db=SessionLocal()
	try:
		yield db
	finally:
			db.close()
