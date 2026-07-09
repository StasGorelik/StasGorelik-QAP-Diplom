from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    board_id: int
    created_by: int
    assignee_id: int | None
    created_at: str
    updated_at: str
