input.onButtonPressed(Button.A, function () {
    if (mes == 5) {
        mes = 1
    } else {
        mes += 1
    }
    switch (mes) {
        case 1: basic.showString("Msg 1"); break;
        case 2: basic.showString("Msg 2"); break;
        case 3: basic.showString("Msg 3"); break;
        case 4: basic.showString("Msg 4"); break;
        case 5: basic.showString("Msg 5"); break;
    }
})
input.onButtonPressed(Button.AB, function () {
    mes = 0
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.B, function () {
    meg_count += 1
    list[meg_count] = 1
    radio.sendNumber(meg_count)
    switch (mes) {
        case 1: radio.sendString("Msg 1"); break;
        case 2: radio.sendString("Msg 2"); break;
        case 3: radio.sendString("Msg 3"); break;
        case 4: radio.sendString("Msg 4"); break;
        case 5: radio.sendString("Msg 5"); break;
    }
    basic.showIcon(IconNames.Happy)
    mes = 0
})
radio.onReceivedValue(function (name, value) {

})
radio.onReceivedString(function (receivedString) {
    if (list[meg_count] != 1) {
        radio.sendString(receivedString)
        basic.showString("R")
        basic.pause(3000)
        basic.showString(receivedString)
        list[meg_count] = 1
    }
})
radio.onReceivedNumber(function (receivedNumber) {
    meg_count = receivedNumber
})

let meg_count = 0
let list: number[] = []
let mes = 0
let check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
basic.showIcon(IconNames.Yes)
basic.forever(function () {

})
