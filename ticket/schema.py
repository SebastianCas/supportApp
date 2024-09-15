from pydantic import BaseModel
from typing import Optional

class SupportTicketSchema(BaseModel):
    description: str
    database_name: str
    schema_name: str
    sql_query: str