from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import datetime

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def calculator(request, num1, num2, num3=None):
    
    params = [int(num1), int(num2)]
    if num3:
        params.append(int(num3))
    else:
        params.append(0)
        
    final_sum = sum(params)
    difference = params[0] - params[1] - params[2]
    product = params[0] * params[1] * params[2]
    quotient = params[0] / params[1]
    
    return render(
        request,
        "calculator.html",
        {"number1": num1, "number2": num2, "number3": num3, "sum": final_sum, "difference": difference, "product": product, "quotient": quotient}
    )
    
def is_valid_date(request, year, month, day):
    
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
        
    if(is_valid):
        answer = "The date is valid."
    else:
        answer = "The date is not valid."
        
    return render(
        request,
        "is_valid_date.html",
        {"year": year, "month": month,"day": day, "is_valid": answer}
    )