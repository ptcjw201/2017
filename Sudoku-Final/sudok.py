
# Sudoku 9x9
# @작성자 남윤재, 최진우, 황종윤
# 게임방법 : 
#  1. cmd 혹은 터미널 에서 해당파일을 python3로 실행한다.
#  2. 난이도 상/중/하 중에 하나를 선택하고 start! 를 누른다.
#  3. 숫자를 넣고 싶은곳을 클릭하고 오른쪽에 있는 숫자판에서 넣고 싶은 숫자를 클릭한다.
#  4. 스도쿠를 그만두고 싶으면 오른쪽 하단에 있는 QUIT버튼을 눌러서 게임을 종료한다.
#  5. 스도쿠를 완성하면 오른쪽 하단에 check버튼을 눌러서 정답인지 아닌지 확인하고 정답이라면 '나가자'를 눌러서 게임을 종료한다.
#

from tkinter import*
import random

#model
class Solution_check(Frame):
 def __init__(self,root2):
  super().__init__(root2)
  self.pack(padx = 20, pady = 20)
  self.create_checkboard()
  self.canvas = Canvas(root2)
  self.canvas.pack()
  

 def create_checkboard(self):
  self.success = PhotoImage(file="success.gif") #성공시 이미지 
  self.nope = PhotoImage(file="놉.gif") #실패시 이미지
  if board == answer:
   #성공시 check화면 생성
   Label(self,image=self.success).pack() #성공라벨 
   Button(self, text = "나가자", command=self.quit).pack() #게임종료버튼
  else:
   #실패시 check화면 생성
   Label(self, image=self.nope).pack() #실패라벨
 

class Sudoku_START(Frame):
 def __init__(self,root):
  super().__init__(root)
  self.pack(padx = 20,pady = 20)
  self.create_cover()
  self.canvas = Canvas(root)
  self.numw=[[],[],[],[],[],[],[],[],[],[]] #흰색숫자이미지
  self.numg=[[],[],[],[],[],[],[],[],[],[]] #회색숫자이미지

  #이미지 삽입# 
  self.numw[0] = PhotoImage(file="0.gif")
  self.numw[1] = PhotoImage(file="1.gif")
  self.numw[2] = PhotoImage(file="2.gif")
  self.numw[3] = PhotoImage(file="3.gif")
  self.numw[4] = PhotoImage(file="4.gif")
  self.numw[5] = PhotoImage(file="5.gif")
  self.numw[6] = PhotoImage(file="6.gif")
  self.numw[7] = PhotoImage(file="7.gif")
  self.numw[8] = PhotoImage(file="8.gif")
  self.numw[9] = PhotoImage(file="9.gif")
  self.numg[0] = PhotoImage(file="0 (1).gif")
  self.numg[1] = PhotoImage(file="1 (1).gif")
  self.numg[2] = PhotoImage(file="2 (1).gif")
  self.numg[3] = PhotoImage(file="3 (1).gif")
  self.numg[4] = PhotoImage(file="4 (1).gif")
  self.numg[5] = PhotoImage(file="5 (1).gif")
  self.numg[6] = PhotoImage(file="6 (1).gif")
  self.numg[7] = PhotoImage(file="7 (1).gif")
  self.numg[8] = PhotoImage(file="8 (1).gif")
  self.numg[9] = PhotoImage(file="9 (1).gif")
  ##

 #constructor
 #첫번째 화면 생성
 def create_cover(self):
  self.rogo = PhotoImage(file="sudokuLogo2.gif") #스도쿠로고이미지
  self.sang = PhotoImage(file="상.gif") #난이도 상 이미지
  self.zung = PhotoImage(file="중.gif") #난이도 중 이미지
  self.ha = PhotoImage(file="하.gif") #난이도 하 이미지
  self.start = PhotoImage(file="스타트.gif") #스타트 버튼 이미지
  self.Name = Label(self, image=self.rogo) #로고 라벨
  self.Name.grid(row=0,column=0,columnspan=3)
  self.level = StringVar() #난이도 변수
  self.level.set(None)

  #난이도 버튼 생성
  self.a=Radiobutton(self,image=self.sang,variable=self.level, value='1') #난이도 상 버튼
  self.a.grid(row=2,column=0)
  self.b=Radiobutton(self,image=self.zung,variable=self.level, value='2') #난이도 중 버튼
  self.b.grid(row=2,column=1)
  self.c=Radiobutton(self,image=self.ha,variable=self.level, value='3') #난이도 하 버튼
  self.c.grid(row=2, column=2)  

  #시작버튼 생성
  self.d=Button(self,image=self.start , command = self.play) #시작 버튼
  self.d.grid(row=3,column=1)



#constructor
 #2번째 화면 생성
 def create_sudoku(self):
  message = ''
  self.d.destroy() #시작버튼 제거
  count = 0
  self.sdok = [[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]] #스도쿠판 버튼공간 
  self.coodinates = StringVar() #좌표변수
  self.coodinates.set(None)

  #스도쿠판 생성
  for a in range(9):
   for b in range(9):
   	#스도쿠판 버튼 / 라벨#
    if (0<=a<=2) and (3<=b<=5) or (3<=a<=5) and (0<=b<=2 or 6<=b<=8) or (6<=a<=8) and (3<=b<=5):
     if board[a][b]==0:
      i = ' '
      self.sdok[a][b] = Radiobutton(self,image = self.numg[0],variable = self.coodinates,value = 10*a+b, height=30, width=30)
      self.sdok[a][b].grid(row = a,column=b,padx = 10,pady = 10)
     else:
      i=board[a][b]
      self.sdok[a][b] = Label(self,image = self.numg[i])
      self.sdok[a][b].grid(row = a,column=b,padx = 10,pady=10)
    else:
     if board[a][b]==0:
      i = ' '
      self.sdok[a][b] = Radiobutton(self,image = self.numw[0],variable = self.coodinates,value = 10*a+b, height=30, width=30)
      self.sdok[a][b].grid(row = a,column=b,padx = 10,pady = 10)
     else:
      i=board[a][b]
      self.sdok[a][b] = Label(self,image = self.numw[i])
      self.sdok[a][b].grid(row = a,column=b,padx = 10,pady=10)

  #스도쿠 입력 번호판 생성
  Button(self,image = self.numw[1],command = lambda:self.input(1)).grid(row = 1+3,column=3+1+9, padx = 5,pady = 5)
  Button(self,image = self.numw[2],command = lambda:self.input(2)).grid(row = 1+3,column=3+2+9, padx = 5,pady = 5)
  Button(self,image = self.numw[3],command = lambda:self.input(3)).grid(row = 1+3,column=3+3+9, padx = 5,pady = 5)
  Button(self,image = self.numw[4],command = lambda:self.input(4)).grid(row = 2+3,column=3+1+9, padx = 5,pady = 5)
  Button(self,image = self.numw[5],command = lambda:self.input(5)).grid(row = 2+3,column=3+2+9, padx = 5,pady = 5)
  Button(self,image = self.numw[6],command = lambda:self.input(6)).grid(row = 2+3,column=3+3+9, padx = 5,pady = 5)
  Button(self,image = self.numw[7],command = lambda:self.input(7)).grid(row = 3+3,column=3+1+9, padx = 5,pady = 5)
  Button(self,image = self.numw[8],command = lambda:self.input(8)).grid(row = 3+3,column=3+2+9, padx = 5,pady = 5)
  Button(self,image = self.numw[9],command = lambda:self.input(9)).grid(row = 3+3,column=3+3+9, padx = 5,pady = 5)
  Button(self,text = "check",command = self.answercheck).grid(row = 5+3,column=2+9, padx = 5,pady = 5) #check 버튼 생성
  Button(self,text = "quit",command = self.quit).grid(row = 5+3,column=3+9, padx = 5,pady = 5) #나가기 버튼 생성
  Label(self,text ="\n").grid(row = 9,column = 0)#공간확보 ##지워도됨

 # 'check'버튼의 커맨드
 def answercheck(self):
  root2 = Toplevel() #새로운창
  root2.title("Right?")
  root2.geometry("1300x1000")
  Solution_check(root2)
  root2.mainloop()

 #첫번째 화면 삭제
 def destroy(self):
  self.a.destroy() #난이도 상 버튼 제거
  self.b.destroy() #난이도 중 버튼 제거
  self.c.destroy() #난이도 하 버튼 제거
  self.Name.destroy() #로고 제거
  global val #난이도 기억 전역변수
  val = self.level.get()

 #'start'버튼의 함수
 def play(self):
  self.destroy() #제거함수실행
  SudokController() #스도쿠보드생성함수실행
  self.create_sudoku() #스도쿠판생성함수실행 

 #스도쿠등록판버튼의 함수
 def input(self,count):
  if self.coodinates.get() == 'None':
   pass
  else:
   b = int(self.coodinates.get())%10 #클릭한 버튼의 y축 위치좌표 
   a = int(self.coodinates.get())/10 #클릭한 버튼의 x축 위치좌표
   #스도쿠판 이미지 변경
   if (0<=int(a)<=2) and (3<=int(b)<=5) or (3<=int(a)<=5) and (0<=int(b)<=2 or 6<=int(b)<=8) or (6<=int(a)<=8) and (3<=int(b)<=5):
    self.sdok[int(a)][int(b)]["image"] = self.numg[int(count)]
    board[int(a)][int(b)] = int(count)
   else:
    self.sdok[int(a)][int(b)]["image"] = self.numw[int(count)]
    board[int(a)][int(b)] = int(count)



class SudokBoard:
 #보드생성
 @staticmethod
 def create_board():
  seed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  random.shuffle(seed)
  n1 = seed[0]
  n2 = seed[1]
  n3 = seed[2]
  n4 = seed[3]
  n5 = seed[4]
  n6 = seed[5]
  n7 = seed[6]
  n8 = seed[7]
  n9 = seed[8]
  return [[n1, n2, n3, n4, n5, n6, n7, n8, n9],
   [n4, n5, n6, n7, n8, n9, n1, n2, n3],
   [n7, n8, n9, n1, n2, n3, n4, n5, n6],
   [n2, n3, n1, n5, n6, n4, n8, n9, n7],
   [n5, n6, n4, n8, n9, n7, n2, n3, n1],
   [n8, n9, n7, n2, n3, n1, n5, n6, n4],
   [n3, n1, n2, n6, n4, n5, n9, n7, n8],
   [n6, n4, n5, n9, n7, n8, n3, n1, n2],
   [n9, n7, n8, n3, n1, n2, n6, n4, n5]]

 #셔플1
 def shuffle_ribbons(board) :
  top = board[:3]
  middle = board[3:6]
  bottom = board[6:]
  random.shuffle(top)
  random.shuffle(middle)
  random.shuffle(bottom)
  return top + middle + bottom

 #셔플2
 def transpose(board) :
  transposed = []  
  for _ in range(len(board)):
   transposed.append([])
  for row in board:
   i = 0
   for entry in row:
    transposed[i].append(entry)
    i += 1
  return transposed
 
 #정답보드생성
 def create_solution_board():
  board = SudokBoard.create_board()
  board = SudokBoard.shuffle_ribbons(board)
  board = SudokBoard.transpose(board)
  board = SudokBoard.shuffle_ribbons(board)
  board = SudokBoard.transpose(board)
  return board

 #난이도 변환
 def get_level(a):
  if a == '1':
   return 40
  elif a == '2':
   return 34
  else:
   return 18
 
 #보드복사
 def copy_board(board):
  board_clone = []
  for row in board :
   row_clone = row[:]
   board_clone.append(row_clone)
  return board_clone
 
 #구멍생성
 def make_holes(board, no_of_holes):
  holeset = set()
  while no_of_holes > 0:
   i = random.randint(0, 8)
   j = random.randint(0, 8)
   if board[i][j] != 0:
    board[i][j] = 0
    holeset.add((i, j))
    no_of_holes -= 1 
  return (board, holeset) 

#Controller
class SudokController:
 def __init__(self):
  self.__solution = SudokBoard.create_solution_board()
  self.__no_of_holes = SudokBoard.get_level(val)
  self.__puzzle = SudokBoard.copy_board(self.__solution)
  global board #보드 기억 전역변수
  (self.__puzzle, self.__holeset) = SudokBoard.make_holes(self.__puzzle, self.__no_of_holes)
  board = self.__puzzle
  global answer #정답보드 기억 전역변수
  answer = self.__solution
 
 def main():
  root = Tk() 
  root.title("Sudok game")
  root.geometry("1000x600")
  Sudoku_START(root)
  root.mainloop()

SudokController.main()
