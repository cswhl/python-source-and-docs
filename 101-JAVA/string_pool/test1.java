public class test1 {
    public static void main(String[] args) {
        String s = "a" + "b"; // 结果放入常量池,返回引用
        String s1 = "ab"; // 常量池中已经String对象，返回引用
        System.out.println(s == s1); // true
    }
}
