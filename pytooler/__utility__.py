import math, time, sys, getpass
username = getpass.getuser()
sys.path.append(f"/Users/{username}/abyssal/")
from verse import crux
class Programm:
    @staticmethod
    def binary_search(sorted_list, target):
        low = 0
        high = len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid] == target:
                return mid
            elif target < sorted_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    @staticmethod
    def caesar_cipher(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += char
        return result
    @staticmethod
    def convert_temp(val, unit):
        if unit.upper() == 'C':
            return (val * 9/5) + 32
        elif unit.upper() == 'F':
            return (val - 32) * 5/9
        return None
    @staticmethod
    def countdown(seconds):
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        return True
    @staticmethod
    def count_words(filename):
        try:
            with open(filename, 'r') as file:
                text = file.read()
                words = text.split()
                return len(words)
        except FileNotFoundError:
            return "File not found."
    @staticmethod
    def password_gen(l):
        crux.Spam.r_spam(1, 0, l, "char")
    def change(text, delay, amount):
        for i in range(amount):
            print(f"Counter: {i}", end="\r", flush=True)
            time.sleep(delay / 1000)
class Mathfunc:
    @staticmethod
    def tr(x):
        return x * (x + 1) // 2
    @staticmethod
    def term(x,c,d):
        return c + (x-1)*d
    @staticmethod
    def sq_repeat(x):
        return [i * i for i in range(1, x + 1)]
    @staticmethod
    def cu_repeat(x):
        return [i * i * i for i in range(1, x + 1)]
    @staticmethod
    def sum_term(x, y, z):
        return z * (2 * x + (z - 1) * y) // 2
    @staticmethod
    def fact(n):
        return math.factorial(n)
    @staticmethod
    def fib(n):
        a, b = 0, 1
        result = []
        for _ in range(n + 1):
            result.append(a)
            a, b = b, a + b
        return result
    @staticmethod
    def sqrt_repeat(x):
        if x < 0: return "Error"
        return [math.sqrt(i) for i in range(1, x + 1)]
    @staticmethod
    def cbrt_repeat(x):
        if x < 0: return "Error"
        return [math.cbrt(i) for i in range(1, x + 1)]
    @staticmethod
    def sq(x):
        return x * x
    @staticmethod
    def cur(x):
        return x * x * x
    @staticmethod
    def sqrt(x):
        if x < 0: return "Error"
        return math.sqrt(x)
    @staticmethod
    def cbrt(x):
        if x < 0: return "Error"
        return math.cbrt(x)
    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    @staticmethod
    def bin_calc(a, b, op):
        a, b = int(a, 2), int(b, 2)
        ops = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a // b if b != 0 else None
        }
        if op not in ops:
            raise ValueError("Invalid operator")
        if op == "/" and b == 0:
            raise ZeroDivisionError("Division by zero")
        r = ops[op]
        return bin(r)[2:], r
    @staticmethod
    def bincon(x, priority="dec"):
        if priority == "dec":
            return int(str(x), 2)
        if priority == "bin":
            n = int(x)
            return bin(n)[2:], n
        raise ValueError("priority must be 'bin' or 'dec'")
