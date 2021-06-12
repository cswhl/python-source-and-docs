import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class iterator {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        list.add("aa");
        list.add("bb");
        list.add("cc");

        System.out.println("使用for循环迭代");
        for (Iterator iter = list.iterator(); iter.hasNext();) {
            String str = (String)iter.next();
            System.out.println(str);
            if (str.equals("cc")) {
                iter.remove();
            }
        }

        System.out.println("源集合显示:" + list);

        System.out.println("使用while循环迭代");
        Iterator iter = list.iterator();
        while(iter.hasNext()) {
            String str = (String) iter.next();
            System.out.println(str);
        }
    }
}
