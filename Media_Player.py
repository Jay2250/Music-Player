from os import system, environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        
    def listprint(self):
        printdata = self.head
        i=1
        while printdata is not None:
            print(i,printdata.data)
            printdata = printdata.next
            i+=1
            
    def total_node(self):
        node = self.head
        i=0
        while node is not None:
            i+=1
            node = node.next
        return i
        
    def add_node(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        
    def at_end(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode
        
    def in_bet(self, middle_node, newdata):
        middle = Node(middle_node)
        if middle_node is None:
            print("The Mentioned Value is not present")
            return
        
        NewNode = Node(newdata)
        NewNode.next = middle.data
        middle.next = NewNode
        
    def search(self, dataval):
        printdata = self.head
        i=1
        while printdata is not None:
            if printdata.data == dataval:
                print("Match Found at ", i)
                break
            printdata = printdata.next
            i+=1
        else:
            print("Match not Found")
        
    def remove_node(self, remove_key):
        headval = self.head
        if headval is not None:
            if headval.data == remove_key:
                self.head = headval.next
                headval = None
                return
            
        while headval is not None:
            if headval.data == remove_key:
                break
            prev = headval
            headval = headval.next
            
        if headval == None:
            return
        
        prev.next = headval.next
        headval = None
        
    def sort(self):
        ls = []
        lsdata = self.head
        while lsdata is not None:
            ls.append(lsdata.data)
            lsdata = lsdata.next
        ls = sorted(ls)
        lsdata = self.head
        i=0
        while lsdata is not None:
            lsdata.data = ls[i]
            lsdata = lsdata.next
            i+=1

def Add_song():
    song_name = input("Enter Song Name\n")
    print('Adding Your Song...')
    Playlist.add_node(song_name)
    Queue.at_end(song_name)
    
def Total_song():
    total = Playlist.total_node()
    print('Playlist contain', total, ' songs')
    
def Search_song():
    song_name = input("Enter Song Name to Search in Playlist\n")
    print('Searching Your Song...')
    Playlist.search(song_name)
    
def Display_playlist():
    print("Here is Your Playlist")
    Playlist.listprint()
    while 1:
        opt = input("Want to play any song?! \n Type 'y' for YES or 'm' to goto Main Menu\n")
        if opt == 'y':
            
                Play_song()
        elif opt == 'm':
            break
            
def Insert_song():
    song_name = input("Enter the Name of the Song to Insert\n")
    while 1:
        opt = int(input('Insert at \n \t 1. Beginning \n \t 2. In Between \n \t 3. End \n \t 4. Quit \n Enter your Choice \n'))
        if opt == 1:
            print('Inserting at Beginning...')
            Playlist.add_node(song_name)
            break
            
        elif opt == 2:
            Playlist.listprint()
            after_song = input('Name of the Song After which you want to Insert\n')
            Playlist.in_bet(after_song, song_name)
            print('Inserting Your Song after', after_song,' song...')
            break
            
        elif opt == 3:
            print('Inserting at the End...')
            Playlist.at_end(song_name)
            break
            
        elif opt == 4:
            break
            
        else:
            print('Invalid input')
            
def Sort_playlist():
    print('Sorting Your Playlist...')
    Playlist.sort()
    print('Sorted Playlist')
    Playlist.listprint()
    
def Remove_song():
    Playlist.listprint()
    song_name = input("Name of  the song to be Removed\n")
    print('Removing the Song...')
    Playlist.remove_node(song_name)
    
def Recently_played():
    print('Showing Recently Played list...')
    Recent.listprint()

def Song_queue():
    print('Showing Recently Added Song in Playlist...')
    Queue.listprint()

def Play_song():
    Playlist.listprint()
    
    while 1:
        song_name = input('Enter the Name of the Song\n')
        song = 'D:/song/04. Favourite songs/'+ song_name +'.mp3'
        mixer.init()
        mixer.music.load(song)
        mixer.music.play()
        Recent.add_node(song_name)
        opt = input('Do you want to Play Another Song?!\n Type "y" to continue or "m" to Show Main Menu\n')
        if opt == 'y':
            mixer.music.pause()
            continue
        elif opt == 'm':
            break
        else:
            print('Invalid Input')
            
def pause():
    wait = input('Press "Enter" to continue...')


Playlist = Linked_list()
Recent = Linked_list()
Queue = Linked_list()

while 1:
    opt_menu = int(input('\t 1. Add Song \n \t 2. Search Song \n \t 3. Play Song \n \t 4. Display Playlist \
                        \n \t 5. Insert Song \n \t 6. Total Song \n \t 7. Sort Playlist \n \t 8. Remove Song \
                        \n \t 9. Recently Played \n \t 10. Song Queue \n \t 11. Quit \n Enter Your Choice :\n'))

    if opt_menu == 1:
        Add_song()

    elif opt_menu == 2:
        Search_song()
    
    elif opt_menu == 3:
        Play_song()
    
    elif opt_menu == 4:
        Display_playlist()
    
    elif opt_menu == 5:
        Insert_song()
    
    elif opt_menu == 6:
        Total_song()
    
    elif opt_menu == 7:
        Sort_playlist()
    
    elif opt_menu == 8:
        Remove_song()
    
    elif opt_menu == 9:
        Recently_played()   
    
    elif opt_menu == 10:
        Song_queue()
    
    elif opt_menu == 11:
        break
        mixer.music.stop()
        
    else:
        print('Invalid Input')
        
    pause()
    system('cls')