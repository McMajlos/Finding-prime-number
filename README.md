# Prime Number Finder

This repository contains a Python script (`main.py`) that demonstrates three different methods for checking if a number is prime, each with increasing levels of optimization:

## Features
- **Level 1:** Basic trial division
- **Level 2:** Optimized trial division (skips even numbers and multiples of 3)
- **Level 3:** Highly optimized using the 6k ± 1 rule and integer square root

## Usage
Run the script with Python:
```bash
python main.py
```

You can test the primality of any number by calling the functions:
- `is_prime_l1(num)`
- `is_prime_l2(num)`
- `is_prime_l3(num)`

Example big primes:
- 50002952501
- 98467039289
- 928467051221

## File Structure
- `main.py` — Contains all prime-checking functions and example usage.

## License
This project is licensed under the MIT License.
