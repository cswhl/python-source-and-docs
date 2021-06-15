class Info<T> {
    private T var ;        // 定义泛型变量
    public void setVar(T var) {
        this.var = var ;
    }
    public T getVar() {
        return this.var ;
    }
    public String toString() {   // 直接打印
        return this.var.toString() ;
    }
};
public class GenericsTest1 {
    public static void main(String args[]) {
        Info<String> i = new Info<String>() ;        // 使用String为泛型类型
        i.setVar("MLDN");                            // 设置内容
        fun(i);
    }

    public static void fun(Info<?> temp) {
        System.out.println("内容：" + temp) ;
        Info<?> i = new Info<String>() ;        // 使用String为泛型类型
        i.setVar("MLDN");                            // 设置内容
    }
};
