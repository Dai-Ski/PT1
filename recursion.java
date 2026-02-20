public class recursion {
    static int sumOfDigits(int n) {
        if (n == 0) {
            return 0;
        }
        return (n % 10) + sumOfDigits(n / 10);
    }
    static int countOfDigits(int n) {
        if (n == 0) {
            return 0;
        }
        return 1 + countOfDigits(n / 10);
    }
    static int reverse(int n, int rev) {
        if (n == 0) {
            return rev;
        }
        rev = rev * 10 + n % 10;
        return reverse(n / 10, rev);
    }
    static int power(int x, int n){
        if (n == 0) {
            return 1;
        }
        return x * power(x, n - 1);
    }
    static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    public static void main(String[] args) {
        System.out.println("Sum of digits: " + sumOfDigits(1234));
        System.out.println("Count of digits: " + countOfDigits(1234));
        System.out.println("Reverse of digits: " + reverse(1234, 0));
        System.out.println("Power of 2^3: " + power(2, 3));
        System.out.println("Fibonacci of 5: " + fibonacci(8));
    }
}
