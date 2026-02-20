
public class number {
    int value;

    static void swap(number a, number b) {
        int temp = a.value;
        a.value = b.value;
        b.value = temp;
    }

    public static void main(String[] args) {
        number num1 = new number();
        number num2 = new number();
        num1.value = 5;
        num2.value = 10;

        System.out.println("Before swap: num1 = " + num1.value + ", num2 = " + num2.value);
        swap(num1, num2);
        System.out.println("After swap: num1 = " + num1.value + ", num2 = " + num2.value);
    }
}
