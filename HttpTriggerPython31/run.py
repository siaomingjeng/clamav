import os
import json
import pyclamd as p
import platform

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
c=p.ClamdNetworkSocket(host='23.101.216.25')
res=c.scan_stream('')
response.write(postreqdata)
response.close()