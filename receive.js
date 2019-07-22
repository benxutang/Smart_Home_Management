input.onButtonPressed(Button.A, function () {
	
})
radio.onReceivedValue(function (name, value) {
    user_num += 1
    switch(user_num){
        case 1:
            user1 = name
            score1 = value
            serial.writeLine(user1)
            serial.writeNumber(score1)
            break;
        case 2:
            user2 = name
            score2 = value
            serial.writeLine(user2)
            serial.writeNumber(score2)
            break;
        case 3:
            user3 = name
            score3 = value
            serial.writeLine(user3)
            serial.writeNumber(score3)
            break;
    }
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
	
})
let user_num = 0
let user3 = ""
let score3 = 0
let user2= ""
let score2 = 0
let user1 = ""
let score1 = 0
serial.writeLine("WELCOME!")
basic.showIcon(IconNames.Happy)
basic.forever(function () {
	
})
