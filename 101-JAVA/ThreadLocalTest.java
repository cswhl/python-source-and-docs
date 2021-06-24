public class ThreadLocalTest {

    // 测试代码
    public static void main(String[] args) {
        // 新开2个线程用于设置 & 获取 ThreadLoacl的值
        MyRunnable runnable = new MyRunnable();
        new Thread(runnable, "线程1").start();
        new Thread(runnable, "线程2").start();
    }

    // 线程类
    public static class MyRunnable implements Runnable {

        // 创建ThreadLocal & 初始化
        private ThreadLocal<String> threadLocal = new ThreadLocal<String>() {
            @Override
            protected String initialValue() {
                return null; // 初始化vaule
            }
        };

        private ThreadLocal<String> threadLocal2 = new ThreadLocal<String>() {
            @Override
            protected String initialValue() {
                return null; // 初始化vaule
            }
        };

        @Override
        public void run() {

            // 运行线程时，分别设置 & 获取 ThreadLoacl的值
            String name = Thread.currentThread().getName();
            threadLocal.set(name + "的threadLocal"); // 设置值 = 线程名
            threadLocal2.set(name + "的csthreadLocal"); // 设置值 = 线程名

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                threadLocal.remove();
            }

            System.out.println(name + "：" + threadLocal.get());
            System.out.println(name + "：" + threadLocal2.get());
        }
    }
}
