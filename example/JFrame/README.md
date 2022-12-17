## 1. frame 창 닫기 event Handler

windowClosing 속성을 사용하여 handler 함수 이름을 작성한다.

```python

from javax.swing import JFrame, JButton

frame = JFrame('Hello, Jython!',
    size = (300, 300)
)
frame.setLocationRelativeTo(None)
# windowClosing 속성을 통해 handler 함수 이름을 작성
frame.windowClosing = onClose

button = JButton(get_data)
frame.add(button)
frame.visible = True

def onClose(event):
    print("close")

```

## 2. 실행된 main frame 위에 다른 frame 띄우기

여러대의 모니터를 사용할 경우, frame 의 출력 위치를 어디에 해야할지 정하기 어렵다.

따라서 실행된 프로그램 위에 다른 frame을 띄우는 방법은 다음과 같다.

`setLocationRelativeTo()` 함수의 인자로 frame 객체를 넘기면 된다. 이때 frame 객체는 `getBurpFrame()` 함수를 통해 원하는 frame 객체를 얻을 수 있다.

예를 들어, burp 프로그램의 main frame을 얻고 싶다면, `getTitle()` 함수를 통해 해당 frame의 제목을 검사하여 원하는 frame을 가져온다.

```python

from javax.swing import JFrame, JButton
from java.awt import Frame

frame = JFrame('Hello, Jython!',
    size = (300, 300)
)
frame.setLocationRelativeTo(getBurpFrame())

def getBurpFrame():
    for f in Frame.getFrames():
        if f.isVisible() and f.getTitle().find(("Burp Suite")) != -1:
            return f
    
    return None

```