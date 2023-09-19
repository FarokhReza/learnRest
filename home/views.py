# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
# @api_view(['GET', 'POST']) # by default is get
# def home(request):
#     return Response({'name':'amir'})

class Home(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):

        # 
        # name = request.GET['name']
        # name = request.query_params['name']
        persons = Person.objects.all() # query set
        
        ser_data = PersonSerializer(instance=persons, many=True)

        return Response(data=ser_data.data)
    
    # def post(self, request):
    #     name = request.data['name']
    #     # all = request.data
    #     return Response({'name': name})



class QuestionView(APIView):

    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data   , status=status.HTTP_200_OK)

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data) # or data=request.POST

        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        # srz_data = QuestionSerializer()
        question.delete()

        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)