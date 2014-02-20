from pyramid.view import view_config
from pyramid.response import FileResponse
from godsflagga import Godsflagga
import os
from config import REMOVE_LABEL_FILES


@view_config(route_name='home', renderer="templates/index.pt")
def index_view(request):
    #print request.GET
    return {}


@view_config(name='render')
def test_page(request):
    g = Godsflagga(request.GET['part_no'], request.GET['quantity'],
                   request.GET['vendor_lot'], request.GET['vendor_number'],
                   request.GET['serial'], request.GET['description'],
                   request.GET['date'], request.GET['po_number'])

    filedict = g.create()

    response = FileResponse(
        filedict.get('FILENAMEPATH'),
        request=request,
        content_type='application/pdf',
        )
    response.content_disposition = 'attachment; filename="%s"' % filedict.get('FILENAME')

    if REMOVE_LABEL_FILES:
        try:
            os.remove(filedict.get('FILENAMEPATH'))
        except Exception, ex:
            print 'Could not remove file', ex

    return response
