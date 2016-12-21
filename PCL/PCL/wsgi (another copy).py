import os
import sys
import site

# Add python site-packages
site.addsitedir(
    '/home/alamin/.virtualenvs/pcl/lib/python3.5/site-packages')
# site.addsitedir('/home/alamin/.local/lib/python3.5/site-packages')

# your project root directory
sys.path.append(
    '/mnt/340048A400486EC4/Dropbox/Programming/Django/PCL_Project/PCL/PCL')

# directory where your settings.py file is located
sys.path.append(
    '/mnt/340048A400486EC4/Dropbox/Programming/Django/PCL_Project/PCL/PCL/PCL')





# # Activate your virtual env
# activate_env = os.path.expanduser(
#     "~/.virtualenvs/eonushilon/bin/activate_this.py")
# print("\n\n in wsgi file \n")
# print(sys.path)
# os.environ["DJANGO_SETTINGS_MODULE"] = "PCL.settings"
# os.environ.setdefault["DJANGO_SETTINGS_MODULE"] = "PCL.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PCL.settings")

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
