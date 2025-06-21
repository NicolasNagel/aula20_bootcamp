from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schema import ProductResponse, ProductUptade, ProductCreate
from typing import List
from crud import (create_product, get_products, get_product, delete_product, update_product)

router = APIRouter()

@router.get("/products/", response_model = List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    """
    Função para ler todos os produtos no Banco de Dados
    """
    products = get_products(db)
    return products

@router.get("/products/{product_id}", response_model = ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    """
    Função para ler apenas um produto no Banco de Dados
    """
    db_product = get_product(db = db, product_id = product_id)
    if db_product is None:
        raise HTTPException(status_code = 404, detail = "Produto não encontrado")
    return db_product

@router.post("/products/", response_model = ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Função para criar um novo produto no Banco de Dados
    """
    return create_product(db = db, product = product)    

@router.delete("/products/{product_id}", response_model = ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Função para deleter um produto existente no Banco de Dados
    """
    product_db = delete_product(db, product_id = product_id)
    if product_db is None:
        raise HTTPException(status_code = 404, detail = "Produto não encontrado")
    return product_db

@router.put("/products/{product_id}", response_model = ProductResponse)
def update_product(product_id: int, product: ProductUptade, db: Session = Depends(get_db)):
    """
    Função que atualiza meu produto no Banco de Dados
    """
    product_db = update_product(db = db, product_id = product_id)
    if product_db is None:
        raise HTTPException(status_code = 404, detail = "Produto não encontrado")
    product_db