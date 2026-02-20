public class Staticmet{
    public static final int X = 200;

    private Staticmet() {
    }

    public static void display(){
        System.out.println("SNPSU-CS/IS");
    }
}
class StaticDemo{
    public static void main(String[] args) {
        Staticmet.display();
        System.out.println(Staticmet.X);
    }
}
