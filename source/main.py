#!/usr/bin/env python3
"""Simple Python demo.

This tiny script shows a greeting, reverses a string, and computes a factorial.
It uses argparse with sensible defaults so it can be executed non-interactively
for quick verification.
"""
import argparse


def greet(name: str) -> str:
	"""Return a friendly greeting for name."""
	return f"Hello, {name}!"


def reverse_string(s: str) -> str:
	"""Return the reverse of the input string."""
	return s[::-1]


def factorial(n: int) -> int:
	"""Return n! for n >= 0. Raises ValueError for negative inputs."""
	if n < 0:
		raise ValueError("n must be >= 0")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


def main() -> None:
	parser = argparse.ArgumentParser(description="Simple Python demo script")
	parser.add_argument("--name", "-n", default="Friend", help="Name to greet")
	parser.add_argument("--text", "-t", default="hello", help="Text to reverse")
	parser.add_argument("--number", "-k", type=int, default=5, help="Number for factorial")
	args = parser.parse_args()

	print(greet(args.name))
	print(f"Reversed '{args.text}' -> '{reverse_string(args.text)}'")

	try:
		f = factorial(args.number)
	except ValueError as exc:
		print("Error computing factorial:", exc)
	else:
		print(f"Factorial of {args.number} is {f}")


if __name__ == "__main__":
	main()

