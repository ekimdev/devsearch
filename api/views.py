from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def get_routes(requets):

    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/project/id'},
        {'POST':'/api/project/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/userssencilla/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)
