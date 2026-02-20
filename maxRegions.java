public class maxRegions {
    static int MaxRegions(int cuts) {
        return cuts * (cuts + 1) / 2 + 1;
    }
    public static void main(String[] args) {
        System.out.println("maxRegions(5) = " + MaxRegions(5));
        System.out.println("maxRegions(4) = " + MaxRegions(4));
    }
}
