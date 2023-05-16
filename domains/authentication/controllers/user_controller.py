from fastapi import APIRouter, Depends, HTTPException
from dependencies.get_current_user import get_current_user
from domains.authentication.schemas.user_schema import CreateUserRequestSchema, UserSchema, CreateUserResponseSchema
from domains.authentication.schemas.update_user_schema import UpdateUserSchema
from domains.authentication.models.user_model import UserModel
import domains.authentication.services.user_service as user_service

router = APIRouter()

@router.get('')
def get_all_user(
    current_user: UserModel = Depends(get_current_user),
) -> list[UserSchema]:
    if not current_user.has_permission('read', 'user'):
        raise HTTPException(status_code=403, detail="User does not have permission to get user data")
    users = user_service.get_all_users()
    return [UserSchema.from_orm(user) for user in users]


@router.get('/{user_id}')
def get_user_by_id(
    user_id: str,
    current_user: UserModel = Depends(get_current_user),
) -> UserSchema:
    if not current_user.has_permission('read', 'user'):
        raise HTTPException(status_code=403, detail="User does not have permission to get user data")
    return user_service.get_user_by_id(user_id)


@router.post('', response_model=CreateUserResponseSchema)
def create_user(
    user: CreateUserRequestSchema,
    current_user: UserModel = Depends(get_current_user),
) -> CreateUserResponseSchema:
    if not current_user.has_permission('create', 'user'):
        raise HTTPException(status_code=403, detail="User does not have permission to create a new user")
    created_user = user_service.create_user(user)
    return created_user


@router.put('/{user_id}')
def update_user(
    user_id: str,
    updated_user: UpdateUserSchema,
    current_user: UserModel = Depends(get_current_user),
) -> None:
    if not current_user.has_permission('update', 'user'):
        raise HTTPException(status_code=403, detail="User does not have permission to update user data")
    user_service.update_user(user_id, updated_user)


@router.delete('/{user_id}')
def delete_user(
    user_id: str,
    current_user: UserModel = Depends(get_current_user),
) -> None:
    if not current_user.has_permission('delete', 'user'):
        raise HTTPException(status_code=403, detail="User does not have permission to delete a user")
    user_service.delete_user(user_id)
