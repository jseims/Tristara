from django.db import connection, transaction, IntegrityError
from django.core.cache import cache

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [ 
        dict(zip([col[0] for col in desc], row)) 
        for row in cursor.fetchall() 
    ] 