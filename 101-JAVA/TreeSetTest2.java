import java.util.*;

public class TreeSetTest2 {
    public static void main(String[] args) {
        TreeSet<Integer> tree = new TreeSet<Integer>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if(o1.equals(o2))
                    return 1;
                else
                    return o1 - o2;

            }

        });
        tree.add(1);
        tree.add(2);
        tree.add(5);
        tree.add(3);
        tree.add(2);
        System.out.println(tree);
    }
}
