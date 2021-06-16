public class DownConversion {
    public static void main(String[] args) {
        Pet dd = new Pet();
        dd.play();
        if (dd instanceof Dog) {
            Dog dog = (Dog)dd;
            dog.play();
        }
    }
}

class Pet {
    public void play() {
        System.out.println("玩游戏");
    }
}

class Dog extends Pet {
    public void sitDown() {
        System.out.println("坐下");
    }
}
