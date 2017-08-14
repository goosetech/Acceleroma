


import os
import datetime
from time import sleep
from subprocess import call 


call('fswebcam -r 1920x1080 --no-banner ~/Projects/GooseTech/Accelerom/images/%Y-%m-%d_%H:%M:%S.jpg', shell=True)
call('git add -A', shell=True)
call('git commit -m "Uploading image"', shell=True)
call('git push acceleroma master', shell=True)

