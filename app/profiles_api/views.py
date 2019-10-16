from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API VIEW"""

    def get(self, request, format=None):
        """Returns a list of APIView objects"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({"message": "hello", "an_api_view": an_apiview})
