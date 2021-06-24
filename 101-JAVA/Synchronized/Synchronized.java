public class Synchronized implements Runnable {
    static Synchronized instance1 = new Synchronized();
    static Synchronized instance2 = new Synchronized();

    @Override
    public void run() {
        method1();
        method2();
        method3();
        method4();
    }

    public synchronized void method1() {
        common();
    }

    public static synchronized void method2() {
        commonStatic();
    }

    public void method3() {
        synchronized(this) {
            common();
        }
    }

    public void method4() {
        synchronized(Synchronized.class) {
            common();
        }
    }

    public void method5() {
        common();
    }

    public void method6() {
        commonStatic();
    }

    public void common() {
        System.out.println("线程 " + Thread.currentThread().getName() + " 正在执行");
        try {
            Thread.sleep(1000);
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("线程 " + Thread.currentThread().getName() + " 执行完毕");
    }

    public static void commonStatic() {
        System.out.println("线程 " + Thread.currentThread().getName() + " 正在执行");
        try {
            Thread.sleep(1000);
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("线程 " + Thread.currentThread().getName() + " 执行完毕");
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(instance1);
        Thread t2 = new Thread(instance2);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("finished");
    }
}
