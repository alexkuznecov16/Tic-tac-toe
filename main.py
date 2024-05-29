from tkinter import *
import random

# function for game
def game(container):
  # Clean full container
  for widget in container.winfo_children():
    widget.grid_forget()
    
  user_clicked_btns = [] # user array with clicked buttons
  computer_clicked_btns = [] # computer array with clicked buttons
  
  # function for winner checking
  def check_winner():
    # all winning combinations array
    winning_combinations = [
        [btn_1, btn_2, btn_3],
        [btn_4, btn_5, btn_6],
        [btn_7, btn_8, btn_9],
        [btn_1, btn_4, btn_7],
        [btn_2, btn_5, btn_8],
        [btn_3, btn_6, btn_9],
        [btn_1, btn_5, btn_9],
        [btn_3, btn_5, btn_7]
    ]
    
    # iterate each combination from array
    for combination in winning_combinations:
      # if user clicked buttons by winning some combination
      if all(btn in user_clicked_btns for btn in combination):
        result(container, winner='User') # send data to result function
        return True # return result
      
      # if computer clicked buttons by winning some combination
      elif all(btn in computer_clicked_btns for btn in combination):
        result(container, winner='Computer') # send data to result function
        return True # return result
    return False # return False, because clicked buttons are not in combinations array

  # function where computer do click
  def computer_step():
    available_btns = [btn for btn in [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9] if btn not in user_clicked_btns and btn not in computer_clicked_btns] # available buttons for computer

    # if we have ALLOWED buttons
    if available_btns:
      computer_choice = random.choice(available_btns) # computer random choice
      computer_choice.config(state=DISABLED, text='X') # disable button
      computer_clicked_btns.append(computer_choice) # add button to computer clicked buttons array
      
      # check combinations
      if check_winner():
        return
    else:
      result(container, winner=None) # draw

  # function for user clicked button
  def clicked_btn(btn):
    btn.config(state=DISABLED, text='O') # disable button
    user_clicked_btns.append(btn) # add button to user clicked buttons array
    
    # check combinations
    if check_winner():
        return
      
    computer_step() # do computer step
  
  
  # buttons area
  
  btn_1 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_1)
  )
  
  btn_2 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_2)
  )
  
  btn_3 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_3)
  )
  
  btn_4 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_4)
  )
  
  btn_5 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_5)
  )
  
  btn_6 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_6)
  )
  
  btn_7 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_7)
  )
  
  btn_8 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_8)
  )
  
  btn_9 = Button(
    container,
    border=3,
    text='',
    width=10,
    height=5,
    highlightbackground="red",
    font=('Arial', 14, 'bold'),
    command=lambda: clicked_btn(btn_9)
  )
  
  # buttons position
  btn_1.grid(column=0, row=0)
  btn_2.grid(column=1, row=0)
  btn_3.grid(column=2, row=0)
  btn_4.grid(column=0, row=1)
  btn_5.grid(column=1, row=1)
  btn_6.grid(column=2, row=1)
  btn_7.grid(column=0, row=2)
  btn_8.grid(column=1, row=2)
  btn_9.grid(column=2, row=2)
  
# function for result processing
def result(container, winner):
  # Clean full container
  for widget in container.winfo_children():
      widget.grid_forget()
  
  text = Label(container, text='Game result:')
  text.grid(column=1, row=0)
  
  # check who is winner
  if winner == 'User':
    # user is winner
    text = Label(container, text='You won against computer!')
    text.grid(column=1, row=0)
    
  elif winner == 'Computer':
    # computer is winner
    text = Label(container, text='You lost against computer!')
    text.grid(column=1, row=0)
    
  else:
    # draw
    text = Label(container, text='You draw against computer!')
    text.grid(column=1, row=0)
  

# main function
def main():
  root = Tk() # Creating an app window
  root.title('Tick-Tack-Toe') # App title
  root.minsize(200, 400) # App sizes
  
  container = Frame(root) # App container
  container.pack(expand=True) # Pack this container to root
  
  # buttons
  btn_start = Button(container, text='Start', command=lambda: game(container), font=40) # button to start game
  btn_close = Button(container, text='Close', command=root.destroy, font=40) # button to close the app
  
  #buttons position
  btn_start.grid(row=0, column=0, padx=20, pady=20) # start button position
  btn_close.grid(row=0, column=1, padx=20, pady=20) # close button position
  
  root.mainloop() # start app
  

# to run the main code
if __name__ == '__main__':
  main() # main function