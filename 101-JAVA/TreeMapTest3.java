import java.util.*;

public class TreeMapTest3 {
    public static void main(String[] args) {
        TreeMap<Integer, String> tree = new TreeMap<Integer, String>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if(o1 != null && o2 != null)
                    return o1 - o2;
                else if(o1 == null && o2 != null) {
                    return -1;
                } else if(o1 != null && o2 == null)
                    return 1;
                else
                    return 0;
            }
        });
        tree.put(1, "唐僧");
        tree.put(2, "李白");
        tree.put(5, "白居易");
        tree.put(3, "孙悟空");
        tree.put(2, "李黑");
        tree.put(null, "赵信");
        System.out.println(tree);
        System.out.println("get(1):" + tree.get(1) + "  get(2)" + tree.get(null));
    }
}
