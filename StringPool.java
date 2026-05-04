public class StringPool {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = new String("Hello");
        String s4 = new String("Hello");
        System.out.println("s1 == s2: " + (s1 == s2)); // true
        System.out.println(s1.equals(s2)); // true
        System.out.println((s3 == s4)); // false
        System.out.println(s3.equals(s4)); // true
        System.out.println(s1 == s3); // false
        System.out.println(s1.equals(s3)); // true
        String s5 = s3.intern();
        System.out.println(s1 == s5); // true
                System.out.println(s1.equals(s5)); // true
            }
        }









