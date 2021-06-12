import java.util.List;
import java.util.ArrayList;

public class foreachTest {
    public static void main(String[] args) {
        List<String> a = new ArrayList<String>();
        a.add("1");
        a.add("2");
        a.add("3");

        for(String temp : a) {
            System.out.print(temp);
        }
    }
}
