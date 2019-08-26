import os
import json
import pyclamd as p
import platform

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
c=p.ClamdNetworkSocket(host='52.189.236.53')
res=c.scan_stream('')
response.write(postreqdata)
response.close()