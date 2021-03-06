"""
This package contains classes necessary for input parsing OGC WPS requests,
working with list of processes, executing them and redirecting OGC WPS
responses back to client.
"""

import os
from lxml.builder import ElementMaker

PYWPS_INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))

NAMESPACES = {
    'xlink': "http://www.w3.org/1999/xlink",
    'wps': "http://www.opengis.net/wps/1.0.0",
    'ows': "http://www.opengis.net/ows/1.1",
    'gml': "http://www.opengis.net/gml",
    'xsi': "http://www.w3.org/2001/XMLSchema-instance"
}

E = ElementMaker()
WPS = ElementMaker(namespace=NAMESPACES['wps'], nsmap=NAMESPACES)
OWS = ElementMaker(namespace=NAMESPACES['ows'], nsmap=NAMESPACES)

XMLSCHEMA_2 = "http://www.w3.org/TR/xmlschema-2/#"

class PyWPS:
    """OGC Web Processsing Service  implementation
    """

    pass


from pywps.inout import *
from pywps.app import *

if __name__ == "__main__":
    pass

