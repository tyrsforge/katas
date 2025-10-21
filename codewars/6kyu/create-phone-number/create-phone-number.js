function createPhoneNumber(numbers) {
	if (numbers.length !== 10) throw new Error("Invalid numbers");

	const [a, b, c, d, e, f, ...rest] = numbers;

	const areaCode = `${a}${b}${c}`;
	const centralOfficeCode = `${d}${e}${f}`;
	const lineNumber = `${rest.join("")}`;
	const phoneNumber = `(${areaCode}) ${centralOfficeCode}-${lineNumber}`;

	return phoneNumber;
}
