class Engine{
    String type;
    public Engine(String type){
        this.type = type;
    }
}
class Car{
    String Name;
    Car(String Name){
        this.Name = Name;
    }
}
public class CompositionDemo {
    public static void main(String[] args) {
        Engine engine = new Engine("V8");
        Car car = new Car("Mustang");
        System.out.println("Car Name: " + car.Name);
        System.out.println("Engine Type: " + engine.type);
    }
}