import java.util.*;

public class ArrayDequeTest {
    public static void main(String[] args) {
        ArrayDeque<String> stack = new ArrayDeque<String>();
        //依次将三个元素push入"栈"
        stack.push("aa");
        stack.push("bb");
        stack.push("cc");

        //输出：[cc, bb, aa]
        System.out.println(stack);

        //访问第一个元素，但并不将其pop出"栈"，输出：cc
        System.out.println(stack.peek());

        //输出：[cc, bb, aa]
        System.out.println(stack);

        //pop出第一个元素，输出：cc
        System.out.println(stack.pop());

        //输出：[bb,aa]
        System.out.println(stack);
    }
}
