from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

<<<<<<< HEAD
        serializer['age'] = 12
        serializer.save()
        return serializer
# class PuppyInfoList(APIView):
=======
#我们可以用这种方法去 手动接收 request
@api_view(['POST'])
def snippet_list(request):
    serializer = PuppyInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def createInfo(request):
#     try:
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         sex = request.POST.get('sex')
#         description = request.POST.get('description')
#         updated_at = request.POST.get('updated_at')
>>>>>>> d194a7b31b93e27fec547caac6f5881ac03b53bb

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