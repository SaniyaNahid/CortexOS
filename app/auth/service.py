import uuid
from datetime import datetime, UTC

from sqlalchemy.orm import Session

from app.auth.models import User
from app.auth.repository import UserRepository
from app.auth.schemas import UserRegister
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    @staticmethod
    def register_user(db: Session, user_data: UserRegister):

        # Check if email already exists
        existing_user = UserRepository.get_by_email(db, user_data.email)

        if existing_user:
            raise ValueError("Email already registered")

        # Hash password
        password_hash = hash_password(user_data.password)

        # Create User object
        user = User(
            id=uuid.uuid4(),
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password_hash=password_hash,
            is_active=True,
            is_verified=False,
            created_at=datetime.now(UTC).replace(tzinfo=None),
            updated_at=datetime.now(UTC).replace(tzinfo=None),
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login_user(db: Session, email: str, password: str):

        # Find user
        user = UserRepository.get_by_email(db, email)

        if not user:
            raise ValueError("Invalid email or password")

        # Verify password
        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid email or password")

        # Generate JWT token
        token = create_access_token(
            data={
                "sub": str(user.id),
                "email": user.email,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }