let score = 0
let state = 0
let name = ""
let t2 = 0
let t = 0
let autotime = 0
let gesture = 0
let input2 = 0
let exit = 0
grove.onGesture(GroveGesture.Right, function () {
    input2 = 0
})
grove.onGesture(GroveGesture.Left, function () {
    input2 = 1
})
grove.onGesture(GroveGesture.Up, function () {
    input2 = 2
})
function gameplay2222() {
    gesture = Math.randomRange(0, 6)
    input2 = -1
    t2 = input.runningTime()
    autotime = input.runningTime()
    if (gesture < 1) {
        gesture = 0
        while (input2 == -1 && input.runningTime() - autotime < 3000) {
            basic.showLeds(`
                . . # . .
                . . . # .
                . . . . #
                . . . # .
                . . # . .
                `)
        }
        judgeGuesture2222()
    } else if (gesture < 2) {
        gesture = 1
        while (input2 == -1 && input.runningTime() - autotime < 3000) {
            basic.showLeds(`
                . . # . .
                . # . . .
                # . . . .
                . # . . .
                . . # . .
                `)
        }
        judgeGuesture2222()
    } else if (gesture < 3) {
        gesture = 2
        while (input2 == -1 && input.runningTime() - autotime < 3000) {
            basic.showLeds(`
                . . # . .
                . # . # .
                # . . . #
                . . . . .
                . . . . .
                `)
        }
        judgeGuesture2222()
    } else if (gesture < 4) {
        gesture = 3
        while (input2 == -1 && input.runningTime() - autotime < 3000) {
            basic.showLeds(`
                . . . . .
                . . . . .
                # . . . #
                . # . # .
                . . # . .
                `)
        }
        judgeGuesture2222()
    } else if (gesture < 5) {
        gesture = 4
        while (input2 == -1 && input.runningTime() - autotime < 3000) {
            basic.showLeds(`
                # # # # .
                # . . # .
                # . . # .
                # . # # #
                # . . # .
                `)
        }
        judgeGuesture2222()
    } else {
        gesture = 5
        while (input2 == -1 && input.runningTime() - autotime < 3000) {
            basic.showLeds(`
                . # # # #
                . # . . #
                . # . . #
                # # # . #
                . # . . #
                `)
        }
        judgeGuesture2222()
    }
}
grove.onGesture(GroveGesture.Down, function () {
    input2 = 3
})
grove.onGesture(GroveGesture.Clockwise, function () {
    input2 = 4
})
function judgeGuesture2222() {
    if (input2 == gesture) {
        music.playTone(494, music.beat(BeatFraction.Whole))
        basic.showIcon(IconNames.Yes)
        score = score + 1
    } else {
        music.playTone(370, music.beat(BeatFraction.Quarter))
        music.playTone(370, music.beat(BeatFraction.Quarter))
        basic.showIcon(IconNames.No)
    }
}
radio.onReceivedValue(function (receivedString, value) {
    basic.showIcon(IconNames.Heart)
    if (state == 0 && value == 1) {
        name = receivedString
        state = 1
    }
})
grove.onGesture(GroveGesture.Anticlockwise, function () {
    input2 = 5
})
exit = 0
autotime = 0
gesture = -1
basic.showIcon(IconNames.Heart)
state = 0
score = 0
radio.setGroup(1)
basic.forever(function () {
    if (state == 0) {
        basic.showString("N")
    } else if (state == 1) {
        basic.showString(name)
        state = 2
    } else if (state == 2) {
        t = input.runningTime()
        while (input.runningTime() - t <= 180000) {
            gameplay2222()
            if (grove.measureInCentimeters(DigitalPin.P1) < 20) {
                score = 0
            }
            grove.createDisplay(DigitalPin.P2, DigitalPin.P16).set(7)
            grove.createDisplay(DigitalPin.P2, DigitalPin.P16).show(score)
        }
        state = 3
    } else if (state == 3) {
        radio.setGroup(0)
        radio.sendValue(name, score)
    } else {
    	
    }
})
