from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Student,StudentSerializer
import pandas as pd

# Create your views here.
class StudentView(APIView):
    def post(self,request):
        file = request.FILES.get('file')
        if file:
            # Read Excel file into a DataFrame
            df = pd.read_excel(file)

            # Convert DataFrame to a list of dictionaries
            data = df.to_dict(orient='records')

            # Serialize and save data to the database
            serializer = StudentSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Data imported successfully'}, status=201)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response({'message': 'No file uploaded'}, status=400)
