import java.util.*;

public class SetComparison {
    public static void main(String[] args) {
        Set<Integer> hashSet = new HashSet<>(Arrays.asList(30, 10, 50, 20, 40));
        Set<Integer> treeSet = new TreeSet<>(Arrays.asList(30, 10, 50, 20, 40));
        Set<Integer> linkedHashSet = new LinkedHashSet<>(Arrays.asList(30, 10, 50, 20, 40));
        System.out.println("HashSet: " + hashSet);
        System.out.println("TreeSet: " + treeSet);
        System.out.println("LinkedHashSet: " + linkedHashSet);
    }

}
