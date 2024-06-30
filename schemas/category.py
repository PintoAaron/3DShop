from pydantic import BaseModel, Field


class CategoryIn(BaseModel):
    name: str = Field(..., description="name of the category")
    description: str | None = Field(None,description="a description of the category")


class CategoryOut(CategoryIn):
    id: int
