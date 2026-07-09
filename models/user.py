from pydantic import BaseModel
from typing import Literal


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: Literal["admin", "user", "guest"]
    avatar_url: str | None
    created_at: str
