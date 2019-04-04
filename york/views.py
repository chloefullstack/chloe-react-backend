from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
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