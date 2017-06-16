from tkinter import *
from tkinter import font
import tkinter.messagebox

host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"
##############
g_Tk = Tk()
g_Tk.geometry("400x800+750+10")  # 윈도우의 크기
DataList = []###


def image():  # 맨위에 이미지 함수
    photo = PhotoImage(file = "비행기.gif")
    imageLabel = Label(g_Tk, image = photo)
    imageLabel.configure(image = photo)
    imageLabel.image = photo
    imageLabel.pack()
    imageLabel.place(x=200, y = 45)


def InitTopText():  # 맨위에 라벨 만드는 함수
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="[인천공항 정보 검색 App]")
    MainText.pack()
    MainText.place(x=20)


def InitSearchListBox():  # 4가지 카테고리 (도서관,모범음식점,마트,문화공간) 리스트를 만듬
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)  # 옆에 스크롤바를 갖고있음
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "공항 시설")
    SearchListBox.insert(2, "승객 예고")
    SearchListBox.insert(3, "여객편 현황")
    SearchListBox.insert(4, "취항 항공사 현황")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)


def InitInputLabel():  # 입력라벨 (ENTRY) 만드는 부분
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=145)


def InitSearchButton():  # 검색 버튼
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색",
                          command=SearchButtonAction)  # SearchButtonAction이라는 함수 연결, 버튼누르자마자 이 함수 실행됨
    SearchButton.pack()
    SearchButton.place(x=330, y=150)


def SearchButtonAction():  # 검색 버튼 눌렀을때 실행되는 함수
    global SearchListBox

    RenderText.configure(state='normal')  # RenderText(텍스트뷰) 한번 클리어하고 넣는다는데
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchFacillity()
    elif iSearchIndex == 1:
        SearchPassenger()
    elif iSearchIndex == 2:
        SearchFlight()
    elif iSearchIndex == 3:
        SearchAirLine()

    RenderText.configure(state='disabled')


############################################################################################################Gmail 연동

def RecipientInputID():  # 받는 아이디 입력
    global RecipientInputID
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    RecipientInputID = Entry(g_Tk, font=TempFont, width=20, borderwidth=12, relief='ridge')
    RecipientInputID.pack()
    RecipientInputID.place(x=70, y=700)

def RecipientIDText():  # 아이디 텍스트
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    RecipientIDText = Label(g_Tk, font=TempFont, text="[받는ID]")
    RecipientIDText.pack()
    RecipientIDText.place(x=5, y=710)


def InputID():  # 아이디 입력
    global InputID
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputID = Entry(g_Tk, font=TempFont, width=20, borderwidth=12, relief='ridge')
    InputID.pack()
    InputID.place(x=70, y=600)
def IDText():  # 아이디 텍스트
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    IDText = Label(g_Tk, font=TempFont, text="[ID]")
    IDText.pack()
    IDText.place(x=8, y=605)


def InputPW():  # 패스워드 입력
    global InputPW
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputPW = Entry(g_Tk, font=TempFont, width=20, borderwidth=12, relief='ridge')
    InputPW.pack()
    InputPW.place(x=70, y=650)

def PWText():  # 패스워드 텍스트
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    PWText = Label(g_Tk, font=TempFont, text="[PW]")
    PWText.pack()
    PWText.place(x=8, y=655)

def SendEmailButton():  # 발송 버튼
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SendEmailButton = Button(g_Tk, font=TempFont, text="발송",
                          command=SendEmailButtonAction)  # SearchButtonAction이라는 함수 연결, 버튼누르자마자 이 함수 실행됨
    SendEmailButton.pack()
    SendEmailButton.place(x=330, y=715)

def SendEmailButtonAction():  # 검색 버튼 눌렀을때 실행되는 함수

    global host, port

    html = str(DataList)
    title = InputLabel.get()
    senderAddr = InputID.get()
    msgtext = " "
    passwd = InputPW.get()
    recipientAddr = RecipientInputID.get()


    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain', 'UTF-8')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


##########################################################################################################################


def SearchFacillity():  # 씹중요한 함수 오픈Api 커넥션해서 필요한정보 긁어내서 화면에보여줌 바로여기서
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.airport.kr")
    conn.request("GET", "/openapi/service/StatusOfFacility/getFacilityKR?ServiceKey=f3k1zJymAnxkgWM0aMwAaWBekcbjNqqCjOGf5yTTCTya4qmfG1NQwmGfh2l7C26x8Tj4wJnXKh6gMujoWsJ8Lw%3D%3D&")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        print("200")
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes  # 첫번째 루트엘리멘트
            body = response[0].childNodes  # 거기서 또 차일드노드를 갖고와

            for item in body:
                if item.nodeName == "body":
                    items = item.childNodes  # row면 또 차일드노드를 갖고옴
            target = items[0].childNodes
            for realtarget in target:
                subitems = realtarget.childNodes
                if subitems[0].firstChild.nodeValue == InputLabel.get():
                    print("==============================")
                    print(subitems[0].firstChild.nodeValue)
                    print(subitems[1].firstChild.nodeValue)
                    print(subitems[2].firstChild.nodeValue)
                    print(subitems[3].firstChild.nodeValue)
                    print(subitems[4].firstChild.nodeValue)
                    print("==============================")
                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue,
                                     subitems[2].firstChild.nodeValue, subitems[3].firstChild.nodeValue,
                                     subitems[4].firstChild.nodeValue
                                     ))
            for i in range(0, (len(DataList))):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "매장명: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "위치: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "서비스 시간: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "Tel ☎: ")
                RenderText.insert(INSERT, DataList[i][3])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "취급 품목  : ")
                RenderText.insert(INSERT, DataList[i][4])
                RenderText.insert(INSERT, "\n\n")

                RenderText.insert(INSERT, "\n\n")

def SearchPassenger():  # 씹중요한 함수 오픈Api 커넥션해서 필요한정보 긁어내서 화면에보여줌 바로여기서
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.airport.kr")
    conn.request("GET", "/openapi/service/PassengerNoticeKR/getfPassengerNoticeIKR?ServiceKey=f3k1zJymAnxkgWM0aMwAaWBekcbjNqqCjOGf5yTTCTya4qmfG1NQwmGfh2l7C26x8Tj4wJnXKh6gMujoWsJ8Lw%3D%3D&selectdate=0")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        print("200")
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes  # 첫번째 루트엘리멘트
            body = response[0].childNodes  # 거기서 또 차일드노드를 갖고와

            for item in body:
                if item.nodeName == "body":
                    items = item.childNodes  # row면 또 차일드노드를 갖고옴
            target = items[0].childNodes
            for realtarget in target:
                subitems = realtarget.childNodes
                if subitems[0].firstChild.nodeValue == InputLabel.get():
                    print("==============================")
                    print(subitems[0].firstChild.nodeValue)
                    print(subitems[1].firstChild.nodeValue)
                    print(subitems[2].firstChild.nodeValue)
                    print(subitems[3].firstChild.nodeValue)
                    print(subitems[4].firstChild.nodeValue)
                    print(subitems[5].firstChild.nodeValue)
                    print(subitems[6].firstChild.nodeValue)
                    print(subitems[7].firstChild.nodeValue)
                    print(subitems[8].firstChild.nodeValue)
                    print(subitems[9].firstChild.nodeValue)
                    print(subitems[10].firstChild.nodeValue)
                    print(subitems[11].firstChild.nodeValue)
                    print("==============================")
                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue,
                                     subitems[2].firstChild.nodeValue, subitems[3].firstChild.nodeValue,
                                     subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                     subitems[6].firstChild.nodeValue, subitems[7].firstChild.nodeValue,
                                     subitems[8].firstChild.nodeValue, subitems[9].firstChild.nodeValue,
                                     subitems[10].firstChild.nodeValue, subitems[11].firstChild.nodeValue
                                     ))
            for i in range( len(DataList)):
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, "표출일자: ")
                    RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "시간대: ")
                    RenderText.insert(INSERT, DataList[i][1])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "입국장 동편(A, B): ")
                    RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "입국장 서편(C, D) : ")
                    RenderText.insert(INSERT, DataList[i][3])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "입국심사(C)  : ")
                    RenderText.insert(INSERT, DataList[i][4])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "입국심사(D)  : ")
                    RenderText.insert(INSERT, DataList[i][5])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "입국장 합계  : ")
                    RenderText.insert(INSERT, DataList[i][6])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출국장(1, 2)  : ")
                    RenderText.insert(INSERT, DataList[i][7])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출국장(3)  : ")
                    RenderText.insert(INSERT, DataList[i][8])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출국장(4)  : ")
                    RenderText.insert(INSERT, DataList[i][9])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출국장(5, 6)  : ")
                    RenderText.insert(INSERT, DataList[i][10])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출국장 합계  : ")
                    RenderText.insert(INSERT, DataList[i][11])
                    RenderText.insert(INSERT, "\n")

                    RenderText.insert(INSERT, "\n\n")
def SearchFlight():  # 씹중요한 함수 오픈Api 커넥션해서 필요한정보 긁어내서 화면에보여줌 바로여기서
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.airport.kr")
    conn.request("GET", "/openapi/service/StatusOfPassengerFlightsDS/getPassengerArrivalsDS?ServiceKey=f3k1zJymAnxkgWM0aMwAaWBekcbjNqqCjOGf5yTTCTya4qmfG1NQwmGfh2l7C26x8Tj4wJnXKh6gMujoWsJ8Lw%3D%3D&airport_code=" + InputLabel.get())
    req = conn.getresponse()
    j = 0
    global DataList
    DataList.clear()

    if req.status == 200:
        print("200")
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes  # 첫번째 루트엘리멘트
            body = response[0].childNodes  # 거기서 또 차일드노드를 갖고와

            for item in body:
                if item.nodeName == "body":
                    items = item.childNodes  # row면 또 차일드노드를 갖고옴
            target = items[0].childNodes
            for realtarget in target:
                subitems = realtarget.childNodes
                if subitems[2].firstChild.nodeValue == InputLabel.get():
                  if len(subitems) == 10:
                    print("==============================")
                    print(subitems[0].firstChild.nodeValue)
                    print(subitems[1].firstChild.nodeValue)
                    print(subitems[2].firstChild.nodeValue)
                    print(subitems[3].firstChild.nodeValue)
                    print(subitems[4].firstChild.nodeValue)
                    print(subitems[5].firstChild.nodeValue)
                    print(subitems[6].firstChild.nodeValue)
                    print(subitems[7].firstChild.nodeValue)
                    print(subitems[8].firstChild.nodeValue)
                    print(subitems[9].firstChild.nodeValue)
                    print(len(subitems))
                    print("==============================")

                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue,
                                     subitems[2].firstChild.nodeValue, subitems[3].firstChild.nodeValue,
                                     subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                     subitems[6].firstChild.nodeValue, subitems[7].firstChild.nodeValue,
                                     subitems[8].firstChild.nodeValue, subitems[9].firstChild.nodeValue,
                                     ))


            for i in range(len(DataList)):
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, "항공사: ")
                    RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출발 공항: ")
                    RenderText.insert(INSERT, DataList[i][1])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "공항코드: ")
                    RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "수하물 수취대: ")
                    RenderText.insert(INSERT, DataList[i][3])
                    RenderText.insert(INSERT, "변경시간  : ")
                    RenderText.insert(INSERT, DataList[i][4])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "출구  : ")
                    RenderText.insert(INSERT, DataList[i][5])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "편명  : ")
                    RenderText.insert(INSERT, DataList[i][6])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "탑승구  : ")
                    RenderText.insert(INSERT, DataList[i][7])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "현황  : ")
                    RenderText.insert(INSERT, DataList[i][8])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "예정시간  : ")
                    RenderText.insert(INSERT, DataList[i][9])
                    RenderText.insert(INSERT, "\n")

                    RenderText.insert(INSERT, "\n\n")



def SearchAirLine():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.airport.kr")
    conn.request("GET",
                 "/openapi/service/StatusOfSrvAirlines/getServiceAirlineInfo?ServiceKey=f3k1zJymAnxkgWM0aMwAaWBekcbjNqqCjOGf5yTTCTya4qmfG1NQwmGfh2l7C26x8Tj4wJnXKh6gMujoWsJ8Lw%3D%3D")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        print("200")
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes  # 첫번째 루트엘리멘트
            body = response[0].childNodes  # 거기서 또 차일드노드를 갖고와

            for item in body:
                if item.nodeName == "body":
                    items = item.childNodes  # row면 또 차일드노드를 갖고옴
            target = items[0].childNodes
            for realtarget in target:
                subitems = realtarget.childNodes
                if subitems[4].firstChild.nodeValue == InputLabel.get():
                    print("==============================")
                    print(subitems[3].firstChild.nodeValue)
                    print(subitems[1].firstChild.nodeValue)
                    print(subitems[2].firstChild.nodeValue)
                    print(subitems[3].firstChild.nodeValue)
                    print(subitems[0].firstChild.nodeValue)
                    print(subitems[5].firstChild.nodeValue)
                    print("==============================")
                    DataList.append((subitems[3].firstChild.nodeValue, subitems[4].firstChild.nodeValue,  # 이미지 , 이름
                                     subitems[1].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                     # 대표연락처 , 공항연락처
                                     subitems[0].firstChild.nodeValue, subitems[2].firstChild.nodeValue
                                     # IATA 코드 ICAO 코드
                                     ))

                """ 이미지 어케띄움
                    url = subitems[3].firstChild.nodeValue
                    print(url)

                    with urllib.request.urlopen(url) as u:
                        raw_data = u.read()

                    im = Image.open(BytesIO(raw_data))
                    image = ImageTk.PhotoImage(im)

                    label = Label(g_Tk, image=image, height=400, width=400)
                    label.pack()
                    label.place(x=0, y=0)
                """

        for i in range(0, len(DataList)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "항공사 이미지: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, " 항공사 이름 : ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "대표 연락처 ☎: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "공항 연락처 ☎: ")
                RenderText.insert(INSERT, DataList[i][3])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "IATA 코드 : ")
                RenderText.insert(INSERT, DataList[i][4])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "ICAO 코드 : ")
                RenderText.insert(INSERT, DataList[i][5])
                RenderText.insert(INSERT, "\n\n")

                RenderText.insert(INSERT, "\n\n")
def InitRenderText():  # 텍스트뷰, 여기에 리스트박스 내용을 여기다 Wirte 함
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
InputID()
IDText()
InputPW()
PWText()
RecipientInputID()
RecipientIDText()
SendEmailButton()
image()

# InitSortListBox()
# InitSortButton()

g_Tk.mainloop()