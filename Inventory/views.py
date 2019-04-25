
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

from .models import Item


def InventoryItemsList(request):
    item_list = Item.objects.filter( quantity__gt=0 )
    page      = request.GET.get('page', 1)

    paginator = Paginator(item_list, 5)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    li = [ (item.quantity, item.item_id) for item in items ]
    return JsonResponse({'item_list':li})



def PurchaseItem(request):
    try:
        item_id = str(request.GET.get('item_id'))
        quantity = int(request.GET.get('quantity'))

        item_quantity = Item.objects.get( item_id = item_id ).quantity

        Item.objects.filter( item_id=item_id ).update( quantity = F('quantity')-quantity ) # update quantity of product 
        
        if( item_quantity-quantity<=0 ):
            return JsonResponse({ 
                'message': f'Item with item_id {item_id}, purchased with quantity: {item_quantity}' 
                })

        return JsonResponse({
            'message': f'Item with item_id {item_id}, purchased with quantity.: {quantity}' 
            })
    except:
        return JsonResponse({ 'message': 'Required query cannot be processed'})


