from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import PuppyInfo
from .serializers import PuppyInfoSerializer, CreatePuppyInfoSerializer
from rest_framework.decorators import action
from rest_framework import renderers, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class PuppyInfoListView(ListAPIView):
    queryset = PuppyInfo.objects.all()
    serializer_class = PuppyInfoSerializer

class PuppyInfoDetailView(RetrieveAPIView):
    queryset = PuppyInfo.objects.all()
    serializer_class = PuppyInfoSerializer

class PuppyInfoCreateView(CreateAPIView):
    queryset = PuppyInfo.objects.all()
    serializer_class = CreatePuppyInfoSerializer
    # permission_classes = (permissions.IsAuthenticated)
    def post(self, request, format = None):
        serializer = CreatePuppyInfoSerializer

        serializer['age'] = 12
        serializer.save()
        return serializer
# class PuppyInfoList(APIView):

#     def get(self, request, format = None):
#         puppyInfo = PuppyInfo.objects.all()
#         serializer = CreatePuppyInfoSerializer(puppyInfo, many=True)
#         return Response(serializer.data)
#     def post(self, request, format = None):
#         serializer = CreatePuppyInfoSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer['age'] = 12
#             serializer.save()

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)