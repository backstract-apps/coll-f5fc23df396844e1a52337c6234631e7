from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column(String, primary_key=False )
    contact_information = Column(String, primary_key=False )


class Wallets(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True, autoincrement=True )
    user_id = Column(Integer, primary_key=False )
    balance = Column(Float, primary_key=False )


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True )
    sender_user_id = Column(Integer, primary_key=False )
    receiver_user_id = Column(Integer, primary_key=False )
    amount = Column(Float, primary_key=False )
    transaction_date = Column(String, primary_key=False )
    merchant_id = Column(Integer, primary_key=False )
    category_id = Column(Integer, primary_key=False )


class Merchants(Base):
    __tablename__ = 'merchants'
    id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column(String, primary_key=False )
    contact_information = Column(String, primary_key=False )


class PaymentMethods(Base):
    __tablename__ = 'payment_methods'
    id = Column(Integer, primary_key=True, autoincrement=True )
    user_id = Column(Integer, primary_key=False )
    type = Column(String, primary_key=False )
    details = Column(String, primary_key=False )


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column(String, primary_key=False )


