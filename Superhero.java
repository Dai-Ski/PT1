public class Superhero{
private String name;
private String superpower;
public void setName(String name) {
    this.name = name;
}
public String getName() {
    return name;
}
public void setSuperpower(String superpower) {
    this.superpower = superpower;
}
public String getSuperpower() { 
    return superpower;
}
public void display(){
    System.out.println("Name: " + this.name);  
    System.out.println("Superpower: " + this.superpower);
}
public static void main(String[] args) {
    Superhero hero = new Superhero();
    hero.setName("Superman");
    hero.setSuperpower("Flight");
    hero.display();
    System.out.println("Name: " + hero.getName());
    System.out.println("Superpower: " + hero.getSuperpower());
}

}
