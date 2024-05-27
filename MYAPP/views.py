# from django.shortcuts import render , HttpResponse

# # Create your views here.
# def index(request):
#     return render(request,'index.html')
#     #return HttpResponse("This is myhompage")

# def about(request):
#     return render( request,'about.html')

# def login(request):
#     return render( request, 'login.html')

# def market(request):
#     return render(request, 'base.html')

# def contect(request):
#     return HttpResponse("This is contect page")

# myapp/views.py

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import CSVData
from .forms import UploadCSVForm
import csv
import io

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                return render(request, 'upload.html', {'form': form, 'error': 'This is not a CSV file'})

            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip the header row
            for column in csv.reader(io_string, delimiter=',', quotechar='"'):
                _, created = CSVData.objects.update_or_create(
                    name=column[0],
                    age=int(column[1]),
                    subscription_price=float(column[2])
                )
            return redirect('data_display')
    else:
        form = UploadCSVForm()
    return render(request, 'upload.html', {'form': form})

def data_display(request):
    data_list = CSVData.objects.all()
    paginator = Paginator(data_list, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'data_display.html', {'page_obj': page_obj})

def subscription_calculator(request):
    data_list = CSVData.objects.all()
    total_price = sum(item.subscription_price for item in data_list)
    return render(request, 'subscription_calculator.html', {'total_price': total_price})
