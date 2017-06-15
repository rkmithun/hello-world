import time
start_time = time.time()

time.asctime()

params = {'query': 'like%COMP%', 'fields': 'date,name,age', }

def display_params ( **kwargs):
    for key,value in kwargs.iteritems():
        print ("Key=%s Value=%s" % (key,value))
        

records = list()

records.append(params)
print ("Records")
print records      
        
records.append(params)
print ("Records")
print records       

    
display_params(**params)
