class Node(object):
    def __init__(self, name, layer):
        self.layer = layer
        self.parent = None
        self.left = None
        self.right = None
        self.name = name
class Tree(object):
    def __init__(self):
        self.root = Node("Pending",1)

    def createTree(self,current_node, teamnum):
        if current_node.layer < teamnum:
            current_node.left = Node("None", current_node.layer * 2)
            current_node.right = Node("None", current_node.layer * 2)
            self.createTree(current_node.left, teamnum)
            self.createTree(current_node.right, teamnum)

    def insertname(self, namelist):
        for name in namelist:
            current_node = self.root
            while (current_node.left.left is not None):
                if(current_node.left.name == "None"):
                    current_node = current_node.left
                    
                else:
                    current_node = current_node.right

            if current_node.left.name == "None":
                current_node.left.name = name
            else:
                current_node.right.name = name
                current_node.name = "Pending"

                
           
            


                    
            
                
                

    def print(self,node):
        self.__print(node)
        
    def __print(self,current_node):
        if current_node is not None:
            self.__print(current_node.left)
            print(current_node.name, end = ' ')
            self.__print(current_node.right)
def main():
    t = Tree()
    t.createTree(t.root,3)
    t.print(t.root)
    print()
    t.insertname(["rrr","qqq", "mmm"])
    t.print(t.root)
    

main()
