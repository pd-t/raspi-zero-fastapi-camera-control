# generated by fastapi-codegen:
#   filename:  oas/openapi.yaml
#   timestamp: 2022-06-15T16:10:43+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class Media(BaseModel):
    filename: str = Field(..., description='Media filename.', title='Media filename')
