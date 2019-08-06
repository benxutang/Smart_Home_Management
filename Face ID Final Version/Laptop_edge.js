radio.onReceivedValue(function (name, value) {
    serial.writeNumber(1)
    basic.showString("T")
    basic.pause(1000)
    basic.showIcon(IconNames.Happy)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString("R")
    radio.sendString(serial.readLine())
})
radio.setGroup(100)
basic.showIcon(IconNames.Happy)
serial.redirectToUSB()
