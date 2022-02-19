# НЕ ГРИФЕРИ!



# СОЗДАЙ СВОЙ ПРОЕКТ!





import tkinter

STEP = 60
SIZE = 600
CENTER = 300
STEPTIME = 300
def endless_movement():
    if is_game_over:
        return


    if where_to in ('Up', 'w', 'W'):
        move(0, -STEP)
    elif where_to == 'Down':
        move(0, STEP)
    elif where_to == 'Left':
        move(-STEP, 0)
    elif where_to == 'Right':
        move(STEP, 0)
    master.after(STEPTIME, endless_movement)

where_to = 'Up'
def key_pressed(event):
    global where_to
    where_to = event.keysym
    #
    # print(event.keysym)
    # if event.keysym in ('Up', 'w', 'W'):
    #     move(0, -STEP)
    # elif event.keysym == 'Down':
    #     move(0, STEP)
    # elif event.keysym == 'Left':
    #     move(-STEP, 0)
    # elif event.keysym == 'Right':
    #     move(STEP, 0)


coords = [300, 300, 300 + STEP, 300 + STEP]
tail = list()

coords = [CENTER, CENTER, CENTER+STEP, CENTER+STEP]
tail = list()

def new_game():
    global coords
    coords.clear()
    coords = [CENTER, CENTER, CENTER + STEP, CENTER + STEP]
    tail.clear()
    master.bind('<KeyPress>', key_pressed)
    canvas.create_rectangle(0, 0, SIZE, SIZE,
                            fill='white')
    canvas.create_text(300, 300, text='Good luck',
                       fill='green',
                       font=('Comic Sans MS',
                             60,
                             'bold')
                       )
    global is_game_over
    is_game_over = False
    master.after(2000, endless_movement)
def move(x, y):
    canvas.create_rectangle(0, 0, 600, 600,
                            fill='white')
    tail.append(coords.copy())
    coords[0] += x
    coords[1] += y
    coords[2] += x
    coords[3] += y
    for coord in coords:
        if coord< 0 or coord > SIZE:
            game_over()
            return
    for segment in tail:
        canvas.create_oval(*segment, fill='green')


    if not had_food():
        tail.pop(0)
    if coords in tail:
        game_over()

    canvas.create_oval(*coords, fill='black')
    canvas.create_oval(*food, fill='teal')


fc = CENTER + STEP * 3
food = [fc, fc, fc + STEP, fc + STEP]


def had_food():
    global coords, food
    if coords != food:
        return False
    while (food == coords) or (food in tail):
        from random import randint
        CELLS = SIZE / STEP - 1
        food_x = randint(0, CELLS) * STEP
        food_y = randint(0, CELLS) * STEP
        food.clear()
        food += [food_x,
                 food_y,
                 food_x + STEP,
                 food_y + STEP]

    return True



def game_over():
    print("Game over")
    master.bind('<KeyPress>', you_lost)
    canvas.create_rectangle(0, 0, SIZE, SIZE,
                            fill='black')
    canvas.create_text(300, 300, text='Ups... \npress any key',
                       fill='red',
                       font=('Comic Sans MS',
                             60,
                             'bold')
                       )
    global is_game_over
    is_game_over = True


is_game_over = False


def you_lost(event):
    canvas.create_rectangle(0, 0, SIZE, SIZE,
                            fill='black')
    canvas.create_text(300, 300, text='Game over\nGame by Ivan\n\nPress space',
                            fill='red',
                       font=('Comic Sans MS' ,
                             60,
                             'bold')
                       )
    if event.keysym == 'space':
        new_game()
        print('new game')



master = tkinter.Tk()
canvas = tkinter.Canvas(master,
                        bg='blue',
                        height=SIZE,
                        width=SIZE)
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.after(2000, endless_movement)
master.mainloop()