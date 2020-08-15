from datetime import datetime

now = datetime.now()
#24-hour format
print(now.strftime('%Y/%m/%d %H:%M:%S'))

#12-hour format
print(now.strftime('%Y/%m/%d %I:%M:%S'))