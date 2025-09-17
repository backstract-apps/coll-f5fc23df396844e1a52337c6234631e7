from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    name: str = raw_data.name
    contact_information: str = raw_data.contact_information

    record_to_be_added = {"name": name, "contact_information": contact_information}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_information: str = raw_data.contact_information

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_information": contact_information,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_wallets(db: Session):

    query = db.query(models.Wallets)

    wallets_all = query.all()
    wallets_all = (
        [new_data.to_dict() for new_data in wallets_all] if wallets_all else wallets_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"wallets_all": wallets_all},
    }
    return res


async def get_wallets_id(db: Session, id: int):

    query = db.query(models.Wallets)
    query = query.filter(and_(models.Wallets.id == id))

    wallets_one = query.first()

    wallets_one = (
        (
            wallets_one.to_dict()
            if hasattr(wallets_one, "to_dict")
            else vars(wallets_one)
        )
        if wallets_one
        else wallets_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"wallets_one": wallets_one},
    }
    return res


async def post_wallets(db: Session, raw_data: schemas.PostWallets):
    user_id: int = raw_data.user_id
    balance: str = raw_data.balance

    record_to_be_added = {"balance": balance, "user_id": user_id}
    new_wallets = models.Wallets(**record_to_be_added)
    db.add(new_wallets)
    db.commit()
    db.refresh(new_wallets)
    wallets_inserted_record = new_wallets.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"wallets_inserted_record": wallets_inserted_record},
    }
    return res


async def put_wallets_id(db: Session, raw_data: schemas.PutWalletsId):
    id: int = raw_data.id
    user_id: int = raw_data.user_id
    balance: str = raw_data.balance

    query = db.query(models.Wallets)
    query = query.filter(and_(models.Wallets.id == id))
    wallets_edited_record = query.first()

    if wallets_edited_record:
        for key, value in {"id": id, "balance": balance, "user_id": user_id}.items():
            setattr(wallets_edited_record, key, value)

        db.commit()
        db.refresh(wallets_edited_record)

        wallets_edited_record = (
            wallets_edited_record.to_dict()
            if hasattr(wallets_edited_record, "to_dict")
            else vars(wallets_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"wallets_edited_record": wallets_edited_record},
    }
    return res


async def delete_wallets_id(db: Session, id: int):

    query = db.query(models.Wallets)
    query = query.filter(and_(models.Wallets.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        wallets_deleted = record_to_delete.to_dict()
    else:
        wallets_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"wallets_deleted": wallets_deleted},
    }
    return res


async def get_transactions(db: Session):

    query = db.query(models.Transactions)

    transactions_all = query.all()
    transactions_all = (
        [new_data.to_dict() for new_data in transactions_all]
        if transactions_all
        else transactions_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"transactions_all": transactions_all},
    }
    return res


async def get_transactions_id(db: Session, id: int):

    query = db.query(models.Transactions)
    query = query.filter(and_(models.Transactions.id == id))

    transactions_one = query.first()

    transactions_one = (
        (
            transactions_one.to_dict()
            if hasattr(transactions_one, "to_dict")
            else vars(transactions_one)
        )
        if transactions_one
        else transactions_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"transactions_one": transactions_one},
    }
    return res


async def post_transactions(db: Session, raw_data: schemas.PostTransactions):
    sender_user_id: int = raw_data.sender_user_id
    receiver_user_id: int = raw_data.receiver_user_id
    amount: str = raw_data.amount
    transaction_date: str = raw_data.transaction_date
    merchant_id: int = raw_data.merchant_id
    category_id: int = raw_data.category_id

    record_to_be_added = {
        "amount": amount,
        "category_id": category_id,
        "merchant_id": merchant_id,
        "sender_user_id": sender_user_id,
        "receiver_user_id": receiver_user_id,
        "transaction_date": transaction_date,
    }
    new_transactions = models.Transactions(**record_to_be_added)
    db.add(new_transactions)
    db.commit()
    db.refresh(new_transactions)
    transactions_inserted_record = new_transactions.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"transactions_inserted_record": transactions_inserted_record},
    }
    return res


async def put_transactions_id(db: Session, raw_data: schemas.PutTransactionsId):
    id: int = raw_data.id
    sender_user_id: int = raw_data.sender_user_id
    receiver_user_id: int = raw_data.receiver_user_id
    amount: str = raw_data.amount
    transaction_date: str = raw_data.transaction_date
    merchant_id: int = raw_data.merchant_id
    category_id: int = raw_data.category_id

    query = db.query(models.Transactions)
    query = query.filter(and_(models.Transactions.id == id))
    transactions_edited_record = query.first()

    if transactions_edited_record:
        for key, value in {
            "id": id,
            "amount": amount,
            "category_id": category_id,
            "merchant_id": merchant_id,
            "sender_user_id": sender_user_id,
            "receiver_user_id": receiver_user_id,
            "transaction_date": transaction_date,
        }.items():
            setattr(transactions_edited_record, key, value)

        db.commit()
        db.refresh(transactions_edited_record)

        transactions_edited_record = (
            transactions_edited_record.to_dict()
            if hasattr(transactions_edited_record, "to_dict")
            else vars(transactions_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"transactions_edited_record": transactions_edited_record},
    }
    return res


async def delete_transactions_id(db: Session, id: int):

    query = db.query(models.Transactions)
    query = query.filter(and_(models.Transactions.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        transactions_deleted = record_to_delete.to_dict()
    else:
        transactions_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"transactions_deleted": transactions_deleted},
    }
    return res


async def get_merchants(db: Session):

    query = db.query(models.Merchants)

    merchants_all = query.all()
    merchants_all = (
        [new_data.to_dict() for new_data in merchants_all]
        if merchants_all
        else merchants_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_all": merchants_all},
    }
    return res


async def get_merchants_id(db: Session, id: int):

    query = db.query(models.Merchants)
    query = query.filter(and_(models.Merchants.id == id))

    merchants_one = query.first()

    merchants_one = (
        (
            merchants_one.to_dict()
            if hasattr(merchants_one, "to_dict")
            else vars(merchants_one)
        )
        if merchants_one
        else merchants_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_one": merchants_one},
    }
    return res


async def put_merchants_id(db: Session, raw_data: schemas.PutMerchantsId):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_information: str = raw_data.contact_information

    query = db.query(models.Merchants)
    query = query.filter(and_(models.Merchants.id == id))
    merchants_edited_record = query.first()

    if merchants_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_information": contact_information,
        }.items():
            setattr(merchants_edited_record, key, value)

        db.commit()
        db.refresh(merchants_edited_record)

        merchants_edited_record = (
            merchants_edited_record.to_dict()
            if hasattr(merchants_edited_record, "to_dict")
            else vars(merchants_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_edited_record": merchants_edited_record},
    }
    return res


async def delete_merchants_id(db: Session, id: int):

    query = db.query(models.Merchants)
    query = query.filter(and_(models.Merchants.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        merchants_deleted = record_to_delete.to_dict()
    else:
        merchants_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_deleted": merchants_deleted},
    }
    return res


async def get_payment_methods(db: Session):

    query = db.query(models.PaymentMethods)

    payment_methods_all = query.all()
    payment_methods_all = (
        [new_data.to_dict() for new_data in payment_methods_all]
        if payment_methods_all
        else payment_methods_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payment_methods_all": payment_methods_all},
    }
    return res


async def get_payment_methods_id(db: Session, id: int):

    query = db.query(models.PaymentMethods)
    query = query.filter(and_(models.PaymentMethods.id == id))

    payment_methods_one = query.first()

    payment_methods_one = (
        (
            payment_methods_one.to_dict()
            if hasattr(payment_methods_one, "to_dict")
            else vars(payment_methods_one)
        )
        if payment_methods_one
        else payment_methods_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payment_methods_one": payment_methods_one},
    }
    return res


async def post_payment_methods(db: Session, raw_data: schemas.PostPaymentMethods):
    user_id: int = raw_data.user_id
    type: str = raw_data.type
    details: str = raw_data.details

    record_to_be_added = {"type": type, "details": details, "user_id": user_id}
    new_payment_methods = models.PaymentMethods(**record_to_be_added)
    db.add(new_payment_methods)
    db.commit()
    db.refresh(new_payment_methods)
    payment_methods_inserted_record = new_payment_methods.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payment_methods_inserted_record": payment_methods_inserted_record},
    }
    return res


async def put_payment_methods_id(db: Session, raw_data: schemas.PutPaymentMethodsId):
    id: int = raw_data.id
    user_id: int = raw_data.user_id
    type: str = raw_data.type
    details: str = raw_data.details

    query = db.query(models.PaymentMethods)
    query = query.filter(and_(models.PaymentMethods.id == id))
    payment_methods_edited_record = query.first()

    if payment_methods_edited_record:
        for key, value in {
            "id": id,
            "type": type,
            "details": details,
            "user_id": user_id,
        }.items():
            setattr(payment_methods_edited_record, key, value)

        db.commit()
        db.refresh(payment_methods_edited_record)

        payment_methods_edited_record = (
            payment_methods_edited_record.to_dict()
            if hasattr(payment_methods_edited_record, "to_dict")
            else vars(payment_methods_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payment_methods_edited_record": payment_methods_edited_record},
    }
    return res


async def delete_payment_methods_id(db: Session, id: int):

    query = db.query(models.PaymentMethods)
    query = query.filter(and_(models.PaymentMethods.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        payment_methods_deleted = record_to_delete.to_dict()
    else:
        payment_methods_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payment_methods_deleted": payment_methods_deleted},
    }
    return res


async def get_categories(db: Session):

    query = db.query(models.Categories)

    categories_all = query.all()
    categories_all = (
        [new_data.to_dict() for new_data in categories_all]
        if categories_all
        else categories_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"categories_all": categories_all},
    }
    return res


async def get_categories_id(db: Session, id: int):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.id == id))

    categories_one = query.first()

    categories_one = (
        (
            categories_one.to_dict()
            if hasattr(categories_one, "to_dict")
            else vars(categories_one)
        )
        if categories_one
        else categories_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"categories_one": categories_one},
    }
    return res


async def post_categories(db: Session, raw_data: schemas.PostCategories):
    name: str = raw_data.name

    record_to_be_added = {"name": name}
    new_categories = models.Categories(**record_to_be_added)
    db.add(new_categories)
    db.commit()
    db.refresh(new_categories)
    categories_inserted_record = new_categories.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"categories_inserted_record": categories_inserted_record},
    }
    return res


async def put_categories_id(db: Session, raw_data: schemas.PutCategoriesId):
    id: int = raw_data.id
    name: str = raw_data.name

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.id == id))
    categories_edited_record = query.first()

    if categories_edited_record:
        for key, value in {"id": id, "name": name}.items():
            setattr(categories_edited_record, key, value)

        db.commit()
        db.refresh(categories_edited_record)

        categories_edited_record = (
            categories_edited_record.to_dict()
            if hasattr(categories_edited_record, "to_dict")
            else vars(categories_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"categories_edited_record": categories_edited_record},
    }
    return res


async def delete_categories_id(db: Session, id: int):

    query = db.query(models.Categories)
    query = query.filter(and_(models.Categories.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        categories_deleted = record_to_delete.to_dict()
    else:
        categories_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"categories_deleted": categories_deleted},
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    try:
        print("HI there!")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def post_merchants(db: Session, raw_data: schemas.PostMerchants):
    name: str = raw_data.name
    contact_information: str = raw_data.contact_information

    record_to_be_added = {"name": name, "contact_information": contact_information}
    new_merchants = models.Merchants(**record_to_be_added)
    db.add(new_merchants)
    db.commit()
    db.refresh(new_merchants)
    merchants_inserted_record = new_merchants.to_dict()

    res = {
        "status": 200,
        "message": "Lakshay Singh",
        "data": {"merchants_inserted_record": merchants_inserted_record},
    }
    return res
