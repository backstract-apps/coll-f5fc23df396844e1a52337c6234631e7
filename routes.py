from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/wallets/')
async def get_wallets(db: Session = Depends(get_db)):
    try:
        return await service.get_wallets(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/wallets/id')
async def get_wallets_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_wallets_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/wallets/')
async def post_wallets(raw_data: schemas.PostWallets, db: Session = Depends(get_db)):
    try:
        return await service.post_wallets(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/wallets/id/')
async def put_wallets_id(raw_data: schemas.PutWalletsId, db: Session = Depends(get_db)):
    try:
        return await service.put_wallets_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/wallets/id')
async def delete_wallets_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_wallets_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/transactions/')
async def get_transactions(db: Session = Depends(get_db)):
    try:
        return await service.get_transactions(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/transactions/id')
async def get_transactions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_transactions_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/transactions/')
async def post_transactions(raw_data: schemas.PostTransactions, db: Session = Depends(get_db)):
    try:
        return await service.post_transactions(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/transactions/id/')
async def put_transactions_id(raw_data: schemas.PutTransactionsId, db: Session = Depends(get_db)):
    try:
        return await service.put_transactions_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/transactions/id')
async def delete_transactions_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_transactions_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchants/')
async def get_merchants(db: Session = Depends(get_db)):
    try:
        return await service.get_merchants(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchants/id')
async def get_merchants_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_merchants_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/merchants/id/')
async def put_merchants_id(raw_data: schemas.PutMerchantsId, db: Session = Depends(get_db)):
    try:
        return await service.put_merchants_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/merchants/id')
async def delete_merchants_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_merchants_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/payment_methods/')
async def get_payment_methods(db: Session = Depends(get_db)):
    try:
        return await service.get_payment_methods(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/payment_methods/id')
async def get_payment_methods_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_payment_methods_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/payment_methods/')
async def post_payment_methods(raw_data: schemas.PostPaymentMethods, db: Session = Depends(get_db)):
    try:
        return await service.post_payment_methods(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/payment_methods/id/')
async def put_payment_methods_id(raw_data: schemas.PutPaymentMethodsId, db: Session = Depends(get_db)):
    try:
        return await service.put_payment_methods_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/payment_methods/id')
async def delete_payment_methods_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_payment_methods_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/')
async def get_categories(db: Session = Depends(get_db)):
    try:
        return await service.get_categories(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/id')
async def get_categories_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_categories_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/categories/')
async def post_categories(raw_data: schemas.PostCategories, db: Session = Depends(get_db)):
    try:
        return await service.post_categories(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/categories/id/')
async def put_categories_id(raw_data: schemas.PutCategoriesId, db: Session = Depends(get_db)):
    try:
        return await service.put_categories_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/categories/id')
async def delete_categories_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_categories_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/merchants/')
async def post_merchants(raw_data: schemas.PostMerchants, db: Session = Depends(get_db)):
    try:
        return await service.post_merchants(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

