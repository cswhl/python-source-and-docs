import java.util.ArrayList;
import java.util.List;

public class ArrayListRemove {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        list.add("aa");
        list.add("bb");
        list.add("bbc");
        list.add("cc");

        System.out.println("使用for循环迭代:" + list);
        for(String str : list) {
            System.out.println(str);
            if("bbc".equals(str)) {
                list.remove(str);
            }
        }
    }
}
