def on_button_pressed_a():
    global PlayerX
    PlayerX += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global PlayerX
    PlayerX += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

Hazard_2: game.LedSprite = None
PlayerX = 0
Hazard_2_Count_down = 6
Difficulty = 1000
Lives = 3
sprite = game.create_sprite(2, 4)
Hazard = game.create_sprite(randint(0, 4), 0)

def on_forever():
    Hazard_2.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
basic.forever(on_forever)

def on_forever2():
    Hazard.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
basic.forever(on_forever2)

def on_forever3():
    global Hazard_2
    if Hazard_2_Count_down == 0:
        Hazard_2 = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever3)

def on_forever4():
    sprite.set(LedSpriteProperty.X, PlayerX)
basic.forever(on_forever4)

def on_forever5():
    if Lives == 0:
        game.game_over()
basic.forever(on_forever5)

def on_forever6():
    global Lives, Hazard, Difficulty, Hazard_2_Count_down
    if sprite.is_touching(Hazard):
        Lives += -1
    else:
        if Hazard.get(LedSpriteProperty.Y) == 4:
            Hazard.delete()
            Hazard = game.create_sprite(randint(0, 4), 0)
            game.add_score(1)
            Difficulty += -50
            if Hazard_2_Count_down > 0:
                Hazard_2_Count_down += -1
basic.forever(on_forever6)

def on_forever7():
    global Lives, Hazard_2, Difficulty
    if sprite.is_touching(Hazard_2):
        Lives += -1
    else:
        if Hazard_2.get(LedSpriteProperty.Y) == 4:
            Hazard_2.delete()
            Hazard_2 = game.create_sprite(randint(0, 4), 0)
            game.add_score(1)
            Difficulty += -50
basic.forever(on_forever7)
