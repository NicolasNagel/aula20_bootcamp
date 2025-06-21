from sqlalchemy.orm import Session
from schema import ProductUptade, ProductCreate
from models import ProductModel

def get_products(db: Session):
    """
    Função que retorna todos os produtos da tabela 'products'
    """
    return db.query(ProductModel).all()

def get_product(db: Session, product_id: int):
    """
    Função que retorna somente um produto da tabela 'products'
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    """
    Função que cria o produto e salva no Banco de Dados
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """
    Função que deleta os produto do Banco de Dados
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

def update_product(db: Session, product_id: int, product: ProductUptade):
    """
    Função que atualiza os registros do produto no Banco de Dados
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor
    db.commit()
    db.refresh(db_product)
    return db_product