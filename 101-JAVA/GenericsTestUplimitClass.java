class Info<T extends Number> {   // 此处泛型只能是数字类型
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

public class GenericsTestUplimitClass {
    public static void main(String args[]) {
        Info<Integer> i1 = new Info<Integer>() ;        // 声明Integer的泛型对象
    }
};
