import java.util.*;

public class LinkedHashMapTest
{
    public static void main(String[] args)
    {
        LinkedHashMap<String, Integer> scores = new LinkedHashMap<String, Integer>();
        scores.put("语文" , 80);
        scores.put("英文" , 82);
        scores.put("数学" , 76);
        //遍历scores里的所有的key-value对
        for (Object key : scores.keySet())
        {
            System.out.println(key + "------>" + scores.get(key));
        }
    }
}
