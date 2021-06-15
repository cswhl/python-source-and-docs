import java.util.*;

public class TreeSetTest3 {
    public static void main(String[] args) {
        TreeSet<Integer> tree = new TreeSet<Integer>(new Comparator<Integer>() {
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
        tree.add(1);
        tree.add(2);
        tree.add(5);
        tree.add(3);
        tree.add(null);
        System.out.println(tree);
    }
}
