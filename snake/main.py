import time
import os
import random
import msvcrt
import json

saveFile = "save.json"

save_attrs = ["SPEED", "WIDTH", "HEIGHT", "HIGH_SCORE"]
valid_attrs = save_attrs[:len(save_attrs)-1]

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
    HIGH_SCORE = 0

    @classmethod
    def save(gs):
        settings = {k: v for k,v in gs.__dict__.items() if k in save_attrs}

        with open(saveFile, 'w') as f:
            json.dump(settings, f)

    @classmethod
    def load(gs):
        try:
            with open(saveFile, 'r') as f:
                settings = json.load(f)

            for k, v in settings.items():
                setattr(gs, k, v)
        except FileNotFoundError:
            gs.save()

    @classmethod
    def update(gs, t: str):
        if not "=" in t:
            return False
        attribute, value = t.split("=")

        if len(attribute) == 0 or len(value) == 0:
            return False
        
        attribute = attribute.upper()

        try:
            value = int(value)
        except ValueError:
            return ValueError
        
        if not attribute in valid_attrs:
            return None
        
        setattr(gs, attribute, value)
        gs.save()

        return True
    
    @classmethod
    def reset(gs):
        gs.SPEED = 5
        gs.WIDTH = 12
        gs.HEIGHT = 12

controls = (
"""Controls:
- W: Move up
- A: Move left
- S: Move down
- D: Move right
- ESC / X: End game
- P: Pause game""")

def init():
    global snake_body, object_pos, direction, registered_direction, death_pos, score

    GameSettings.ALIVE = True
    snake_body = [(i, GameSettings.HEIGHT // 2) for i in range(3, 0, -1)]
    object_pos = (GameSettings.WIDTH - 3, GameSettings.HEIGHT // 2)
    direction = (1, 0)
    registered_direction = direction
    death_pos = (0, 0)
    score = 0

    clear()
    print("\033[?25l", end="") # Used to hide cursor

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
    global snake_body, registered_direction, death_pos, score

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
        score += 1
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
                    if (x, y) == death_pos and not GameSettings.ALIVE:
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
    
    if GameSettings.ALIVE:
        print(controls)
        print(f"\nScore: {score}")
        print(f"Best score: {GameSettings.HIGH_SCORE}")

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
            elif key == 'p':
                key = 0
                while key != 'p':
                    key = msvcrt.getch().decode('utf-8').lower()

def game():
    update_interval = 1 / GameSettings.SPEED

    while True:
        init()
        while GameSettings.ALIVE:
            start_time = time.time()

            print("\033[H", end="") # Used instead of clear() to prevent flickering on screen refresh.
            updateBody()
            if GameSettings.ALIVE == False:
                clear() # removes controls and looks cool
            draw()
            if GameSettings.ALIVE == False:
                print("\nYou have died. :(")
                show_cursor()
                break
            if len(snake_body) == GameSettings.WIDTH * GameSettings.HEIGHT:
                print("\nYou have won!")
                show_cursor()
                break

            while time.time() - start_time < update_interval:
                detect_keypress()
                time.sleep(0.01)
        
        if score > GameSettings.HIGH_SCORE:
            GameSettings.HIGH_SCORE = score
            GameSettings.save()
            print(f"New best! Your final score was {score}.")
        else:
            print(f"Your final score was {score}.")
            print(f"Your best score is: {GameSettings.HIGH_SCORE}")
        show_cursor()
        r = input("\nWould you like to go again? (Y/N): ")
        if r.lower() != "y" and r.lower() != "yes":
            break

def settings():
    clear()
    while True:
        for setting in valid_attrs:
            print(f"{setting.lower()} = {getattr(GameSettings, setting)}")
        
        print("\nChange a setting by typing its name and a value, or type 'back' to begin the game.")
        print("Examples are 'speed=5' or 'height=10'. You must only type integers as values.")
        print("Type 'reset' to return to default values.")

        setting = input("> ").lower()
        if setting == 'back' or len(setting) == 0:
            break
        elif setting == 'reset':
            GameSettings.reset()
            continue

        s = GameSettings.update(setting)

        clear()
        if s == False:
            print("Please ensure that you have entered a valid variable name and value.\n")
        elif s == None:
            print("Attribute not found.\n")
        elif s == ValueError:
            print("Please only insert integers as a value.\n")


if __name__ == "__main__":
    GameSettings.load()
    while True:
        clear()
        print("Welcome to snake!")
        print("Press Enter to begin, or type 'settings' to change game settings.")
        c = input("> ")

        if c.lower() == 'settings':
            settings()
        else:
            game()