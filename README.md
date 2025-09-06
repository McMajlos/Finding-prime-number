# 🔢 Prime Number Finder

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](test_is_prime.py)

A comprehensive Python implementation showcasing **three different algorithms** for prime number detection, each demonstrating progressive optimization techniques. This project is part of the "100 Days of Python" coding challenge.

## 📊 Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Best For |
|-----------|----------------|------------------|----------|
| **Level 1** - Basic Trial Division | O(n) | O(1) | Learning & small numbers |
| **Level 2** - Optimized Trial Division | O(√n) | O(1) | Medium-sized numbers |
| **Level 3** - 6k±1 Optimization | O(√n/3) | O(1) | Large numbers & performance |

## 🚀 Features

- **🎯 Three Progressive Algorithms**: From basic to highly optimized implementations
- **📈 Performance Benchmarking**: Compare execution times across different methods
- **🧪 Unit Testing**: Comprehensive test suite included
- **📚 Educational**: Well-documented code with complexity analysis
- **🔍 Large Number Support**: Efficiently handles very large prime numbers

## 📋 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Installation
```bash
git clone https://github.com/McMajlos/Finding-prime-number.git
cd Finding-prime-number
```

### Basic Usage
```python
from main import is_prime_l1, is_prime_l2, is_prime_l3

# Test a number for primality
number = 97
print(f"Is {number} prime?")
print(f"Level 1: {is_prime_l1(number)}")
print(f"Level 2: {is_prime_l2(number)}")
print(f"Level 3: {is_prime_l3(number)}")
```

### Run the Demo
```bash
python main.py
```

## 🔍 Algorithm Details

### Level 1: Basic Trial Division
```python
def is_prime_l1(num):
    """Basic trial division - checks all numbers from 2 to n-1"""
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Educational purposes, very small numbers

### Level 2: Optimized Trial Division
```python
def is_prime_l2(num):
    """Optimized version - only checks up to √n, skips even numbers and multiples of 3"""
```
- **Time Complexity**: O(√n)
- **Space Complexity**: O(1)
- **Optimizations**: 
  - Only checks divisors up to √n
  - Skips even numbers after 2
  - Skips multiples of 3 after 3

### Level 3: 6k±1 Rule Implementation
```python
def is_prime_l3(n):
    """Most efficient - uses 6k±1 rule with integer square root"""
```
- **Time Complexity**: O(√n/3)
- **Space Complexity**: O(1)
- **Optimizations**:
  - Uses mathematical insight that all primes > 3 are of the form 6k±1
  - Uses `math.isqrt()` for precise integer square root
  - Reduces iterations by ~66% compared to Level 2

## 🧪 Testing

Run the unit tests:
```bash
python -m unittest test_is_prime.py -v
```

Or run tests individually:
```bash
python test_is_prime.py
```

## 📊 Performance Examples

Test these large prime numbers to see the performance difference:

| Number | Type | Digits |
|--------|------|--------|
| 97 | Small prime | 2 |
| 50002952501 | Large prime | 11 |
| 98467039289 | Large prime | 11 |
| 928467051221 | Large prime | 12 |

## 📁 Project Structure

```
Finding-prime-number/
├── main.py              # Main implementation with all three algorithms
├── test_is_prime.py     # Unit tests for the algorithms
├── README.md           # This file
└── __pycache__/        # Python cache files
```

## 🎓 Educational Value

This project demonstrates:
- **Algorithm Optimization**: Progressive improvement in time complexity
- **Mathematical Insights**: Application of number theory (6k±1 rule)
- **Python Best Practices**: Clean code, documentation, and testing
- **Performance Analysis**: Understanding Big O notation in practice

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Part of the "100 Days of Python" coding challenge
- Inspired by classical number theory algorithms
- Educational resource for algorithm optimization techniques

---

⭐ **Found this helpful?** Give it a star and share with fellow developers!
