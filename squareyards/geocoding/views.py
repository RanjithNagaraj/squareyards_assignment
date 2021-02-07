from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import pandas as pd
import geocoder
from django.contrib import messages
import xlwt

KEY = "q60JQBb4IN6OmIhJxArpp8lz2oyVY0Z7"

### Coordinates function to get the latitude and longitude 
def get_coordinate(request:'uploaded file'):
    """Coordinates function to get the latitude and longitude based on the input data from the file
       args: ExcelFile input
       returns ExcelFile with latitude and longitude values"""    
    if request.method == 'POST':        
        myfile = request.FILES['myfile']
        fs = FileSystemStorage('media/geocoding')
        filename = fs.save(myfile.name, myfile)
        if Path(filename).suffix == '.xls' or  Path(filename).suffix == '.xlsx':            
            map_ip = pd.read_excel(fs.path(filename))
            lat_n_lng =  get_lat_lng(map_ip)
            if(isinstance(lat_n_lng, str)):
                return HttpResponse(lat_n_lng)
            else:                                
                response = HttpResponse(content_type='application/ms-excel')            
                response['Content-Disposition'] = 'attachment; filename="lat_lng.xls"'  
                wb = write_output(lat_n_lng)
                wb.save(response)
                return response
        else:
            messages.success(request, "Please upload only .xls or xlsx file")
            return render(request, 'geocoding/index.html')
    return render(request, 'geocoding/index.html')


def get_lat_lng(df:'Dataframe Object'):
    """finds the latitude and longitude values 
       args: Dataframe Object
       returns Mapquest Batch Object """ 
    try:
        lat_n_lng = geocoder.mapquest(df.iloc[:,0], method='batch',key=KEY) 
        return lat_n_lng
    except IndexError:
        return "<h1>Please upload the Correct file</h1>"

def write_output(lat_lng_inp:'mapquest object'):   
    """writes output to the excel file 
       args: batch mapquest object
       returns Excel Workbook Object""" 
    row_num = 0
    wb = xlwt.Workbook(encoding='utf-8')  
    ws = wb.add_sheet("sheet1")    
    font_style = xlwt.XFStyle()    
    font_style.font.bold = True    
    columns = ['Address', 'lat', 'lng', ]   
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)    
    font_style = xlwt.XFStyle()
    for result in lat_lng_inp:
        row_num = row_num + 1
        ws.write(row_num, 0, result.address, font_style)
        ws.write(row_num, 1, result.latlng[0], font_style)
        ws.write(row_num, 2, result.latlng[1], font_style)    
    return wb

    
    

    

        
