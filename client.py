import socket

words = ["able","acid","aged","also","area","army","away","baby","back","ball","bath","bear","beat","been","beer","bell","belt","best","bill","bird","blow","blue","boat","body","both","bowl","bulk","burn","bush","busy","call","calm","came","camp","card","care","case","cash","coat","code","cold","come","cook","cool","cope","copy","core","cost","crew","crop","dear","debt","deep","deny","desk","dial","drug","dual","duke","dust","duty","each","earn","ease","east","easy","edge","else","even","ever","evil","exit","face","fact","fail","fair","fall","farm","fast","fate","fear","feed","feel","feet","foot","ford","form","fort","four","free","from","fuel","full","fund","gain","game","gate","gave","gear","gene","gift","girl","give","glad","goal","goes","gold","Golf","gone","good","gray","held","hell","help","here","hero","high","hill","hire","hold","hole","holy","home","hope","hunt","hurt","idea","inch","into","iron","item","jack","king","knee","knew","know","lack","lady","laid","lake","like","lost","love","luck","made","mail","main","make","male","many","Mark","mass","matt","meal","mean","meat","meet","menu","much","must","name","navy","near","neck","need","news","next","nice","open","oral","over","pace","pack","page","paid","pain","pair","palm","park","part","pass","past","path","peak","pick","pink","pull","pure","push","race","rail","rain","rank","rare","rate","read","real","roll","roof","room","root","rose","rule","rush","ruth","safe","said","sake","sale","salt","some","song","soon","sort","soul","spot","star","stay","step","stop","such","suit","sure","take","tale","talk","tall","true","tune","turn","twin","type","unit","upon","used","user","vary","vast","very","what","when","whom","wide","wife","wild","will","wood","word","wore","work","yard","yeah","year","your","zero","zone"]

def client_program():
    usrName = input("Username: ")
    print("Welome ", usrName + "!")
    name = input("Server Name: ")
    port = int(input("Code: "))
    nameList = name.split("-")
    try:
        host = str(words.index(nameList[0])) + "." + str(words.index(nameList[1])) + "." + str(words.index(nameList[2])) + "." + str(words.index(nameList[3]))
    except:
        print("Invalid Server Name")
        quit()

    client_socket = socket.socket()  # instantiate
    try: 
        client_socket.connect((host, port))  # connect to the server
    except:
        print("ERROR: Could not connect to ", host)

    client_socket.send(usrName.encode())

    print("Connected... Waiting for opponent...")

    opponent = client_socket.recv(1024).decode()
    print("You're playing against " + opponent + "... Good luck!")
    print("(type \"leave\" at any point to leave the game)")
    inp = ''
    recvd = ''
    while True:
        inp = input("\nMake your move with \"r\", \"p\", or \"s\": ")
        while inp != "r" and inp != "s" and inp != "p" and inp != "leave":
            inp = input("Invalid input... Try again: ")
        client_socket.send(inp.encode())
        if inp == "leave":
            break

        print("waiting...")
        recvd = client_socket.recv(1024).decode()
        if recvd == usrName:
            print("You won that round!")
        elif recvd == "tie":
            print("It was a tie!")
        elif recvd == opponent:
            print(opponent + " won that round...")
        elif recvd == (opponent + " left the game"):
            print(recvd)
            quit()
        else:
            print(recvd)

    client_socket.close()  # close the connection

# main
if __name__ == '__main__':
    client_program()