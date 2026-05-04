import java.util.Scanner;

public class ArrrayIndex {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int[] arr = new int[n];
            System.out.println("Enter array elements");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            System.out.println("Enter index");
            int index = sc.nextInt();
            try {
                fetchElement(arr, index);
            }
            catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Invalid index");
            }
            sc.close();
    }
    public static void fetchElement(int[] arr, int index) {
        System.out.println("Element at index " + index + ": " + arr[index]);
    }
}
