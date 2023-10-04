from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse  # Add this import
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

simple_detail = [
    {
        "id": 1,
        "name": "Akshaya",
        "image": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
    },
    {
        "id": 2,
        'name': 'John Doe',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 3,
        'name': 'Jane Smith',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 4,
        'name': 'Michael Johnson',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 5,
        'name': 'Emily Davis',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 6,
        'name': 'David Wilson',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 7,
        'name': 'Sarah Brown',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 8,
        'name': 'James Lee',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 9,
        'name': 'Olivia Miller',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 10,
        'name': 'William Taylor',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 11,
        'name': 'Sophia Anderson',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 12,
        'name': 'Daniel Martinez',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 13,
        'name': 'Emma Wilson',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 14,
        'name': 'Liam White',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 15,
        'name': 'Olivia Clark',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 16,
        'name': 'Noah Martin',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 17,
        'name': 'Ava Garcia',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 18,
        'name': 'Mason Lopez',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 19,
        'name': 'Sophia Perez',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        "id": 20,
        'name': 'Ethan Davis',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    }
]


advanced_detail = [
    {
        'id': 1,
        'f_name': 'Akshaya',
        'l_name': 'P',
        'contact': '123-456-7890',
        'email': 'akshaya@example.com',
        'image': "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
    },
    {
        'id': 2,
        'f_name': 'John',
        'l_name': 'Doe',
        'contact': '123-456-7890',
        'email': 'john.doe@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 3,
        'f_name': 'Jane',
        'l_name': 'Smith',
        'contact': '987-654-3210',
        'email': 'jane.smith@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 4,
        'f_name': 'Michael',
        'l_name': 'Johnson',
        'contact': '555-555-5555',
        'email': 'michael.johnson@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 5,
        'f_name': 'Emily',
        'l_name': 'Davis',
        'contact': '555-555-5555',
        'email': 'emily.davis@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 6,
        'f_name': 'David',
        'l_name': 'Wilson',
        'contact': '555-555-5555',
        'email': 'david.wilson@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 7,
        'f_name': 'Sarah',
        'l_name': 'Brown',
        'contact': '555-555-5555',
        'email': 'sarah.brown@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 8,
        'f_name': 'James',
        'l_name': 'Lee',
        'contact': '555-555-5555',
        'email': 'james.lee@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 9,
        'f_name': 'Olivia',
        'l_name': 'Miller',
        'contact': '555-555-5555',
        'email': 'olivia.miller@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 10,
        'f_name': 'William',
        'l_name': 'Taylor',
        'contact': '555-555-5555',
        'email': 'william.taylor@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 11,
        'f_name': 'Sophia',
        'l_name': 'Anderson',
        'contact': '555-555-5555',
        'email': 'sophia.anderson@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 12,
        'f_name': 'Daniel',
        'l_name': 'Martinez',
        'contact': '555-555-5555',
        'email': 'daniel.martinez@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 13,
        'f_name': 'Emma',
        'l_name': 'Wilson',
        'contact': '555-555-5555',
        'email': 'emma.wilson@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 14,
        'f_name': 'Liam',
        'l_name': 'White',
        'contact': '555-555-5555',
        'email': 'liam.white@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 15,
        'f_name': 'Olivia',
        'l_name': 'Clark',
        'contact': '555-555-5555',
        'email': 'olivia.clark@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 16,
        'f_name': 'Noah',
        'l_name': 'Martin',
        'contact': '555-555-5555',
        'email': 'noah.martin@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 17,
        'f_name': 'Ava',
        'l_name': 'Garcia',
        'contact': '555-555-5555',
        'email': 'ava.garcia@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 18,
        'f_name': 'Mason',
        'l_name': 'Lopez',
        'contact': '555-555-5555',
        'email': 'mason.lopez@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 19,
        'f_name': 'Sophia',
        'l_name': 'Perez',
        'contact': '555-555-5555',
        'email': 'sophia.perez@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    },
    {
        'id': 20,
        'f_name': 'Ethan',
        'l_name': 'Davis',
        'contact': '555-555-5555',
        'email': 'ethan.davis@example.com',
        'image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    }
]

# You now have the completed advanced_detail list up to 'id': 20 based on the data from simple_detail.


@api_view(['GET'])
def employeedetails(request, id):
    employee = None
    for item in advanced_detail:
        if item['id'] == id:
            employee = item
            break

    if employee:
        return Response({"status": "success", "response_code": status.HTTP_200_OK, "data": employee})
    else:
        return Response({"status": "failed", "response_code": status.HTTP_404_NOT_FOUND, "data": []})


@api_view(['GET'])
def simple_details(request):
    return Response({"status": "success", "response_code": status.HTTP_200_OK, "data": simple_detail})

