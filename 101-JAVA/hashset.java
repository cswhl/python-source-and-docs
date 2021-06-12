import java.util.HashSet;
import java.util.Iterator;

public class hashset {
    public static void main(String[] args) {
        HashSet<String> hashset = new HashSet<String>();

        //向其中添加元素
        hashset.add("c");
        hashset.add("java");
        hashset.add("python");
        System.out.println("元素重复添加，失败:" + hashset.add("python"));
        System.out.println("查询HashSet:" + hashset);
        System.out.println("查询HashSet中元素个数:" + hashset.size());
        System.out.println("HashSet中是否存在'cj':" + hashset.contains("cj"));
        System.out.println("HashSet中是否存在'java:'" + hashset.contains("java"));
        System.out.println("");

        System.out.println("forEach遍历HashSet中的元素:");
        for (String i : hashset) {
            System.out.println(i);
        }
        System.out.println("");

        System.out.println("使用迭代器遍历hashet:");
        Iterator iter = hashset.iterator();
        while (iter.hasNext()) {
            String ss = (String)iter.next();
            System.out.println(ss);
        }
        System.out.println("");

        System.out.println("删除成功返回:" + hashset.remove("java"));
        System.out.println("删除失败返回:" + hashset.remove("java"));
        System.out.println("删除HashSet中'java'元素:" + hashset);

        hashset.clear();
        System.out.println("使用clear清空HashSet中所有元素后:" + hashset);

    }
}
