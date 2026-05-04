public class recursion {
<<<<<<< HEAD
    private static int sumOfDigits(int n) {
=======
    static int sumOfDigits(int n) {
>>>>>>> 5c37cd68c9b591c0547d4e39732863146cb458cc
        if (n == 0) {
            return 0;
        }
        return (n % 10) + sumOfDigits(n / 10);
    }
<<<<<<< HEAD

    private static int countOfDigits(int n) {
=======
    static int countOfDigits(int n) {
>>>>>>> 5c37cd68c9b591c0547d4e39732863146cb458cc
        if (n == 0) {
            return 0;
        }
        return 1 + countOfDigits(n / 10);
    }
<<<<<<< HEAD

    private static int reverse(int n, int rev) {
        if (n == 0) {
            return rev;
        }
        return reverse(n / 10, rev * 10 + n % 10);
    }

    private static int power(int x, int n) {
=======
    static int reverse(int n, int rev) {
        if (n == 0) {
            return rev;
        }
        rev = rev * 10 + n % 10;
        return reverse(n / 10, rev);
    }
    static int power(int x, int n){
>>>>>>> 5c37cd68c9b591c0547d4e39732863146cb458cc
        if (n == 0) {
            return 1;
        }
        return x * power(x, n - 1);
    }
<<<<<<< HEAD

    private static int fibonacci(int n) {
=======
    static int fibonacci(int n) {
>>>>>>> 5c37cd68c9b591c0547d4e39732863146cb458cc
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
<<<<<<< HEAD

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
=======
    public static void main(String[] args) {
        System.out.println("Sum of digits: " + sumOfDigits(1234));
        System.out.println("Count of digits: " + countOfDigits(1234));
        System.out.println("Reverse of digits: " + reverse(1234, 0));
        System.out.println("Power of 2^3: " + power(2, 3));
        System.out.println("Fibonacci of 5: " + fibonacci(8));
>>>>>>> 5c37cd68c9b591c0547d4e39732863146cb458cc
    }
}
