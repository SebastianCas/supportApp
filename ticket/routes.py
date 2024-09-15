from fastapi import APIRouter, HTTPException, Depends
from ticket.schema import SupportTicketSchema
from .repository import saveTicket, searchTickets
from auth.helper import getCurrentUser
from typing import Optional

app = APIRouter()

@app.post("/ticket")
async def createTicket(ticket: SupportTicketSchema, currentUser: dict = Depends(getCurrentUser)):
    userId = currentUser['userid']
    ticketId = await saveTicket(ticket, userId)
    if not ticketId:
        return HTTPException(status_code=500, detail="An error occurred while creating the ticket")
    
    return {'ticketId': ticketId, "message": "Ticket created successfully"}

@app.get("/ticket")
async def getAllTickets(createdby: Optional[int]=None):
    return await searchTickets(createdby)