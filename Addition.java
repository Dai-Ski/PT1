public class Addition {
    static void add (int a, int b) {
        System.out.println("Sum: " + (a + b));
    }
    static void add (double a, double b, double c) {
        System.out.println("Sum: " + (a + b + c));
    }
    static void add(float a, float b) {
        System.out.println("Sum: " + (a + b));
    }
    static void add(int a, int b, int c) {
        System.out.println("Sum: " + (a + b + c));
    }
    public static void main(String[] args) {
        add(5, 10);
        add(5.53, 10.54, 15.904);
        add(3.5f, 4.5f);
        add(1, 2, 3);
    }
}