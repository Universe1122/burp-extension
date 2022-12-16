```python
## Reference https://gist.github.com/stefanocoding/d302f29a417a43b4f880e432b9ad1962

from burp import IBurpExtender, IContextMenuFactory, IContextMenuInvocation
from javax.swing import JMenuItem
from java.io import PrintWriter

class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Add Context Menu Example")
        callbacks.registerContextMenuFactory(self)
        self.stdout = PrintWriter(callbacks.getStdout(), True)
        
    
    """
        https://portswigger.net/burp/extender/api/
        이 함수는 IContextMenuFactory 인터페이스에 있는 함수이다.
        사용자가 Context Menu를 호출할 때 이 함수가 호출된다.
    """
    def createMenuItems(self, invocation):
        
        # getInvocationContext() https://portswigger.net/burp/extender/api/burp/IContextMenuInvocation.html#getInvocationContext--
        # 함수는 Menu가 호출된 Context를 찾는데 사용된다.
        # 예를 들어, Proxy의 History Context에 호출되었는지를 확인할 수 있다.
        context = invocation.getInvocationContext()
        
        if context == IContextMenuInvocation.CONTEXT_MESSAGE_EDITOR_REQUEST or context == IContextMenuInvocation.CONTEXT_MESSAGE_VIEWER_REQUEST or context == IContextMenuInvocation.CONTEXT_PROXY_HISTORY:

            # 메뉴 이름
            label = "test"

            # 사용자가 메뉴를 클릭했을 때, self.callFunction() 이라는 함수를 호출하기 위해 callback 인자로 준다.
            menuItem = JMenuItem(label, actionPerformed = self.callFunction)

            # 사용자가 메뉴를 클릭했을 때, 예를 들어 해당 패킷의 정보를 저장했다가 가져올 때 사용된다.
            # test22 는 key 이름, aa는 해당 key에 대한 value 값이다.
            menuItem.putClientProperty("test22", "aa")

            return [menuItem]
        
    
    def callFunction(self, event):
        menuItem = event.getSource()

        # 위에서 putClientProperty() 함수를 통해 저장한 값을 가져온다.
        get_data = menuItem.getClientProperty("test22")

        # 가져온 값을 output console에 출력한다.
        self.stdout.println(get_data)
```