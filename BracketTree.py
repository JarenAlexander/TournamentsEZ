class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.parent = None
        self.right = None
        self.score = None

class Tree():
    def __init__(self):
        self.root = None

    def add(self, data):

        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            myqueue = []
            treeNode = self.root
            myqueue.append(treeNode)
            while myqueue:
                treeNode = myqueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    treeNode.left.parent = treeNode
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    treeNode.right.parent = treeNode
                    return
                else:
                    myqueue.append(treeNode.left)
                    myqueue.append(treeNode.right)
    def BFS(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)

        while queue:
            now_node = queue.pop(0)
            print(now_node.data)
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)

    def setWinner(self, player, score):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            now_node = queue.pop(0)
            if now_node.data == player:
                now_node.parent.data = player
                now_node.parent.score = score
                return
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)

    def removePlayer(self, player):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            now_node = queue.pop(0)
            if now_node.data == player:
                if now_node == now_node.parent.left:
                    now_node.parent.left = None
                    return
                elif now_node == now_node.parent.right:
                    now_node.parent.right = None
                    return
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)



def insertPlayer(playerlist):
    tree = Tree()
    l = len(playerlist)
    for i in range(1, l * 2):
        if i < l:
            tree.add("TBD")
        else:
            tree.add(playerlist[l*2 - i-1])
    
    return tree
'''
# this is for testing the code
def test():
    teamlist = ["1","2","3","4"]
    t = insertPlayer(teamlist)
    t.BFS()
    t.removePlayer("3")
    t.setWinner("1","3:0")
    t.setWinner("4","2:0")
    print()
    t.BFS()
    t.setWinner("1","3:0")
    print()
    t.BFS()

test()
'''
    