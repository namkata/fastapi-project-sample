from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from apps.dependencies import get_db
from apps.sql_app import sevices, schemas

router = APIRouter()
"""
Noted:
- file-path: path:
    - You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).
    In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.
"""


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = sevices.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return sevices.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = sevices.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await sevices.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
async def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return await sevices.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = await sevices.get_items(db, skip=skip, limit=limit)
    return items
