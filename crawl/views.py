import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from registration.models import *

content = [
    {
        'error': 0,
        'response': 'success',
        'id': 0
    }
]

error = [
    {
        'error': 1,
        'response': 'fail',
        'id': 0
    }
]


class StudSubjectTaken(APIView):
    def get(self,request):
        c = requests.Session()
        # cook = c.cookies['JSESSIONID']
        cooki = {'JSESSIONID': Cookie.objects.get(enrollment='14103179').cookie}
        cgpa_resp = c.get("https://webkiosk.jiit.ac.in/StudentFiles/Academic/StudSubjectTaken.jsp", cookies=cooki)
        html = BeautifulSoup(cgpa_resp.content, 'html.parser')
        rows = html.find_all("table")
        subjectlists = rows[2].find_all("tr")
        subject_list = []
        for subjectlist in subjectlists:
            cols = subjectlist.find_all('td')
            temp = {"subject": cols[1].text.strip()}
            subject_list.append(temp)
            print(subject_list)
        return Response(content)
