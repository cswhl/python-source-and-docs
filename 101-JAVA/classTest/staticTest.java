public class staticTest {

    static String name = "java的架构师技术栈";

    public static void main(String[] args) {
        //直接通过类名
        System.out.println(staticTest.name);

        staticTest statictest = new staticTest();
        System.out.println(statictest.name); // warning

        staticTest.name  = "通过类名修改静态变量";
        System.out.println(staticTest.name);
        System.out.println(statictest.name); // warning

        statictest.name  = "通过对象名修改静态变量";
        System.out.println(staticTest.name);
        System.out.println(statictest.name); // warning
    }

}
