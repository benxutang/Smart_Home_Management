let i = 0
let list : number[] = []
let 列表 : number[] = []
let letter = 0
input.onButtonPressed(Button.A, function() {
	letter = letter + 1
		if (letter > 90) {
			letter = 65
		}
	basic.showString(String.fromCharCode(letter))
})
input.onButtonPressed(Button.B, function() {
		if (letter < 65) {
			letter = 90
		}
		basic.showString(String.fromCharCode(letter))
			letter = letter - 1
	})
		input.onButtonPressed(Button.AB, function() {
			list[i] = letter
				i = i + 1
				if (i > 4) {
					basic.showString("Plyaer'name:")
						for (let j = 0; j <= 4; j++) {
							basic.showString(String.fromCharCode(list[j]))
								basic.pause(200)
						}
				}
		})

			i = 0
			letter = 64
			list = [0, 0, 0, 0, 0]

