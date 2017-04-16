import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView

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


class StudSubjectTaken(APIView):
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
            content['id'] = data['eno']
            cgpa_resp = c.get("https://webkiosk.jiit.ac.in/StudentFiles/Academic/StudSubjectTaken.jsp", cookies=cooki)
            html = BeautifulSoup(cgpa_resp.content, 'html.parser')
            rows = html.find_all("table")
            subjectlists = rows[2].find_all("tr")
            subject_list = []
            for subjectlist in subjectlists:
                cols = subjectlist.find_all('td')
                temp = {
                    "Subject": cols[1].text.strip(), "Credits": cols[2].text.strip()}
                # }
                subject_list.append(temp)
            content['data'] = subject_list
            return Response(content)


class StudCGPAReport(APIView):
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
            content['id'] = data['eno']
            sgpa_resp = c.get("https://webkiosk.jiit.ac.in/StudentFiles/Exam/StudCGPAReport.jsp", cookies=cooki)
            html = BeautifulSoup(sgpa_resp.content, 'html.parser')
            rows = html.find_all("table")
            SGPA = rows[2].find_all("tr")
            SGPA_LIST = []
            for val in SGPA:
                cols = val.find_all('td')
                temp = {
                    "Semester": cols[0].text.strip(), "Grade Points": cols[1].text.strip(),
                    "Course Credit": cols[2].text.strip(),
                    "Earned Credits": cols[3].text.strip(),
                    "Points Secured SGPA": cols[4].text.strip(),
                    "Points Secured CGPA": cols[5].text.strip(),
                    "SGPA": cols[6].text.strip(),
                    "CGPA": cols[7].text.strip()}
                SGPA_LIST.append(temp)
            content['data'] = SGPA_LIST
            return Response(content)


class StudSubjectFaculty(APIView):
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
            content['id'] = data['eno']
            teacher_resp = c.get("https://webkiosk.jiit.ac.in/StudentFiles/Academic/StudSubjectFaculty.jsp",
                                 cookies=cooki)
            html = BeautifulSoup(teacher_resp.content, 'html.parser')
            rows = html.find_all("table")
            teacher = rows[2].find_all("tr")
            teacher_list = []
            for val in teacher:
                cols = val.find_all('td')
                temp = {
                    "Subject": cols[1].text.strip(),
                    "Faculty(Lecture)": cols[2].text.strip(),
                    "Faculty(Tutorial)": cols[3].text.strip(),
                    "Faculty(Practical)": cols[4].text.strip()}
                teacher_list.append(temp)
            content['data'] = teacher_list
            return Response(content)


class StudentEventGradesView(APIView):
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
            content['id'] = data['eno']
            form = {
                'x': '',
                'exam': data['exam']
            }
            grade = c.get("https://webkiosk.jiit.ac.in/StudentFiles/Exam/StudentEventGradesView.jsp", params=form,
                          cookies=cooki)
            html = BeautifulSoup(grade.content, 'html.parser')
            rows = html.find_all("table")
            subjects = rows[2].find_all("tr")
            subject_list = []
            for val in subjects:
                cols = val.find_all('td')
                temp = {
                    "Subject": cols[1].text.strip(),
                    "EXAM CODE": cols[2].text.strip(),
                    "GRADE AWARDED": cols[3].text.strip()}
                subject_list.append(temp)
            content['data'] = subject_list
            return Response(content)
