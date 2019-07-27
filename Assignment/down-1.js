let list: number[] = []
let i = 0
let letter = 0
input.onButtonPressed(Button.A, function () {
    letter = letter + 1
    if (letter > 90) {
        letter = 65
    }
    basic.showString(String.fromCharCode(letter))
})
input.onButtonPressed(Button.B, function () {
    if (letter < 65) {
        letter = 90
    }
    basic.showString(String.fromCharCode(letter))
    letter = letter - 1
})
input.onButtonPressed(Button.AB, function () {
    list[i] = letter
    i = i + 1
    if (i > 4) {
        basic.showString("N:")
        for (let j = 0; j <= 4; j++) {
            basic.showString(String.fromCharCode(list[j]))
            basic.pause(200)
        }
        radio.sendValue("" + String.fromCharCode(list[0]) + String.fromCharCode(list[1]) + String.fromCharCode(list[2]) + String.fromCharCode(list[3]) + String.fromCharCode(list[4]), 1)
        basic.showIcon(IconNames.Yes)
    }
})
i = 0
letter = 64
list = [0, 0, 0, 0, 0]
radio.setGroup(1)
