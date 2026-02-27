class Teacher{
    String Name;
    Teacher (String Name){
        this.Name = Name;
    }
}
class Student{
    String Name;
    Student (String Name){
        this.Name = Name;
    }
}
public class AssociationDeemo {
    public static void main(String[] args) {
        Teacher teacher = new Teacher("Mr. Smith");
        Student student = new Student("Alice");
        System.out.println("Teacher: " + teacher.Name);
        System.out.println("Student: " + student.Name);
    }
}   