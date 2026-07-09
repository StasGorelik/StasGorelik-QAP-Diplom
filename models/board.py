from pydantic import BaseModel


class BoardResponse(BaseModel):
    id: int
    title: str
    description: str | None
    public: bool
    archived: bool
    created_at: str
