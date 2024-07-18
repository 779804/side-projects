import time
import os
import random
import msvcrt

class GameSettings:
    WIDTH = 12
    HEIGHT = 12
    SPEED = 5
    SNAKE_BODY = "##"
    SNAKE_HEADS = {
        (1, 0): ">>",
        (-1, 0): "<<",
        (0, 1): "VV",
        (0, -1): "ɅɅ"
    }
    FOOD = "❰❱"
    ALIVE = True

snake_body = [(i, GameSettings.HEIGHT // 2) for i in range(3, 0, -1)]
object_pos = (GameSettings.WIDTH - 3, GameSettings.HEIGHT // 2)
direction = (1, 0)
registered_direction = direction
death_pos = (0, 0)

def clear():
    os.system("cls")

def show_cursor():
    print("\033[?25h", end="") # weird magic that shows cursor (no idea how)

def generateFood(body):
    global object_pos

    all_coords = [(x, y) for x in range(GameSettings.WIDTH) for y in range(GameSettings.HEIGHT)]
    available_coords = [coord for coord in all_coords if coord not in body]

    object_pos = random.choice(available_coords)

def updateBody():
    global snake_body, registered_direction, death_pos

    registered_direction = direction

    new_body = []

    for i in range(len(snake_body)):
        if i == 0:
            original = snake_body[0]
            head_pos = (original[0] + direction[0], original[1] + direction[1])
            new_body.append(head_pos)
        else:
            part = snake_body[i - 1]
            new_body.append(part)
    
    if head_pos in new_body[1:]:
        GameSettings.ALIVE = False
        death_pos = head_pos
        return
    elif (head_pos[0] > (GameSettings.WIDTH - 1) or head_pos[0] < 0) or (head_pos[1] > (GameSettings.HEIGHT - 1) or head_pos[1] < 0):
        GameSettings.ALIVE = False
        death_pos = head_pos
        return

    if new_body[0] == object_pos:
        prevLast = new_body[len(new_body)-2]
        last = new_body[len(new_body)-1]
        new_body.append((last[0] - (prevLast[0] - last[0]), last[1] - (prevLast[1] - last[1])))
        generateFood(new_body)

    registered_direction = direction
    snake_body = new_body

def draw():
    horizontal_border = "+" + "-" * GameSettings.WIDTH * 2 + "+"
    if death_pos[1] < 0:
        death_x = death_pos[0]
        print("+" + "-" * death_x * 2 + "XX" + "-" * (GameSettings.WIDTH - death_x - 1) * 2 + "+")
    else:
        print(horizontal_border)
    

    for y in range(GameSettings.HEIGHT):
        line_str = "|"
        if death_pos[0] < 0 and death_pos[1] == y:
            line_str = "X"
        
        for x in range(GameSettings.WIDTH):
            if (x, y) in snake_body:
                if (x, y) == snake_body[0]:
                    line_str += GameSettings.SNAKE_HEADS[registered_direction]
                else:
                    if (x, y) == death_pos:
                        line_str += "XX"
                    else:
                        line_str += GameSettings.SNAKE_BODY
            elif (x, y) == object_pos:
                line_str += GameSettings.FOOD
            else:
                line_str += "  "

        if death_pos[0] > (GameSettings.WIDTH - 1) and death_pos[1] == y:
            print(line_str + "X")
        else:
            print(line_str + "|")

    if death_pos[1] > (GameSettings.HEIGHT - 1):
        death_x = death_pos[0]
        print("+" + "-" * death_x * 2 + "XX" + "-" * (GameSettings.WIDTH - death_x - 1) * 2 + "+")
    else:
        print(horizontal_border)

def detect_keypress():
    global direction

    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\x1b' or key == b'x': # ESC or X key to end game.
            GameSettings.ALIVE = False
            print("Game ended.")
        else:
            key = key.decode('utf-8').lower()
            if key == 'w' and registered_direction != (0, 1):
                direction = (0, -1)
            elif key == 's' and registered_direction != (0, -1):
                direction = (0, 1)
            elif key == 'a' and registered_direction != (1, 0):
                direction = (-1, 0)
            elif key == 'd' and registered_direction != (-1, 0):
                direction = (1, 0)

def main():
    update_interval = 1 / GameSettings.SPEED

    while GameSettings.ALIVE:
        start_time = time.time()

        print("\033[H", end="") # Used instead of clear() to prevent flickering on screen refresh.
        updateBody()
        draw()
        if GameSettings.ALIVE == False:
            print("You have died. :(")
            show_cursor()
            break
        if len(snake_body) == GameSettings.WIDTH * GameSettings.HEIGHT:
            print("You have won.")
            show_cursor()
            break

        while time.time() - start_time < update_interval:
            detect_keypress()
            time.sleep(0.01)

    show_cursor()

if __name__ == "__main__":
    clear()
    print("\033[?25l", end="") # Used to hide cursor
    main()