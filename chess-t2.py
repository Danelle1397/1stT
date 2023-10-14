with open('d:/SPR/PYTHON_LEARNING/input.txt', 'r') as file:
    n = int(file.readline().strip())
    chess: str=[]

    for i in range(n) :
        sit = ""
        for j in range(8) :
            sit += file.readline().strip()+"\n"
        chess.append(sit)
 
        chesscount: str=[" "]
        for step in chess :
            j=1
            for way2 in chesscount :
                if step == way2 :
                    j+=1
            chesscount.append(step+"\n")
            print(j)