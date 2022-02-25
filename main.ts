input.onButtonPressed(Button.A, function () {
    sprite.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    sprite.change(LedSpriteProperty.X, 1)
})
let sprite: game.LedSprite = null
let Score = 0
let Difficulty = 1000
let Lives = 3
sprite = game.createSprite(2, 4)
basic.pause(500)
let Hazard = game.createSprite(randint(0, 4), 0)
basic.pause(500)
let Hazard_2 = game.createSprite(randint(0, 4), 0)
basic.pause(500)
let Hazard_3 = game.createSprite(randint(0, 4), 0)
basic.pause(500)
let Hazard_4 = game.createSprite(randint(0, 4), 0)
basic.forever(function () {
    Hazard_4.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
})
basic.forever(function () {
    if (Lives == 0) {
        sprite.delete()
        Hazard.delete()
        Hazard_2.delete()
        Hazard_3.delete()
        Hazard_4.delete()
        basic.showString("Score: " + Score)
    }
})
basic.forever(function () {
    if (sprite.isTouching(Hazard)) {
        Lives += -1
    } else {
        if (Hazard.get(LedSpriteProperty.Y) == 4) {
            Hazard.delete()
            Hazard = game.createSprite(randint(0, 4), 0)
        }
    }
})
basic.forever(function () {
    Hazard.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
})
basic.forever(function () {
    Hazard_3.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
})
basic.forever(function () {
    Hazard_2.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
})
basic.forever(function () {
    if (sprite.isTouching(Hazard_2)) {
        Lives += -1
    } else {
        if (Hazard_2.get(LedSpriteProperty.Y) == 4) {
            Hazard_2.delete()
            Hazard_2 = game.createSprite(randint(0, 4), 0)
        }
    }
})
basic.forever(function () {
    if (sprite.isTouching(Hazard_3)) {
        Lives += -1
    } else {
        if (Hazard_3.get(LedSpriteProperty.Y) == 4) {
            Hazard_3.delete()
            Hazard_3 = game.createSprite(randint(0, 4), 0)
            Score += 1
            if (Score < 15) {
                Difficulty += -50
            } else {
                Difficulty += -10
            }
        }
    }
})
basic.forever(function () {
    if (sprite.isTouching(Hazard_4)) {
        Lives += -1
    } else {
        if (Hazard_4.get(LedSpriteProperty.Y) == 4) {
            Hazard_4.delete()
            Hazard_4 = game.createSprite(randint(0, 4), 0)
        }
    }
})
