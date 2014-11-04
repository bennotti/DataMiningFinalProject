__author__ = 'shreyarajani'

from pydap.client import open_url
dataset = open_url('http://test.opendap.org/dap/data/nc/coads_climatology.nc')
#print type(dataset)
print dataset