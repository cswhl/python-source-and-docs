class Circle3 {

    private double radius;

    Circle3() {
        radius = 0;
    }

    Circle3(double newRadius) {
        radius = newRadius;
    }

    double getRadius() {
        return radius;
    }

    void setRadius(double newRadius) {
        radius = newRadius;
    }

    double getArea() {
        return Math.PI * radius * radius;
    }
}
public class PrivateTest {

    public static void main(String[] args) {

        Circle3 circle = new Circle3();
        System.out.println("The radius is " + circle.getRadius());
        //
        //System.out.println("The radius is " + circle.radius);  // wrong, since the radius is private

        circle.setRadius(10.0);
        System.out.println("The modified radius is " + circle.getRadius());

        Circle3.radius;

        Circle3 c = new Circle3(50.0);
        System.out.println("The radius is " + c.getRadius());
    }

}
