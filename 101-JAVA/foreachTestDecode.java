
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class foreachTestDecode {
    public static void main(String[] args) {
        List<String> a = new ArrayList<String>();
        a.add("1");
        a.add("2");
        a.add("3");

        String temp;
        for(Iterator i$=a.iterator(); i$.hasNext();) {
            temp = (String)i$.next();
            System.out.print(temp);
        }
    }
}
