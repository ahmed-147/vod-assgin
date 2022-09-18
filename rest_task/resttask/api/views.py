from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser
import pandas as pd

from sites.models import Site
from .serializers import SiteSerializer, RequestSerializer


@api_view(['GET'])
def get_sites(request):
    sites = Site.objects.all()
    serializer = SiteSerializer(sites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upload_sites(request):
    sites = Site.objects.all()
    serializer = SiteSerializer(sites, many=True)
    return Response(serializer.data)


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file_obj = request.FILES['sites']
        df = pd.read_csv(file_obj)
        for index, row in df.iterrows():
            # print(index, row)
            print(row['Active'])

        return Response(status=204)