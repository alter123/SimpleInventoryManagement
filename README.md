## SimpleInventoryManagement

API's implemented are:

1. /inventory/list
 - Should return data with pagination count of 5.
 - Filters objects which are sold out.
2. /inventory/purchase
 - Allows purchase multiple items for required quantity.

##### Inventory Auto-generation:
The repeated jobs are created using dependency django-background-tasks
To create automated entries, `python manage.py process_tasks` should be executed after `python manage.py runserver`

Client specifications(client.py):
- Python script to communicate with the server and performs list/purchase inventory.
