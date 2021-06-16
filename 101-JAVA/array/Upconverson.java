public class Upconverson {
    public static void main(String[] args) {
        Pet dd = new Dog();
        dd.play();
        //dd.sitDown();
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
