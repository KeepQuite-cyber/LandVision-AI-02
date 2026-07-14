from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import ChatRequestSerializer
from .agent import AIAgent


class AIChatAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ChatRequestSerializer( data=request.data)
        serializer.is_valid(  raise_exception=True)
        message = serializer.validated_data["message"]
        response = AIAgent.chat(session_id='default', message=message)
        return Response(response)