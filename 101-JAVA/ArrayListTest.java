import java.util.*;

public class ArrayListTest {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        System.out.println("**对ArrayList的CRUD**");
        list.add("China");
        System.out.println("list.addChina后:" + list);
        list.add("hello");
        System.out.println("list.addhello后:" + list);
        list.addAll(list);
        System.out.println("list.addlist后:" + list);
        list.add(0, "dd");
        System.out.println("list.add第0位后:" + list);
        list.set(0, "huanle");
        System.out.println("list.set第0位后:" + list);
        System.out.println("list.size:" + list.size());
        System.out.print("list.containshello:" + list.contains("hello") + "\n");
        System.out.println("romve(1)前：" + list);
        list.remove(1);
        System.out.println("remove后: " + list);
        System.out.println("romve('hello')前：" + list);
        list.remove("hello");
        System.out.println("remove后: " + list);
        System.out.println("\n");

        System.out.println("**使用迭代器操作ArrayList**");
        Iterator<String> it = list.iterator();
        int j = 0;
        while (it.hasNext()) {
            String str = it.next();
            System.out.println("iterator遍历输出list第" + (j++) + "项:" + str);
        }
        System.out.println("\n");

        list.add("[1,2,3]");
        System.out.println(list);

        System.out.println("**将ArrayList转换为数组**");
        //第一种方式
        Object[] array = list.toArray();
        //array是个数组
        System.out.println(array[1]);
        System.out.println(array.length);
        for (int i = 0; i < array.length; i++) {
            String a = (String) array[i];
            System.out.println("输出对象" + a);
        }
        System.out.println("直接输出list.toArray: " + list.toArray());
        //第二种方式    T[] a  数组的运行时类型
        String[] array2 = new String[list.size()];
        System.out.println("list.toArray的输出:" + list.toArray(array2));
        System.out.println("\n");

        //返回此列表中  第一次 出现的指定元素的索引，如果列表不包含该元素，则返回 -1
        //就是从前往后找需要比较的元素时，遇到第一个相同元素就停止，比较这一个，不继续往下找
        System.out.println("输出元素在list中的索引，不存在的话返回-1");
        System.out.println(list.indexOf("huanle"));
        System.out.println(list.indexOf("hello"));
        System.out.println(list.indexOf("China"));
        System.out.println(list.indexOf("[1,2,3]"));
        System.out.println(list.indexOf("ddddd"));
    }
}
