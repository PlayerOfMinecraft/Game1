input.onButtonPressed(Button.A, function () {
    PlayerX += -1
})
input.onButtonPressed(Button.B, function () {
    PlayerX += 1
})
let Hazard_2: game.LedSprite = null
let PlayerX = 0
let Hazard_2_Count_down = 6
let Difficulty = 1000
let Lives = 3
let sprite = game.createSprite(2, 4)
let Hazard = game.createSprite(randint(0, 4), 0)
basic.forever(function () {
    Hazard_2.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
})
basic.forever(function () {
    Hazard.change(LedSpriteProperty.Y, 1)
    basic.pause(Difficulty)
})
basic.forever(function () {
    if (Hazard_2_Count_down == 0) {
        Hazard_2 = game.createSprite(randint(0, 4), 0)
    }
})
basic.forever(function () {
    sprite.set(LedSpriteProperty.X, PlayerX)
})
basic.forever(function () {
    if (Lives == 0) {
        game.gameOver()
    }
})
basic.forever(function () {
    if (sprite.isTouching(Hazard)) {
        Lives += -1
    } else {
        if (Hazard.get(LedSpriteProperty.Y) == 4) {
            Hazard.delete()
            Hazard = game.createSprite(randint(0, 4), 0)
            game.addScore(1)
            Difficulty += -50
            if (Hazard_2_Count_down > 0) {
                Hazard_2_Count_down += -1
            }
        }
    }
})
basic.forever(function () {
    if (sprite.isTouching(Hazard_2)) {
        Lives += -1
    } else {
        if (Hazard_2.get(LedSpriteProperty.Y) == 4) {
            Hazard_2.delete()
            Hazard_2 = game.createSprite(randint(0, 4), 0)
            game.addScore(1)
            Difficulty += -50
        }
    }
})
