import java.util.Scanner;
public class StringBufferDemo {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String input = sc.nextLine();
            StringBuffer sb = new StringBuffer(input);
            sb.append(" - Appended text");
            System.out.println(sb);
            sb.insert(0,"XLR8");
            System.out.println(sb);
            sb.delete(0, 5);
            System.out.println(sb);
            //replace
            sb.replace(0, 5, "Replaced");
            System.out.println(sb);
            //reverse
            sb.reverse();
            System.out.println(sb);
        }
    }
}
