from django.shortcuts import render
# parsing imports
from django.contrib import messages
from tablib import Dataset
import io
import csv
from .models import Phones
from .resources import PhonesResource

# Create your views here.
def parsing(request):
    if request.method == "POST":
        phones_resource = PhonesResource()
        dataset = Dataset()
        new_phones = request.FILES["myfile"]

        if not new_phones.name.endswith("csv"):
            messages.info(request, "wrong format")
            return render(request, "upload.html")
        
        data_set = new_phones.read().decode("UTF-8")
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=",", quotechar="|"):
            created = Phones.objects.update_or_create(model=column[0])
    return render(request, "parse.html")