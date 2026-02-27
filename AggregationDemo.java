class Department{
    String deptName;
    Department(String deptName){
        this.deptName = deptName;
    }
}
class College{
    String collegeName;
    Department department;
    College(String collegeName, Department department){
        this.collegeName = collegeName;
        this.department = department;
    }
    void display(){
        System.out.println("College: " + collegeName);
        System.out.println("Department: " + department.deptName);
    }
}
public class AggregationDemo {
    public static void main(String[] args) {
        Department dept = new Department("Computer Science");
        College college = new College("ABC College", dept);
        college.display();
    }
}