from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    result = None
    error = None
    if request.method == 'POST':
        try:
            a = int(request.POST.get('Num1'))
            b = int(request.POST.get('Num2'))
            Op = request.POST.get('Op')
            
            if Op == 'Add':
                result = a + b
            elif Op == 'Sub':
                result = a - b
            elif Op == 'Mul':
                result = a * b
            elif Op == 'Div':
                if b == 0:
                    error = "Cannot divide by zero."
                else:
                    result = a / b
            else:
                error = "Invalid operation."
        except Exception as e:
            error = str(e)

        if error:
            return render(request, 'home.html', {'error': error})
        return render(request, 'result.html', {'result': result})
    
    return render(request, 'home.html')

def hello(request):
    result = request.GET.get('result')
    return render(request, 'result.html', {'result': result})