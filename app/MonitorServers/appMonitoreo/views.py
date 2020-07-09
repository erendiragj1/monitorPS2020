from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .clases import Monitor
from .serializers import monitorSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .monitor import *
import json
import logging
from django.conf import settings

#PATH_LOG: Se define en el archivo de settings.py
logging.basicConfig(filename=settings.PATH_LOG,
                    format='%(asctime)s %(message)s', level=logging.DEBUG)


# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_datos(request):
    logging.info('login: Se hace petición por el método: ' + request.method)
    if request.method == "GET":
        cpu = dar_uso_cpu()
        memoria = dar_uso_memoria()
        disco = dar_uso_disco()
        datos_raw = Monitor(cpu,memoria,disco)
        logging.info('login: datos: ' + str(datos_raw))
        serialisador = monitorSerializer(datos_raw)
        datosServer = JSONRenderer().render(serialisador.data)
        return Response(datosServer)

