var start = 1000;
while(1) {
	var string = start.toString();
	if (string.split('').reverse().join('') === string) {
		var i;
		var got = true;
		for (i = 2; i <= Math.sqrt(start); i++) {
			if (start % i === 0) {
				got = false;
				break;
			}
		}
		if (got === true) {
			console.log(string);
			break;
		}
	}
	start--;
}
