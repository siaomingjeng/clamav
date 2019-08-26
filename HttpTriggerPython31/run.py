import os
import json
import pyclamd as p
import platform

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
c=p.ClamdNetworkSocket(host='10.0.0.4')
res=c.scan_stream('')
response.write(postreqdata)
response.close()