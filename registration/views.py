import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.
content = {
    'error': 0,
    'response': 'success',
    'id': 0
}

error = {
    'error': 1,
    'response': 'fail',
    'id': 0
}


class loginList(APIView):
    def post(self, request):
        data = request.data
        c = requests.Session()
        c.get("https://webkiosk.jiit.ac.in")
        params = {'x': '',
                  'txtInst': 'Institute',
                  'InstCode': 'JIIT',
                  'txtuType': 'Member Type',
                  'UserType': 'S',
                  'txtCode': 'Enrollment No',
                  'MemberCode': data['eno'],
                  'DOB': 'DOB',
                  'DATE1': data['dob'],
                  'txtPin': 'Password/Pin',
                  'Password': data['password'],
                  'BTNSubmit': 'Submit'}
        cook = c.cookies['JSESSIONID']
        cooki = dict(JSESSIONID=cook)
        reslogin = c.post("https://webkiosk.jiit.ac.in/CommonFiles/UserActionn.jsp", data=params, cookies=cooki)
        test = '#### JIIT  [ Signin Action ] '
        html = BeautifulSoup(reslogin.content, 'html.parser')
        if html.title and html.title.string.find(test) == 0:
            return Response(error)
        else:
            return Response(content)
