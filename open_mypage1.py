import webbrowser
import os

myuri='file://'+'localhost'+os.path.join(os.getcwd(), 'src/mypage1.html')
webbrowser.open(myuri)
# uri형식을 지키지 않으면 안된다.
# webbrowser.open('mypage.html')