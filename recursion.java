public class recursion {
    private static int sumOfDigits(int n) {
        if (n == 0) {
            return 0;
        }
        return (n % 10) + sumOfDigits(n / 10);
    }

    private static int countOfDigits(int n) {
        if (n == 0) {
            return 0;
        }
        return 1 + countOfDigits(n / 10);
    }

    private static int reverse(int n, int rev) {
        if (n == 0) {
            return rev;
        }
        return reverse(n / 10, rev * 10 + n % 10);
    }

    private static int power(int x, int n) {
        if (n == 0) {
            return 1;
        }
        return x * power(x, n - 1);
    }

    private static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        int number = 1234;
        int base = 2;
        int exponent = 3;
        int fibIndex = 8;

        System.out.println("Sum of digits: " + sumOfDigits(number));
        System.out.println("Count of digits: " + countOfDigits(number));
        System.out.println("Reverse of digits: " + reverse(number, 0));
        System.out.println("Power of 2^3: " + power(base, exponent));
        System.out.println("Fibonacci of " + fibIndex + ": " + fibonacci(fibIndex));
    }
}
