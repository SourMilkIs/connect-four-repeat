# -*- coding: utf-8 -*-
"""
@author: furry
"""

def make_board():
  border=["❅"]
  mid=["⍣"]
  board=[]
  col=1
  #making borders
  for i in range(7):
    for j in range(3):
      if j%2==0:
        border.append(" ")
      elif j%2==1:
        border.append("⍣")
    border.append("❅")
  border.append("\n")
  #making middles
  for i in range(7):
    for j in range(3):
      mid.append(" ")
    mid.append("⍣")
  mid.append("\n")
  #making board
  for i in range(29):
    if (i-2)%4==0:
      board.append(col)
      col+=1
    elif i==28:
      board.append("\n")
    else:
      board.append(" ")
  board+=border
  for i in range(6):
      board+=mid
      board+=border
  return board
#######
def instruct_me():
  print("No worries! \nBasically, two players will take turn dropping their pieces into a valid column--one that has not yet been filled to the top. The player who first achieves four of their pieces in a row--horizontally, vertically, or diagonally--will be the winner!")
def invalid_ans():
  print("Sorry, that was not a valid response. Please answer me again.")
def pronoun_me(_player):
  player=_player
  pronoun=""
  while (pronoun != "his" and pronoun !="her" and pronoun !="their" and pronoun !="its"):
    pronoun=input("What is Player "+ player+ "'s pronoun? \n[a] he/him/his \n[b] she/her/hers \n[c] they/them/their \n[d] it/its \n")
    if pronoun=="a":
      pronoun="his"
    elif pronoun=="b":
      pronoun="her"
    elif pronoun=="c":
      pronoun="their"
    elif pronoun=="d":
      pronoun="its"
    else:
      invalid_ans()
  return pronoun
def welcome_me():
  print("Welcome to ConnectFour!")  
  first_timer=""
  can_play=""
  print("This game requires two players.")
  while (first_timer != "a") and (first_timer != "b"):
    first_timer=input("Have both of you played before? \n[a] Yes! \n[b] Nope! \n")
    if (first_timer=="a"):
      print("Great!")
      while (can_play != "a") and (can_play != "b"):
        can_play=input("Do you remember how to play? \n[a] Yes! \n[b] Nope! \n")
        if (can_play=="a"):
          print("Cool!")
        elif (can_play=="b"):
          instruct_me()
        else:
          invalid_ans()
    elif (first_timer=="b"):
      instruct_me()
    else:
      invalid_ans()
def first_player():
  first_player=""
  while (first_player !="a") and (first_player !="b"):
    first_player=input("Now, who would like to have the first turn? \n[a] ◔◡◔ \n[b] ಠ_ಠ \n")
    if (first_player=="a"):
      player1="◔◡◔"
      player2="ಠ_ಠ"
    elif (first_player=="b"):
      player1="ಠ_ಠ"
      player2="◔◡◔"
    else:
      invalid_ans()
  return player1,player2
#######
def check_col(_player,_game,_row,_col):
  player=_player
  game=_game
  col=_col
  row=_row
  slot=60*row+4*col-3
  for i in range(4):
    if game[slot]!=player:
      return False
    else:
      slot+=60
  return True
def check_row(_player,_game,_row,_col):
  player=_player
  game=_game
  col=_col
  row=_row
  slot=60*row+4*col-3
  for i in range(4):
    if game[slot]!=player:
      return False
    else:
      slot+=4
  return True
def check_diagR(_player,_game,_row,_col):
  player=_player
  game=_game
  col=_col
  row=_row
  slot=60*row+4*col-3
  for i in range(4):
    if game[slot]!=player:
      return False
    else:
      slot+=64
  return True
def check_diagL(player,game,row,col):
  slot=60*row+4*col-3
  for i in range(4):
    if game[slot]!=player:
      return False
    else:
      slot+=56
  return True
def check_over(_player,_game,_row,_col):
  player=_player
  game=_game
  row=_row
  col=_col
  if row<=3:
    for i in range(1,row+1):
      res=check_col(player,game,i,col)
      if res==True:
        return True
  else:
    for i in range(col-3,4):
      res=check_col(player,game,i,col)
      if res==True:
        return True
  if col<=4:
    for i in range(1,col+1):
      res=check_row(player,game,row,i)
      if res==True:
        return True
  else:
    for i in range(col-3,5):
      res=check_row(player,game,row,i)
      if res==True:
        return True
  row_copy=row
  col_copy=col
  if row_copy<=3 and col_copy>=4:
    for i in range(4):
      if row_copy>0 and (col_copy>0):
          res=check_diagR(player,game,row_copy,col_copy)
          if res==True:
            return True
          row_copy-=1
          col_copy-=1
  else:
     for i in range(4):
       row_copy-=1
       col_copy-=1
       if row_copy>0 and col_copy>0 and row_copy<=3 and col_copy<=4:
        res=check_diagR(player,game,row_copy,col_copy)
        if res==True:
          return True
  row_copy=row
  col_copy=col
  if row_copy<=3 and col_copy>=4:
    for i in range(4):
      if row_copy>0 and (col_copy>0):
          res=check_diagL(player,game,row_copy,col_copy)
          if res==True:
            return True
          row_copy-=1
          col_copy-=1
  else:
     for i in range(4):
       row_copy-=1
       col_copy+=1
       if row_copy>0 and col_copy>0 and row_copy<=3 and col_copy>=4:
        res=check_diagL(player,game,row_copy,col_copy)
        if res==True:
          return True
  return False
#######
class Player():
  def __init__(self,name,pronoun,score):
    self.name=name
    self.pronoun=pronoun
    self.score=score
  def swap(self,other):
    temp=[self.name,self.pronoun,self.score]
    self.name=other.name
    self.pronoun=other.pronoun
    self.score=other.score
    other.name=temp[0]
    other.pronoun=temp[1]
    other.score=temp[2]
    return self,other
class ConnectFour(Player):
  def _init_(self,player1,player2,board):
    self.player1=player1
    self.player2=player2
    self.imboard=board
  def show(self):
    display=''.join(str(val) for val in self.imboard)
    print(display[:-1])
  def show_score(self):
    print("Player " +self.player1.name+ ": "+repr(self.player1.score) +"\nPlayer " +self.player2.name+ ": "+repr(self.player2.score)+"\n")
  def select(self,player,pronoun):
    self.show()
    self.show_score()
    print("It's "+player+"'s turn!")
    col=""
    valid=list(range(1,8))
    valid=[str(elm) for elm in valid]
    cont=False
    while (cont==False): 
      col=input("Player "+player+" is placing "+pronoun+" piece in column ")
      if col not in valid and col !="X":
        invalid_ans()
      elif col=="X":
        self.show()
        return "exit"
      elif self.imboard[4*int(col)+57] != " ":
        print("This column is already full. Please choose a different column.")
      else:
        cont=True
    col=int(col)
    slot=4*col+357
    for i in range(6):
      if (self.imboard[slot]==" "):
        self.imboard[slot]=player[1]   
        self.imboard[slot-1]=player[0]   
        self.imboard[slot+1]=player[2]   
        print("Piece was successfully placed!\n")
        cont=(check_over(player[1],self.imboard,int(slot/60),col))
        print(cont)
        if cont==True:
          self.show()
          return "winner"
        else:
          break
      else:
        slot-=60
  def is_tie(self,board):
    for i in range(1,8):
      if board[4*i+57]==" ":
        return False
    return True

class BeginGame(ConnectFour):
  welcome = welcome_me()
  def __init__(self):
    self.player1 = Player("","",0)
    self.player2 = Player("","",0)
    repeat = True
    while (repeat):
      cont = ""
      self.imboard = make_board()
      name1,name2 = first_player()
      if self.player1.name == "":
        self.player1.name,self.player2.name = name1,name2
        self.player1.pronoun,self.player2.pronoun = pronoun_me(self.player1.name),pronoun_me(self.player2.name)
      elif self.player1.name == name2:
        self.player1,self.player2 = self.player1.swap(self.player2)
      print("Ok! We can get started now. \nReminder: A player can quit anytime by entering X instead of a column number, but the point for that round goes to the other player.")
      while(cont != "winner" and cont != "exit"):
        cont = super().select(self.player1.name,self.player1.pronoun)
        if cont == "winner":
          self.player1.score += 1
          self.show_score()
          print("Player", self.player1.name, "has won!")
          break
        elif cont == "exit":
          self.player2.score += 1
          self.show_score()
          print("Player", self.player1.name, "has surrendered!")
          print("Player", self.player2.name, "has won!")
          break
        cont = super().select(self.player2.name,self.player2.pronoun)
        if cont == True:
          self.player2.score += 1
          self.show_score()
          print("Player", self.player2.name, "has won!")
          break
        elif cont == "exit":
          self.player1.score1 += 1
          self.show_score()
          print("Player", self.player2.name, "has surrendered!")
          print("Player", self.player1.name, "has won!")
          break
        if (self.is_tie(self.imboard)):
          print("This is a tie!")
          self.show_score()
          break
      more=""
      while(more != "a" and more != "b"):
        more = input("Would you like to play again? \n[a] Yes! \n[b] No thanks, I'm good for the day. \n")
        if more == "a":
          print("Yay! I'm excited to have you here for a bit longer! (o´〰`o)♡ ")
        elif more == "b":
          print("Thank you for playing! Hope to see you again soon!")
          repeat = False
        else:
          invalid_ans()
      
gameboard = BeginGame()




