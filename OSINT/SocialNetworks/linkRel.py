# File: linkRel.py
# Date: 2017/08/18
# Author: Simon Roses Femerling
# Desc: SImple Google Hacking
#
# VULNES (C) 2013
# www.vulnes.com

import request
import json 
import urllib
import const

site = "https://www.googleapis.com/customsearch/v1?key="

# Your Google Hacking query
query = ''
query_params = ''

url = site+const.cse_token + "&cx=" + const.cse_id + urllib.quote(query+query_params)
response = request.get(url)
print json.dumps(response.json,indent=4)