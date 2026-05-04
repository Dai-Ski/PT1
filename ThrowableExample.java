public class ThrowableExample {
    public static void main(String[] args) {
        try {
            int a = 10;
            int b = 0;
            if (b == 0) {
                throw new Throwable("Division by Zero");
            }
            int result = a / b;
            System.out.println("Result: " + result);
        } catch (Throwable t) {
            System.out.println(t.getMessage());
        }
    }

}
