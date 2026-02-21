public class user {
    void role(){
        System.out.println("I am a user");
    }
}
class Admin extends user{
    void role(){
        System.out.println("I am an admin");
    }
}
class Guest extends user{
    void role(){
        System.out.println("I am a guest");
    }
}
class Demo {
    public static void main(String[] args) {
        user u1 = new user ();
        user u2 = new Admin ();
        user u3 = new Guest ();
        u1.role();
        u2.role();
        u3.role();
    }
}