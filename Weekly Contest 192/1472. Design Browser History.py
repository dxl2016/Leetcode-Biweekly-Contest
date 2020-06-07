class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = Node(homepage)
        return
    
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newnode = Node(url)
        self.head.next = newnode
        newnode.prev = self.head
        self.head = self.head.next
        return
    
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.head.prev:
                self.head = self.head.prev
        return self.head.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.head.next:
                self.head = self.head.next
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
