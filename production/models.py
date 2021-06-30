from django.db import models, connection
from datetime import datetime, timedelta

class Production(models.Model):    
    # Get Production
    total = models.PositiveIntegerField(default=1)    
    
    # Get machine
    query = "SELECT id, id FROM pz_equipment WHERE id = 2" 
    cursor = connection.cursor()
    cursor.execute(query)
    machines = cursor.fetchall()    
    machine = models.IntegerField(        
        choices=machines,
        default=2,               
    )    

    # Get references
    query = "SELECT id, description FROM pz_references"
    cursor = connection.cursor()
    cursor.execute(query)
    references = cursor.fetchall()    
    article = models.IntegerField(        
        choices=references,
        default= 1,               
    )

    # Get date and time
    date_from = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField(default=datetime.now() + timedelta(hours=1))

class ProductionTable(models.Model):    
    article=models.CharField(max_length=20 )
    machine=models.IntegerField()
    total=models.IntegerField()
    date_from=models.DateTimeField()
    date_to=models.DateTimeField()
    
    class Meta():
        db_table = "public.production_production"