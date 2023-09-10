from django.shortcuts import render

# Create your views here.
def items(request) :
    
    application = 'Library Inventories'
    name = 'Sarah Nazly Nuraya'
    class_name = 'PBP - A'

    return render(request, 'items.html', {'application' : application, 'name' : name, 'class' : class_name})