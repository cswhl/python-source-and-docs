// 父类
class Foo {
    static {
        System.out.println("父类第一个静态代码块");
    }

    static int fj = 88;

    {
        i = 99;  // 代码块可以赋值其后定义的实例变量，但不能访问其后定义的实例变量
        System.out.println("父类第一个普通代码块");
    }

    int i = 1;

    static {
        System.out.println("子类静态代码块"+ "fj=" + fj);
    }

    public Foo() {
        i = getValue();// 父类调用子类的重写getValue()方法，而子类的变量j为0(因为jvm仅对内存空间进行过初始化)
        System.out.println("父构造函数初始化后:" + "i=" + i);
    }

    {
        System.out.println("父实例变量初始化后:" + "i=" + i);
        i = 2;
        System.out.println("父代码块初始化后:" + "i=" + i);
    }

    protected int getValue() {
        System.out.println("父类的getValue:i=" + i);
        return i;
    }
}

// 子类
class Bar extends Foo {

    static {
        System.out.println("子类第一个静态代码块");
    }

    static int sj = 66;

    {
        System.out.println("");
        System.out.println("子类第一个普通代码块");
    }

    int j = 3;

    static {
        System.out.println("子类静态代码块" + "sj=" + sj);
    }


    public Bar() {
        j = 4;
        System.out.println("子构造函数初始化后:" + "j=" + j);
    }

    {
        System.out.println("子实例变量初始化后:" + "j=" + j);
        j = 5;
        System.out.println("子代码块初始化后:" + "j=" + j);
    }

    @Override
    protected int getValue() {
        System.out.println("调用子类重写的getValue:j=" + j);
        return j;
    }
}

public class OrderTest {
    public static void main(String... args) {
        Bar bar = new Bar();
        System.out.println("子类getValue返回值:" + bar.getValue());
    }
}
/*
输出:
父实例变量初始化后:i=1
父代码块初始化后:i=2
调用子类重写的getValue:j=0
父构造函数初始化后:i=0

子实例变量初始化后:j=3
子代码块初始化后:j=5
子构造函数初始化后:j=4
调用子类重写的getValue:j=4
子类getValue返回值:4
*/
