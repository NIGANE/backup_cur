from rest_framework.decorators import api_view
from rest_framework.response import Response

class Controller:

    @staticmethod
    @api_view(['GET'])
    def index(req):

        print("passed")
        return Response({
            "body": "index results"
        })

    @staticmethod
    @api_view(['POST'])
    def search(req):

        print("search gateway!")
        return Response({
            "body": "search results"
        })