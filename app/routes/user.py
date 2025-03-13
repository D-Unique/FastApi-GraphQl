from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas import UserBase, UserCreate, UserGetResponse, UserPostResponse
from models.user import User
from db.conn import get_db
from typing import List


user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", response_model=List[UserGetResponse], summary="The endpoint return all users")
async def get_users(db: AsyncSession = Depends(get_db)):
    """
    
    This route returns all users

    """
    result = await db.execute(select(User))
    all_users = result.scalars().all()
    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No registered user")
    return all_users


@user_router.get("/{user_id}", response_model=UserGetResponse)
async def get_user(user_id: int, session: AsyncSession = Depends(get_db)):
    """
    This Endpoint returns a single user
    
    """
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No User found")
        
    return user


@user_router.post("/", response_model=UserPostResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, session: AsyncSession = Depends(get_db)):
    """
    The endpoint create a new user
    
    """
    new_user =  User(name=user.name, email=user.email, password=user.password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
