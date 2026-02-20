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
    public static void main(String[] args) {
        System.err.println("Sum of digits: " + sumOfDigits(1234));
        System.err.println("Count of digits: " + countOfDigits(1234));
        System.err.println("Reverse of digits: " + reverse(1234, 0));
    }
}
