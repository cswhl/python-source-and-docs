import java.util.*;

public class TreeMapTest2 {
    public static void main(String[] args) {
        TreeMap<Integer, String> tree = new TreeMap<Integer, String>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                System.out.println(o1);
                if(o1.equals(o2))
                    return 1;
                else
                    return o1 - o2;

            }

        });
        tree.put(1, "唐僧");
        tree.put(2, "李白");
        tree.put(5, "白居易");
        tree.put(3, "孙悟空");
        tree.put(2, "李黑");
        System.out.println(tree);
        System.out.println("get(1):" + tree.get(1) + " get(2)" + tree.get(2));
    }
}
