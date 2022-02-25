def Die():
    basic.show_number(Score)
    while True:
        sprite.delete()
        Hazard.delete()
        Hazard_2.delete()
        Hazard_3.delete()
        Hazard_4.delete()
        basic.show_number(Score)

def on_button_pressed_a():
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Hazard_4: game.LedSprite = None
Hazard_3: game.LedSprite = None
Hazard_2: game.LedSprite = None
Hazard: game.LedSprite = None
sprite: game.LedSprite = None
Score = 0
Score = 0
Difficulty = 1000
Lives = 3
sprite = game.create_sprite(2, 4)
basic.pause(500)
Hazard = game.create_sprite(randint(0, 4), 0)
basic.pause(500)
Hazard_2 = game.create_sprite(randint(0, 4), 0)
basic.pause(500)
Hazard_3 = game.create_sprite(randint(0, 4), 0)
basic.pause(500)
Hazard_4 = game.create_sprite(randint(0, 4), 0)

def on_forever():
    Hazard_4.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
basic.forever(on_forever)

def on_forever2():
    global Hazard
    if sprite.is_touching(Hazard):
        Die()
    else:
        if Hazard.get(LedSpriteProperty.Y) == 4:
            Hazard.delete()
            Hazard = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever2)

def on_forever3():
    Hazard.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
basic.forever(on_forever3)

def on_forever4():
    Hazard_3.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
basic.forever(on_forever4)

def on_forever5():
    Hazard_2.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
basic.forever(on_forever5)

def on_forever6():
    global Hazard_2
    if sprite.is_touching(Hazard_2):
        Die()
    else:
        if Hazard_2.get(LedSpriteProperty.Y) == 4:
            Hazard_2.delete()
            Hazard_2 = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever6)

def on_forever7():
    global Hazard_3, Score, Difficulty
    if sprite.is_touching(Hazard_3):
        Die()
    else:
        if Hazard_3.get(LedSpriteProperty.Y) == 4:
            Hazard_3.delete()
            Hazard_3 = game.create_sprite(randint(0, 4), 0)
            Score += 1
            if Score < 15:
                Difficulty += -50
            else:
                Difficulty += -10
basic.forever(on_forever7)

def on_forever8():
    global Hazard_4
    if sprite.is_touching(Hazard_4):
        Die()
    else:
        if Hazard_4.get(LedSpriteProperty.Y) == 4:
            Hazard_4.delete()
            Hazard_4 = game.create_sprite(randint(0, 4), 0)
basic.forever(on_forever8)
