import java.util.*;
public class StringMethod {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String input = sc.nextLine();
        // find the length
        System.out.println("Lenght: "+input.length());
        // convert to uppercase
        System.out.println("Uppercase: "+input.toUpperCase());
        // convert to lowercase
        System.out.println("LowerCase: "+input.toLowerCase());
        // access element using index
        System.out.println(input.charAt(0));
        // slicing, returns sliced string
        System.out.println(input.substring(0,2));
        // concatenation can be done with '+' too
        System.out.println(input.concat("the addition part"));
        // equals returns boolean
        System.out.println(input.equals("233"));
        System.out.println(input.equalsIgnoreCase("123ab"));
        // replace(old,new) returns the str
        System.out.println(input.replace("121","212"));
    }
}