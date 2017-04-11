import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from registration.models import *

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


# class StudSubjectTaken(APIView):
#     def get(self, request):
#         c =requests.session()
#         cook = c.cookies['JSESSIONID']
        # cgpa_resp = c.get("https://webkiosk.jiit.ac.in/StudentFiles/Academic/StudSubjectTaken.jsp",
        #                   cookies=request.session['cookie'])
        # print('cookie4', request.session['cookie'])
        # html = BeautifulSoup(cgpa_resp.content, 'html.parser')
        # print(html)
        # return Response(error)
        # rows = html.find_all("table")
        # subjectlists = rows[2].find_all("tr")
        # subject_list = []
        # for subjectlist in subjectlists:
        #     cols = subjectlist.find_all('td')
        #     temp = {"subject": cols[1].text.strip()}
        #     subject_list.append(temp)
        #     print(subject_list)
        # return Response(content)
