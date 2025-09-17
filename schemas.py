from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None


class ReadUsers(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None
    class Config:
        from_attributes = True


class Wallets(BaseModel):
    user_id: Optional[int]=None
    balance: Optional[float]=None


class ReadWallets(BaseModel):
    user_id: Optional[int]=None
    balance: Optional[float]=None
    class Config:
        from_attributes = True


class Transactions(BaseModel):
    sender_user_id: Optional[int]=None
    receiver_user_id: Optional[int]=None
    amount: Optional[float]=None
    transaction_date: Optional[Any]=None
    merchant_id: Optional[int]=None
    category_id: Optional[int]=None


class ReadTransactions(BaseModel):
    sender_user_id: Optional[int]=None
    receiver_user_id: Optional[int]=None
    amount: Optional[float]=None
    transaction_date: Optional[Any]=None
    merchant_id: Optional[int]=None
    category_id: Optional[int]=None
    class Config:
        from_attributes = True


class Merchants(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None


class ReadMerchants(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None
    class Config:
        from_attributes = True


class PaymentMethods(BaseModel):
    user_id: Optional[int]=None
    type: Optional[str]=None
    details: Optional[str]=None


class ReadPaymentMethods(BaseModel):
    user_id: Optional[int]=None
    type: Optional[str]=None
    details: Optional[str]=None
    class Config:
        from_attributes = True


class Categories(BaseModel):
    name: Optional[str]=None


class ReadCategories(BaseModel):
    name: Optional[str]=None
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    contact_information: Optional[str]=None

    class Config:
        from_attributes = True



class PostWallets(BaseModel):
    user_id: Optional[int]=None
    balance: Optional[str]=None

    class Config:
        from_attributes = True



class PutWalletsId(BaseModel):
    id: Optional[int]=None
    user_id: Optional[int]=None
    balance: Optional[str]=None

    class Config:
        from_attributes = True



class PostTransactions(BaseModel):
    sender_user_id: Optional[int]=None
    receiver_user_id: Optional[int]=None
    amount: Optional[str]=None
    transaction_date: Optional[str]=None
    merchant_id: Optional[int]=None
    category_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutTransactionsId(BaseModel):
    id: Optional[int]=None
    sender_user_id: Optional[int]=None
    receiver_user_id: Optional[int]=None
    amount: Optional[str]=None
    transaction_date: Optional[str]=None
    merchant_id: Optional[int]=None
    category_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutMerchantsId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    contact_information: Optional[str]=None

    class Config:
        from_attributes = True



class PostPaymentMethods(BaseModel):
    user_id: Optional[int]=None
    type: Optional[str]=None
    details: Optional[str]=None

    class Config:
        from_attributes = True



class PutPaymentMethodsId(BaseModel):
    id: Optional[int]=None
    user_id: Optional[int]=None
    type: Optional[str]=None
    details: Optional[str]=None

    class Config:
        from_attributes = True



class PostCategories(BaseModel):
    name: Optional[str]=None

    class Config:
        from_attributes = True



class PutCategoriesId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None

    class Config:
        from_attributes = True



class PostMerchants(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None

    class Config:
        from_attributes = True

