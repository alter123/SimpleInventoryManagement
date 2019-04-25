
import requests

def inventory_list(page=1):
    data = requests.get(f'http://127.0.0.1:8000/inventory/list/?page={page}')
    print(data.content)

def purchase_item( item_id = 'ef2b1992-82e1-4231-8fd9-31bb79622744', quantity = 5 ):
    data = requests.get(f'http://127.0.0.1:8000/inventory/purchase?quantity={quantity}&item_id={item_id}')
    print( data.content )