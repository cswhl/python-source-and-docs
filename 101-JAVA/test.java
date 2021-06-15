public class test {
    public static void main(String[] args) {

        //// 会在SCP中创建对象并将引用返回给t0
        //String t0 = "helloworld";
        //// 会在heap中创建对象并将引用返回给t1
        //String t1 = new String("hellowrold");
        //System.out.println(t0 == t1); // false
        //// SCP中已有对象时，会将对象的引用直接返回
        //String t2 = "helloworld";
        //System.out.println(t0 == t2); // true

        //// 每次new都会在堆创建一个新对象，且会将引用返回给遍历
        //String t3 = new String("mohan");
        //String t4 = new String("mohan");
        //System.out.println(t3 == t4); // false

        //// 每次new时，如果SCP中没有该字符串对象，则在SCP中创建一个字符串对象
        //String t5 = new String("cs");
        //String t6 = t5.intern();
        //String t7 = "cs";
        //System.out.println(t5 == t6); // false
        //System.out.println(t7 == t6); // true



        // intern返回SCP中的字符串对象的引用
        //String t5 = t3.intern();
        //System.out.println(t3 == t5); // false
        //String t6 = "mohan".intern();
        //System.out.println(t5 == t6); // true


        String s = new String("a") +  new String("b"); // 不管a、b，只会在堆中创建"ab"对象
        String s1 = s.intern(); // 发现SCP中没有"ab"对象，将堆中"ab"对象的引用保存到SCP中后返回给s1
        String s4 = "ab"; // 发现SCP中有"ab"，将其地址返回给s4
        System.out.println(s == s1); // true
        System.out.println(s4 == s1); // true

        String r = new String("cc"); // 先在SCP中创建"cc"对象，后在队中创建"cc"对象并返回引用给r
        String r1 = r.intern(); // 将SCP中"cc"对象的引用返回给r1
        String r4 = "cc";
        System.out.println(r == r1); // false
        System.out.println(r4 == r1); // true

        String m = new String("m") +  new String("n"); // 不管"m"和"n"，只会在堆中创建"mn"对象,并将引用返回给m
        String m4 = "mn"; // 发现SCP中没有"mn"，在SCP中创建新对象"mn",引用返回给m4
        String m1 = m.intern(); // 发现SCP中已有"mn",将SCP中对象引用返回给m1
        System.out.println(m == m1); // false
        System.out.println(m4 == m1); // true

    }
}
