import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
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
