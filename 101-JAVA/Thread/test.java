public class test {
    public static void main(String[] args) {
        Mtest mtest = new Mtest(5);
    }
}

class Mtest {
    private Integer num;

    public Mtest(Integer num) {
        this.num = num;
        System.out.println(num);
    }
}
