def create_phone_number(numbers):
	if len(numbers) != 10:
		raise ValueError("Invalid numbers")

	area_code = ''.join(map(str, numbers[:3]))
	central_office_code = ''.join(map(str, numbers[3:6]))
	line_number = ''.join(map(str, numbers[6:]))
	phone_number = f"({area_code}) {central_office_code}-{line_number}"

	return phone_number

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
