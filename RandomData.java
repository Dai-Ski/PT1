public class RandomData{
    public static void main(String[] args) {
        int[] arr= {1,2,3,4,5};
        for(int x : arr){
            System.out.println(x+" ");
        }
        System.out.println(" ");
        for(Object o: arr){
            System.out.println(o+" ");
        }
    }
}