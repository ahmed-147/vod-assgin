import uuid
import pandas as pd
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.parsers import MultiPartParser
from django.conf import settings

from django_filters.rest_framework import DjangoFilterBackend
from sites.models import Site, Request
from .serializers import SiteSerializer, RequestSerializer


class SiteList(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['region', 'active']


class FileImportExportView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            file_obj = request.FILES['sites']
        except :
            raise ValidationError("You must add file with name[sites], type[csv]")
        if file_obj.content_type != 'text/csv':
            raise ValidationError("Your file must be a CSV type")
        try:
            df = pd.read_csv(file_obj)
        except:
            raise ParseError("check the file content")

        sites = []
        for index, row in df.iterrows():

            site_exist = Site.objects.filter(name=row['SiteName']).exists()
            site_len_check = len(row['SiteName']) <= 20
            region_len_check = len(row['Region']) <= 50
            type(row['Latitude'])
            if isinstance(row['Latitude'], str):
                latitude_float_check = row['Latitude'].replace('.', '',1).isdigit()
            elif isinstance(row['Latitude'], float):
                latitude_float_check = True
            else:
                latitude_float_check = False

            if isinstance(row['Longitude'], str):
                longitude_float_check = row['Longitude'].replace('.', '',1).isdigit()
            elif isinstance(row['Longitude'], float):
                longitude_float_check = True
            else:
                longitude_float_check = False

            active_check = (row['Active'] == 'yes' or row['Active'] == 'no')

            if site_exist:
                raise ValidationError(('line %s : SiteName (%s) already exist.')%(index+1, row['SiteName']))
            if not site_len_check:
                raise ValidationError(('line %s : SiteName (%s) length greater than 20 characters.')%(index+1, row['SiteName']))
            if not region_len_check:
                raise ValidationError(('line %s : Region (%s) length greater than 50 characters.') % (index+1, row['Region']))
            if not latitude_float_check:
                raise ValidationError(('line %s : Latitude (%s) is not float.') % (index+1, row['Latitude']))
            if not longitude_float_check:
                raise ValidationError(('line %s : Longitude (%s) is not float.') % (index+1, row['Longitude']))
            if not active_check:
                raise ValidationError(('line %s : Active (%s) must be (yes/no) --> (y,Yes,n,No) not accepted.') % (index+1, row['Active']))

            if not site_exist and site_len_check and region_len_check and latitude_float_check and longitude_float_check and active_check:
                sites.append(Site(name=row['SiteName'], region=row['Region'], latitude=row['Latitude'],
                                  longitude=row['Longitude'], active=row['Active']))
            # sites.append(Site(name=row['SiteName'], region=row['Region'], latitude=float(row['Latitude']),
            #                   longitude=float(row['Longitude']), active=row['Active']))
        if len(df.index) == len(sites):
            created_sites = Site.objects.bulk_create(sites)
            serializer = SiteSerializer(created_sites, many=True)
            return Response(serializer.data, status=201)
        else:
            raise ValidationError('upload file not match the requirements ')

    def get(self, request):
        sites = Site.objects.all()
        data=[]
        for site in sites:
            data.append({
                'SiteName': site.name,
                'Region': site.region,
                'Latitude': float(site.latitude),
                'Longitude': float(site.longitude),
                'Active': site.active,
            })

        serializer = SiteSerializer(sites, many=True)
        df = pd.DataFrame(data)
        df.to_csv(f'{settings.MEDIA_ROOT}/{uuid.uuid4()}.csv', encoding='utf-8',index=False)
        return Response(serializer.data, status=200)


class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
