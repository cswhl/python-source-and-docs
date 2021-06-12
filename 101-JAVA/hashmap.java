import java.util.HashMap;
import java.util.Map;
import java.util.Iterator;
import java.util.Collection;
import java.util.Set;

public class hashmap {
    public static void main(String[] args) {
        // 创建 HashMap 对象
        Map<String, Integer> hashMap = new HashMap<String, Integer>();

        // 添加元素(key,value)
        System.out.println("添加(aa,1)返回:" + hashMap.put("aa", 1));
        System.out.println("添加(bb,2)返回:" + hashMap.put("bb", 2));
        System.out.println("再次添加key bb返回值:" + hashMap.putIfAbsent("bb", 20));
        System.out.println("第一次添加key cc返回值:"  + hashMap.put("cc", 3));
        System.out.println("再次添加key cc返回值:" + hashMap.put("cc", 4));
        System.out.println("替换key cc返回值:" + hashMap.replace("cc", 3));
        System.out.println("替换key ccc返回值:" + hashMap.replace("ccc", 3));
        System.out.println("");
        // 读取元素
        System.out.println("读取元素:");
        System.out.println("获取key 'aa'的值:" + hashMap.get("aa"));
        System.out.println("获取key 'aaa'的值" + hashMap.get("aaa"));
        System.out.println("获取key 'aaa'的值" + hashMap.getOrDefault("aaa", 0));
        //判断key或value是否存在
        System.out.println("key aa是否存在:" + hashMap.containsKey("aa"));
        System.out.println("value 1是否存在:" + hashMap.containsValue(1));
        System.out.println("map中元素个数:" + hashMap.size());
        System.out.println("");

        // foreach遍历
        System.out.println("foreach遍历映射项(实体):");
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            System.out.println("Key = " + entry.getKey() + ",value = " + entry.getValue());
        }
        System.out.println("foreach遍历映射项的键值:");
        for (String key : hashMap.keySet()) {
            System.out.println("Key = " + key);
        }
        System.out.println("foreach遍历映射项的value值:");
        for (Integer value : hashMap.values()) {
            System.out.println("Value = " + value);
        }
        System.out.println("");

        // Iterator迭代器遍历
        System.out.println("Iterator遍历映射项(实体):");
        // 使用带泛型的迭代器: Iterator<Map.Entry<String, Integer>>, 因为创建HahsMap对象使用泛型化了
        Iterator<Map.Entry<String, Integer>> iterator = hashMap.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, Integer>  entry = iterator.next();
            System.out.println("Key = " + entry.getKey() + ",value = " + entry.getValue());
        }
        System.out.println("Iterator遍历映射项键值:");
        Iterator<String> iterator2 = hashMap.keySet().iterator();
        while (iterator2.hasNext()) {
            String key = iterator2.next();
            System.out.println("Key = " + key);
        }
        System.out.println("Iterator遍历映射项值:");
        Iterator<Integer> iterator3 = hashMap.values().iterator();
        while (iterator3.hasNext()) {
            Integer value = iterator3.next();
            System.out.println("value = " + value);
        }
        System.out.println("");

        // 使用lambda表达式
        System.out.println("lambda表达式遍历映射项:");
        hashMap.forEach((k,v) -> System.out.println("key = " +k + ",value = " + v));
        System.out.println("");

        // hampMap转换为集合
        System.out.println("hampMap转换为集合:");
        Set<Map.Entry<String, Integer>> entries = hashMap.entrySet();
        System.out.println("映射项的集合:" + entries);
        Set<String> keys = hashMap.keySet();
        System.out.println("键值的集合:" + keys);
        Collection<Integer> values = hashMap.values();
        System.out.println("value的集合:" + values);
        System.out.println("");

        // 删除元素
        hashMap.remove("aa");
        System.out.println(hashMap);

        // 清空map
        hashMap.clear();
        System.out.println(hashMap);
    }
}
