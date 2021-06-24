public class StaticMethod {
    public static void test() {
        System.out.println("============= 静态方法=============");
    };
    public static void main(String[] args) {
        //方式一：直接通过类名
        StaticMethod.test();
        //方式二：
        StaticMethod fdd = new StaticMethod();
        fdd.test();
    }
}
