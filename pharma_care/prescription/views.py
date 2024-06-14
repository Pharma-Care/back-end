from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prescription, PrescriptionItem
from customers.models import Customer
from inventory.models import InventoryItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@csrf_exempt
def submit_sale(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_name = data.get('customer_name')
        customer_id_number = data.get('customer_id')

        customer, created = Customer.objects.get_or_create(name=customer_name, id_number=customer_id_number)

        prescription = Prescription.objects.create(
            customer=customer,
            subtotal=data['subtotal'],
            vat=data['vat'],
            total_price=data['total_price']
        )

        for item in data['sale_items']:
            inventory_item = get_object_or_404(InventoryItem, item_name=item['name'])
            
            if inventory_item.quantity < item['quantity']:
                return JsonResponse({'error': f'Not enough stock for {item["name"]}'}, status=400)

            inventory_item.quantity -= item['quantity']
            inventory_item.save()

            PrescriptionItem.objects.create(
                prescription=prescription,
                inventory_item=inventory_item,
                quantity=item['quantity'],
                price=item['price']
            )

        return JsonResponse({'message': 'Sale submitted successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@api_view(['POST'])
def get_prescriptions_by_customer(request):
    print(request.data)
    customer_id = int(request.data.get('customer_id'))
    customer = get_object_or_404(Customer, id_number=customer_id)
    print(f'Customer: {customer}')
    
    prescriptions = Prescription.objects.filter(customer=customer)
    print(f'Prescriptions: {prescriptions}')
    
    response_data = {
        'name': customer.name,
        'id': customer.id_number,
        'Items': []
    }

    for prescription in prescriptions:
        print(prescription)
        items = PrescriptionItem.objects.filter(prescription=prescription)
        # temp = PrescriptionItem.objects.
        # print(temp)
        print(f'Items for prescription {prescription.id}: {items}')
        
        for item in items:
            print(f'Item: {item}, Inventory Item: {item.inventory_item}')
            response_data['Items'].append({
                'ItemName': item.inventory_item.item_name,
                'ItemIssued': prescription.date.strftime('%d/%m/%Y')
            })
    
    print(f'Final response data: {response_data}')
    return Response(response_data)
