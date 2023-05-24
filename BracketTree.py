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

    def setWinner(self, team, score):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            now_node = queue.pop(0)
            if now_node.data == team:
                now_node.parent.data = team
                now_node.parent.score = score
                return
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)


def insertTeam(teamlist):
    tree = Tree()
    l = len(teamlist)
    for i in range(1, l * 2):
        if i < l:
            tree.add("TBD")
        else:
            tree.add(teamlist[l*2 - i-1])
    
    return tree

def test():
    teamlist = ["1","2","3","4"]
    t = insertTeam(teamlist)
    t.BFS()
    t.setWinner("1","3:0")
    t.setWinner("4","2:0")
    print()
    t.BFS()
    t.setWinner("1","3:0")
    print()
    t.BFS()

test()

    