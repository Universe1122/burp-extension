```python

from java.awt import Frame

class test():
    def getBurpFrame(self):

        # java.awt 의 Frame 클래스에서 getFrames() 함수를 통해 모든 frame 목록을 가져옴
        for f in Frame.getFrames():

            # 만약, burp 프로그램의 main frame 을 가져오기 위해서는 아래처럼 찾을 수 있음
            if f.isVisible() and f.getTitle().find(("Burp Suite")) != -1:
                print(f, f.getTitle())

```