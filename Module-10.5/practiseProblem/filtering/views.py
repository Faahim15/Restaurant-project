from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    d = {
    'product': 'Smartphone',
    'price': 799.99,
    'quantity': 3,
    'discount_rate': 0.1,
    'tags': ['electronics', 'gadgets', 'mobile'],
    'description': 'A powerful smartphone with advanced features.',
    'date_purchased': '2023-01-15',
    'rating': 4.5,
    'is_available': True,
    'message': 'This is a special character: '' \n New line',
     'birthday': datetime.now(),
     'string': 'hello World',
     'empty': '',
     'lst': [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    
    ] , 
     'value':123456789,
     'striptags':'<b>I</b> <button>love</button> <span>dogs</span>'
  
    } 
    return render(request,'index.html',d)
