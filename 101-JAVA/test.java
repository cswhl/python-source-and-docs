import java.util.*;

public class test {
    public  static void main(String[] args) {
        //String[] aa = new String[] {"aa", "bb", "cc"};
        String[] aa = {"aa", "bb", "cc"};
        for(String i: aa) {
            System.out.println(i);
        }

        List<String> list = Arrays.asList(aa);
        System.out.println(list);
    }
}
