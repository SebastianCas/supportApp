from config.database import connection
from ticket.schema import SupportTicketSchema

async def saveTicket(ticket: SupportTicketSchema, userId: int):
    conn = connection()
    cur = conn.cursor()
    
    query = """
    INSERT INTO support_ticket (description, database_name, schema_name, sql_query, created_by)
    VALUES (%s, %s, %s, %s, %s) RETURNING id;
    """
    cur.execute(query, (ticket.description, ticket.database_name, ticket.schema_name, ticket.sql_query, userId))
    
    ticketId = cur.fetchone()['id']
    conn.commit()
    cur.close()
    conn.close()
    
    return ticketId

async def searchTickets(createdby):
    conn = connection()
    cur = conn.cursor()
    
    if createdby:
        query = """
        SELECT sp.*, u.username FROM support_ticket sp JOIN users u ON sp.created_by = u.id WHERE u.id = %s;
        """
        cur.execute(query, (createdby,))
    else:
        query = """
        SELECT sp.*, u.username FROM support_ticket sp JOIN users u ON sp.created_by = u.id;
        """
        cur.execute(query)
    
    tickets = cur.fetchall()
    cur.close()
    conn.close()
    
    return tickets