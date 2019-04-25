

from time import sleep
from random import randint

from .models import Item
from background_task import background

@background(schedule=10)
def create_new_inventory_item():
    '''
    This method only runs when django starts 
    and creates new objects every 10 secs 
    '''
    try:
        new_item = Item.objects.create( quantity = randint(1,10) )
        print( f'new item with id :{new_item.item_id} created' )
    except:
        print('some error occured!') 