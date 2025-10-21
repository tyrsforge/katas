function solution(n) {
	if (n <= 0) return 0;

	let sum = 0;
	for (let i = 1; i < n; i++) {
		if (i % 3 === 0 || i % 5 === 0) sum += i;
	}
	return sum;
}

// Recursive version, but exceeds stack calls size with large numbers

function recursiveSolution(n) {
	if (n <= 0) return 0;

	return sumMultiples(n - 1);
}

function sumMultiples(n) {
	if (n === 0) return 0;

	const sum = n % 3 === 0 || n % 5 === 0 ? n : 0;

	return sum + sumMultiples(n - 1);
}
