from sqlalchemy.ext.asyncio import AsyncSession

from app.model import Product

def add_product(session: AsyncSession, title: str, image:str):
    new_product = Product(title=title, image=image)
    session.add(new_product)
    return new_product