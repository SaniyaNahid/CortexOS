import bcrypt
import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from app.auth.models import User
from app.auth.repository import UserRepository
from app.auth.schemas import UserRegister


class AuthService:

    @staticmethod
    def register_user(db: Session, user_data: UserRegister):

        # Check if email already exists
        existing_user = UserRepository.get_by_email(db, user_data.email)

        if existing_user:
            raise ValueError("Email already registered")

        # Hash password
        password_hash = bcrypt.hashpw(
            user_data.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # Create User object
        user = User(
            id=uuid.uuid4(),
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password_hash=password_hash,
            is_active=True,
            is_verified=False,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        return UserRepository.create(db, user)