from builtins import input
W='W'
B='B'
Pawn='Pawn'
Rook='Rook'
Knight='Knight'
Bishop='Bishop'
King='King'
Queen='Queen'
Em='= '
uniDict = {W : {Pawn : "♙   ", Rook : "♖   ", Knight : "♘   ", Bishop: "♗   ", King : "♔   ", Queen : "♕   " },
            B : {Pawn : "♟   ", Rook : "♜   ", Knight : "♞   ", Bishop : "♝   ", King : "♚   ", Queen : "♛   " }}
matboard = [[uniDict[W][Rook], uniDict[W][Knight] ,uniDict[W][Bishop],uniDict[W][Queen] ,uniDict[W][King] ,uniDict[W][Bishop] ,uniDict[W][Knight] ,uniDict[W][Rook] ],
                [uniDict[W][Pawn],uniDict[W][Pawn] , uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn]],
                [Em,Em, Em, Em,Em,Em, Em, Em], [Em,Em, Em, Em,Em,Em, Em, Em],
                [Em,Em, Em, Em,Em,Em, Em, Em],[Em,Em, Em, Em,Em,Em, Em, Em],
                [uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn]],
                [uniDict[B][Rook],uniDict[B][Knight],uniDict[B][Bishop],uniDict[B][Queen],uniDict[B][King],uniDict[B][Bishop],uniDict[B][Knight],uniDict[B][Rook]]]
        
class board :
    def print_board_basic():
        matboard = [[uniDict[W][Rook], uniDict[W][Knight] ,uniDict[W][Bishop],uniDict[W][Queen] ,uniDict[W][King] ,uniDict[W][Bishop] ,uniDict[W][Knight] ,uniDict[W][Rook] ],
                [uniDict[W][Pawn],uniDict[W][Pawn] , uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn], uniDict[W][Pawn]],
                [Em,Em, Em, Em,Em,Em, Em, Em], [Em,Em, Em, Em,Em,Em, Em, Em],
                [Em,Em, Em, Em,Em,Em, Em, Em],[Em,Em, Em, Em,Em,Em, Em, Em],
                [uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn],uniDict[B][Pawn]],
                [uniDict[B][Rook],uniDict[B][Knight],uniDict[B][Bishop],uniDict[B][Queen],uniDict[B][King],uniDict[B][Bishop],uniDict[B][Knight],uniDict[B][Rook]]]
        print('     a  b  c  d  e  f  g  h ')
        print('^'*29)
        for x in range(0,8):
            print(x+1, "| ",end =' ')
            for y in range(0,8):
                print(matboard[x][y],end=" ")
            print("| {x}".format(x=x+1))
            print()
        print('^'*29)
        print('     a  b  c  d  e  f  g  h ')
        print('*'*35)
        print('*'*35)
        
    def print_new() :
        print('     a  b  c  d  e  f  g  h ')
        print('^'*29)
        for x in range(0,8):
            print(x+1, "| ",end =' ')
            for y in range(0,8):
                print(matboard[x][y],end=" ")
            print("| {x}".format(x=x+1))
            print()
        print('^'*29)
        print('     a  b  c  d  e  f  g  h ')
        print('*'*35)
        print('*'*35)

class Piece():    
    def Pawn(i,j,ine,jne,T):
        PossitT=B
        if T==B:
            PossitT=W
        else:
           PossitT=B
        def Step_Kill(i,j,ine,jne,T):
            for k, v in uniDict[PossitT].items(): 
                IsSame=False
                if matboard[int(ine)][int(jne)]== v  :
                    IsSame=True
                    o=1
                    if int(ine)==int(i+o) and int(jne)==int(j-o) :
                        matboard[int(ine)][int(jne)],matboard[int(i)][int(j)]=matboard[int(i)][int(j)],Em
                        break
                    elif int(ine)==int(i+o) and int(jne)==int(j+o) :
                        matboard[int(ine)][int(jne)],matboard[int(i)][int(j)]=matboard[int(i)][int(j)],Em
                        break
                    elif int(ine)==int(i-o) and int(jne)==int(j-o) :
                        matboard[int(ine)][int(jne)],matboard[int(i)][int(j)]=matboard[int(i)][int(j)],Em
                        break
                    elif int(ine)==int(i-o) and int(jne)==int(j+o)  :
                        matboard[int(ine)][int(jne)],matboard[int(i)][int(j)]=matboard[int(i)][int(j)],Em
                        break
                    else :
                        print('ERROR : Can`t Move')
                else:
                    continue
            if IsSame==False or matboard[int(ine)][int(jne)] ==Em: 
                print('ERROR : Can`t Move')
                        
        if matboard[int(i)][int(j)] ==uniDict[B][Pawn]  :
            if i==6 and jne==j:
                if ine==4 or ine==5 :
                    matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                else :
                    print('ERROR : Can`t Move')
            elif int(ine)==i-1 and int(jne)==j and matboard[int(ine)][int(jne)] == Em:
                matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)] = matboard[int(i)][int(j)] ,Em
            elif ine !=i and jne !=j :
                Step_Kill(i,j,ine,jne,T)
            else :
                print('ERROR : Can`t Move')
        else :
            if i==1 and jne==j:
                if ine==2 or ine==3 :
                    matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                else :
                    print('ERROR : Can`t Move')
            elif int(ine)==i+1 and int(jne)==j and matboard[int(ine)][int(jne)] == Em :
                matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)] = matboard[int(i)][int(j)] ,Em
            elif ine !=i and jne !=j :
                Step_Kill(i,j,ine,jne,T)
            else:
                print('ERROR Position')

    def Rook(i,j,ine,jne,T):
        PossitT=B
        if T==B:
            PossitT=W
        else:
           PossitT=B
        if i!=ine  and int(jne)==int(j):
            ERR=True
            if ine>i:
                for c in range(int(i+1), int(ine)):
                    if matboard[int(c)][int(jne)] !=Em:
                        ERR= False
                        break
            else:
                for c in range(int(ine+1), int(i)):
                    if matboard[int(c)][int(jne)] !=Em:
                        ERR= False
                        break
            
            if ERR==False :
                print('ERROR : Can`t Move')
                ERR=True
            else:
                for k, v in uniDict[PossitT].items(): 
                    if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                        matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                    else:
                        continue
        elif j!=jne and int(ine)==int(i):
            ERR=True
            if jne>j:
                for c in range(int(j+1), int(jne)):
                    if matboard[int(ine)][int(c)] !=Em:
                        ERR= False
                        break
            else:
                for c in range(int(jne+1), int(j)):
                    if matboard[int(ine)][int(c)] !=Em:
                        ERR= False
                        break
            if ERR==False :
                print('ERROR : Can`t Move')
                ERR=True
            else:
                for k, v in uniDict[PossitT].items(): 
                    if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                        matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                    else:
                        continue
        else:
            print('ERROR : Can`t Move')
          
    def Knight(i,j,ine,jne,T):
        PossitT=B
        if T==B:
            PossitT=W
        else:
           PossitT=B
        if int(ine)==int(i+2) or int(ine)==int(i-2):
            if int(jne)==int(j+1) or int(jne)==int(j-1):
                for k, v in uniDict[PossitT].items(): 
                    if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                        matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                    else:
                        continue
            else:
                print('ERROR : Can`t Move')
        elif int(jne)==int(j+2) or int(jne)==int(j-2):
            if int(ine)==int(i+1) or int(ine)==int(i-1):
                for k, v in uniDict[PossitT].items(): 
                    if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                        matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                    else:
                        continue
                else:
                    print('ERROR : Can`t Move')
            else:
                print('ERROR : Can`t Move')
        else :
            print('ERROR Position')
                    
    def Bishop(i,j,ine,jne,T):
        PossitT=B
        if T==B:
            PossitT=W
        else:
           PossitT=B 
        for o in range(0,8):
            if int(ine)==int(i+o) and int(jne)==int(j-o):
                ERR=True
                for c in range(i+1, ine):
                    if matboard[int(i+1)][int(j-1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            elif int(ine)==int(i+o) and int(jne)==int(j+o):
                ERR=True
                for c in range(i+1, ine):
                    if matboard[int(i+1)][int(j+1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue
                     
            elif int(ine)==int(i-o) and int(jne)==int(j-o):
                ERR=True
                for c in range(ine+1, i): 
                    if matboard[int(i-1)][int(j-1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            elif int(ine)==int(i-o) and int(jne)==int(j+o):
                ERR=True
                for c in range(ine+1, i):
                    if matboard[int(i-1)][int(j+1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            
    def Queen(i,j,ine,jne,T):
        PossitT=B
        if T==B:
            PossitT=W
        else:
           PossitT=B
        if ine !=i and jne !=j :
            Piece.Bishop(i, j, ine, jne, T)
        elif i!=ine  and int(jne)==int(j) or j!=jne and int(ine)==int(i):
           Piece.Rook(i, j, ine, jne, T)
        else:
            print('ERROR : Can`t Move1')  

    def King(i,j,ine,jne,T):
        PossitT=B
        if T==B:
            PossitT=W
        else:
           PossitT=B 
        if ine !=i and jne !=j :
            o=1       
            if int(ine)==int(i+o) and int(jne)==int(j-o):
                ERR=True
                for c in range(i+1, ine):
                    if matboard[int(i+1)][int(j-1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            elif int(ine)==int(i+o) and int(jne)==int(j+o):
                ERR=True
                for c in range(i+1, ine):
                    if matboard[int(i+1)][int(j+1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue
                     
            elif int(ine)==int(i-o) and int(jne)==int(j-o):
                ERR=True
                for c in range(ine+1, i): 
                    if matboard[int(i-1)][int(j-1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            elif int(ine)==int(i-o) and int(jne)==int(j+o):
                ERR=True
                for c in range(ine+1, i):
                    if matboard[int(i-1)][int(j+1)] !=Em:
                        ERR= False
                        break
                    else:
                        continue
                if ERR==False :
                    print('ERROR : Can`t Move')
                    ERR=True
                else:
                    for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            else:
                print('ERROR : Can`t Move')
                        
        elif i!=ine  and int(jne)==int(j):
            if ine==i+1 or ine==i-1:
                for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            else:
                print('ERROR : Can`t Move')
        elif j!=jne and int(ine)==int(i):
            if jne==j+1 or jne==j-1:
                for k, v in uniDict[PossitT].items(): 
                        if matboard[int(ine)][int(jne)]== v or matboard[int(ine)][int(jne)] ==Em:
                            matboard[int(ine)][int(jne)] , matboard[int(i)][int(j)]=matboard[int(i)][int(j)] ,Em
                        else:
                            continue 
            else:
                print('ERROR : Can`t Move') 
        else:
            print('ERROR : Can`t Move')
        
class game(Piece):
     
    def move(i,j,ine,jne,T):
        if matboard[int(i)][int(j)] ==uniDict[T][Pawn] :
            Piece.Pawn(i,j,ine,jne,T)
        elif matboard[int(i)][int(j)] == uniDict[T][Rook] :
            Piece.Rook(i, j, ine, jne,T)  
        elif matboard[int(i)][int(j)] ==uniDict[T][Knight] :
            Piece.Knight(i, j, ine, jne,T)
        elif matboard[int(i)][int(j)] ==uniDict[T][Bishop] :
            Piece.Bishop(i, j, ine, jne,T)    
        elif matboard[int(i)][int(j)] ==uniDict[T][Queen] :
            Piece.Queen(i, j, ine, jne,T)
        elif matboard[int(i)][int(j)] ==uniDict[T][King] :
            Piece.King(i, j, ine, jne,T)
        else :
            print('ERROR :Not Piece')
        
def main():
    print()
    board.print_board_basic()
    T=W
    while True:
        King_Not_Kill=False
        if T==W:
            for x in range(0,8):
                for y in range(0,8):
                    if matboard[x][y] ==uniDict[T][King]:
                        King_Not_Kill=True
                    else:
                        continue
        else:
            for x in range(0,8):
                for y in range(0,8):
                    if matboard[x][y] ==uniDict[T][King]:
                        King_Not_Kill=True
                    else:
                        continue
                    
        if King_Not_Kill:
            while True:
                if T==W:
                    print('Play For White')
                else:
                    print('Play For Black')
                try:
                    st= input('Enter old (i,j) : ')
                    i=int(st[0])-1
                    j=ord(st[1])-97
                    st2=input('Enter curent (i,j) : ')
                    ine=int(st2[0])-1
                    jne=ord(st2[1])-97
                except :
                    print('I/O error try again')
                    print()
                    continue
                Is_Found=False
                try:
                    s=matboard[i][j]
                except:
                    print('I/O error try again')
                    print()
                    continue
                if s==Em :
                    print('ERROR :Not Piece')
                    print()
                    continue
                for K , V in uniDict[T].items():
                    if matboard[i][j] ==V:
                        Is_Found=True
                        s=matboard[i][j]
                        game.move( i , j , ine , jne,T )
                        board.print_new()
                        if  matboard[ine][jne]==s   :
                            if T==W:
                                T=B
                                break
                            else:
                                T=W
                                break
                        else:
                            break
                    else:
                        continue
                if Is_Found==True :
                    break
                else:
                    print('Play is not for you')
                    print( )
                    break
        else:
            print('You has won  -"-  -"- ')
            print()
            break
main()