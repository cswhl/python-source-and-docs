import java.util.*;

public class BasicTypeTest {
    public static void main(String[] args) {
        Integer a = 10;
        Integer b = 10;
        Integer b2 = Integer.valueOf(10);
        System.out.println(a == b);
        System.out.println(b == b2);
        Integer c = 200;
        Integer d = 200;
        System.out.println(c == d);
        Long e = 200L;
        Long f = 200L;
        System.out.println(e == f);
        Long g = 20L;
        Long h = 20L;
        System.out.println(g == h);
        Double i = 20.0;
        Double j = 20.0;
        System.out.println(i == j);

        Integer b3 = Integer.valueOf(15);
        System.out.println(b3);
    }
}
