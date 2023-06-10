import sqlite3

class Node():
    # each node stands for each player, and the node will store their all information 
    def __init__(self, data):

        self.data = data[0] # There can be no two emails with the same name, so we are using it as the main data member
        self.fname = data[1]
        self.lname = data[2]
        self.phonenum = data[3]
        self.address = data[4]

        self.left = None
        self.parent = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def add(self, data):
        # each time calling this fction just add one player into the bracket tree
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
        # this function is for testing if the bracket tree works
        # it will use the BFS to print each player's name in the python file
        if self.root == None:
            #the tree is empty
            return
        queue = []
        queue.append(self.root)

        while queue:
            # each time just get the first one from the queue
            # then git it's left and right children and put them in the last of the queue
            now_node = queue.pop(0)
            if now_node.data != "TBD":
                name_to_print = now_node.fname + " " + now_node.lname
            else:
                name_to_print = "TBD"
            # print(name_to_print)
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)

    def getPlayerList(self):
        # this function is for just get the player full name
        # it will use the BFS to get each player's name
        if self.root == None:
            #the tree is empty
            return
        playerList = []
        queue = []
        queue.append(self.root)

        while queue:
            # each time just get the first one from the queue
            # then git it's left and right children and put them in the last of the queue
            now_node = queue.pop(0)
            if now_node.data != "TBD":
                playername = now_node.fname + " " + now_node.lname
                if playername not in playerList:
                    playerList.append(playername)

            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)
        return playerList

    def BFSList(self):
        # same way with the BFS function just put the name into the list
        # this function is use for get the data and put in to the html
        if self.root == None:
            return
        tl = []
        queue = []
        queue.append(self.root)

        while queue:
            now_node = queue.pop(0)
            if now_node.data != "TBD":
                name_to_print = now_node.fname + " " + now_node.lname
            else:
                name_to_print = "TBD"
            tl.append(name_to_print)
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)
        return tl

    def setWinner(self, email):
        # using the player's email to search the winner
        # afer just set the player to their uper layer
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            now_node = queue.pop(0)
            if now_node.data == email:
                now_node.parent.data = email
                now_node.parent.fname = now_node.fname
                now_node.parent.lname = now_node.lname
                now_node.parent.phonenum = now_node.phonenum
                now_node.parent.address = now_node.address
                return
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)

    def removePlayer(self, player):
        #if player didn't show up in the match, remove the player
        #this function also use the bfs way to search the player
        #if find that player just remove
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
    # when the game statr just use the player list to insert the players in to the bracket tree
    tree = Tree()
    l = len(playerlist)
    for i in range(1, l * 2):
        if i < l:
            tree.add(("TBD", None, None, None, None))
        else:
            tree.add(playerlist[l*2 - i-1])
    
    return tree

def loadPlayerData(tournament_name): 
    """
    Loads player data from database with name "dbname" in database folder in directory path ./database/<dbname> into
    a list of tuples. Each tuple represents a single tournament participant and has the form (email, fname, lname, phonenum, address).
    """

    connection = sqlite3.connect("./database/proj2_db.sqlite3") # Connecting to database
    print(f"Tournament name: {tournament_name}")
    my_cursor = connection.cursor()
    my_cursor.execute("PRAGMA foreign_keys = ON;")

    participant_list = []


    select_query = """SELECT * FROM Player JOIN PlayerTournament ON (Player.email=PlayerTournament.player_email) JOIN Tournament ON (PlayerTournament.tournament_name=Tournament.name) WHERE Tournament.name=(?)""" 
    my_cursor.execute(select_query, (tournament_name,))
    player_data = my_cursor.fetchall()
    for row in player_data:
        participant_list.append(row)
        print(f"Row: {row}")

    return participant_list

# this is for testing the code
def test():

    # testing to see if we can load from database
    db_list = loadPlayerData("Super Smash Showdown")
    for player in db_list:
        print(player)

    teamlist = ["1","2","3","4"]
    # testing insert
    t = insertPlayer(db_list)
    t.BFS()

    # testing remove
    t.removePlayer("player3@example.com")
    print()
    t.BFS()

    # testing add single
    player_3 = ("player3@example.com", "Mike", "Johnson", "5555545555", "789 Oak Road, Villagetown")
    t.add(player_3)
    print()
    t.BFS()

    # PAUSE HERE
    # testing winner function
    t.setWinner("player3@example.com")
    t.setWinner("player7@example.com")
    print()
    t.BFS()
    t.setWinner("player6@example.com")
    t.setWinner("player6@example.com")
    print()
    t.BFS()
    print()
    print(t.BFSList())

# test()
    
