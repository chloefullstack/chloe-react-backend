from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PuppyInfo
from .serializers import PuppyInfoSerializer


class PuppyInfoListView(ListAPIView):
    queryset = PuppyInfo.objects.all()
    serializer_class = PuppyInfoSerializer

class PuppyInfoDetailView(RetrieveAPIView):
    queryset = PuppyInfo.objects.all()
    serializer_class = PuppyInfoSerializer

class PuppyInfoCreateView(CreateAPIView):
    queryset = PuppyInfo.objects.all()
    serializer_class = PuppyInfoSerializer
    # permission_classes = (permissions.IsAuthenticated)

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

#         post_info = Posts(
#             name = name,
#             age = age,
#             sex = sex,
#             description = description,
#             updated_at = updated_at
#         )
#         post_info.save()

#     except Exception as e:
#         print(e)
#         return HttpResponse("Failed")