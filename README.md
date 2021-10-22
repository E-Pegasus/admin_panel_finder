# admin_panel_finder
The script will try to request possible admin panels
by reading possible admin panels url then report 
as 200 YES or 404 NO

usage:
python3 admin_finder.py <url> <option>

example:
   python3 admin_finder.py http://E-Pegasus.net:8000
   python3 admin_finder.py https://google.com
   python3 admin_finder.py https://yahoo.com -l

make sure to requests is installed
to install requests: pip install requests
