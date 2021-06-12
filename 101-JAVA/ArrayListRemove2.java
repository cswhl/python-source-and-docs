import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

public class ArrayListRemove2 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        list.add("aa");
        list.add("bb");
        list.add("bbc");
        list.add("cc");

        System.out.println("使用for循环迭代:" + list);
        String temp;
        for(Iterator i$ = list.iterator(); i$.hasNext(); ){
                temp = (String)i$.next();
                System.out.print(temp);
                if("bbc".equals(temp)) {
                    list.remove(temp);
                }
        }
    }
}
