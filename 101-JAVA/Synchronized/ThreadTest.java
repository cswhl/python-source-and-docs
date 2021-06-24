class MyThread extends Thread {

    private String name;

    public MyThread(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println("MyThread is " + name);
    }
}

public class ThreadTest {

    public static void main(String[] args) {
        MyThread myThread1 = new MyThread("线程1");
        MyThread myThread2 = new MyThread("线程2");
        MyThread myThread3 = new MyThread("线程3");

        myThread1.start();
        myThread2.start();
        myThread3.start();

        System.out.println("myThread1 id =" + myThread1.getId());
        System.out.println("myThread1 id =" + myThread2.getId());
        System.out.println("myThread1 id =" + myThread3.getId());
    }
}
