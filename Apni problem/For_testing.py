import time
from datetime import datetime
# import time
#
time_star=datetime.now().strftime('%S')
time.sleep(2)
time_end=datetime.now().strftime('%S')
# print(datetime.now().strftime('%S'))
if int(time_end)-int(time_star)<2:
    print("fd")