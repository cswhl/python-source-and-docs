public class test4 {
    public static void main(String[] args) {
        String t0 = "a";
        String t1 = "b";
        String t2 = t0 + t1;
        //t2.intern();
        String t3 = "ab";
        System.out.println(t2 == t3);
    }
}
