from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import pandas as pd
import geocoder
from django.contrib import messages
import xlwt

KEY = "q60JQBb4IN6OmIhJxArpp8lz2oyVY0Z7"

# Create your views here.
def coordinates(request):
    if request.method == 'POST':
        #print(request.FILES)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage('media/geocoding')
        filename = fs.save(myfile.name, myfile)
        if Path(filename).suffix == '.xls' or  Path(filename).suffix == '.xlsx':            
            map_ip = pd.read_excel(fs.path(filename))  
            try:
                lat_n_lng = geocoder.mapquest(map_ip.iloc[:,0], method='batch',key='q60JQBb4IN6OmIhJxArpp8lz2oyVY0Z7')
            except IndexError:
                return HttpResponse("<h1>Please upload the Correct file</h1>")
            # content-type of response
            response = HttpResponse(content_type='application/ms-excel')
            #decide file name
            response['Content-Disposition'] = 'attachment; filename="lat_lng.xls"'
            #creating workbook
            wb = xlwt.Workbook(encoding='utf-8')
            #adding sheet
            ws = wb.add_sheet("sheet1")
            #Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
	        # headers are bold
            font_style.font.bold = True
            #column header names, you can use your own headers here
            columns = ['Address', 'lat', 'lng', ]
            #write column headers in sheet
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            for result in lat_n_lng:
                row_num = row_num + 1
                ws.write(row_num, 0, result.address, font_style)
                ws.write(row_num, 1, result.latlng[0], font_style)
                ws.write(row_num, 2, result.latlng[1], font_style)
            wb.save(response)           
            return response
        else:
            messages.error(request, "Please upload only .xls or xlsx file")
            return render(request, 'geocoding/index.html')
    return render(request, 'geocoding/index.html')
    

        
