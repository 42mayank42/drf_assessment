from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import render
from django.http import JsonResponse

from .models import File

from .serializers import FileSerializer, MultipleFileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        """Upload multiple files and create objects."""
        serializer = MultipleFileSerializer(data=request.data or None)
        serializer.is_valid(raise_exception=True)
        files = serializer.validated_data.get("files")

        files_list = []
        for file in files:
            files_list.append(
                FileModel(file=file)
            )
        if files_list:
            FileModel.objects.bulk_create(files_list)

        return Response("Success")





def single_upload(request):
    file = request.FILES.get("file")
    File.objects.create(file=file)
    return JsonResponse({"message": "Success"})


def multiple_upload(request):
    files = request.FILES.getlist("files")

    files_list = []
    for file in files:
        files_list.append(File(file=file))

    if files_list:
        File.objects.bulk_create(files_list)

    return JsonResponse({"message": "Success"})


def index(request):
    return render(template_name="index.html", request=request)