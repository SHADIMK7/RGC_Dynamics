from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

simple_detail = [
    {
        "id": 1,
        "name": "Akshaya",
        "image": "fdghj.jpg"
    },

    {
        "id": 2,
        'name': 'John Doe',
        'image': 'john.jpg',
    },
    {
        "id": 3,
        'name': 'Jane Smith',
        'image': 'jane.jpg',
    }

]

advanced_detail = [
    {
        'id': 1,
        'f_name': 'akshaya',
        'l_name': 'p',
        'contact': '123-456-7890',
        'email': 'akshaya@example.com',
        'image': 'fgh.jpg',
    },
    {
        'id': 2,
        'f_name': 'John',
        'l_name': 'Doe',
        'contact': '123-456-7890',
        'email': 'john.doe@example.com',
        'image': 'john.jpg',
    },
    {
        'id': 3,
        'f_name': 'Jane',
        'l_name': 'Smith',
        'contact': '987-654-3210',
        'email': 'jane.smith@example.com',
        'image': 'jane.jpg',
    }
]


@csrf_exempt
def employeedetails(request, id):
    employee = None
    for item in advanced_detail:
        if item['id'] == id:
            employee = item
            break

    if employee:
        # Return the entire employee dictionary as JSON
        return JsonResponse(employee)
    else:
        return HttpResponse('Employee not found', status=404)


@csrf_exempt
def simple_details(request):
    return JsonResponse(simple_detail, safe=False)
