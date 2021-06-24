import java.util.concurrent.atomic.AtomicInteger;

public class ThreadLocalTest2 {
    public static void main(String []args) {
        for(int i = 0; i < 5; i++) {
            final Thread t = new Thread() {
                @Override
                public void run() {
                    System.out.println("当前线程:" + Thread.currentThread().getName() + ",已分配ID:" + ThreadId.get());
                }
            };
            t.start();
        }
    }
    static class ThreadId {
        //一个递增的序列，使用AtomicInger原子变量保证线程安全
        private static final AtomicInteger nextId = new AtomicInteger(0);
        //线程本地变量，为每个线程关联一个唯一的序号
        private static final ThreadLocal<Integer> threadId =
        new ThreadLocal<Integer>() {
            @Override
            protected Integer initialValue() {
                return nextId.getAndIncrement();//相当于nextId++，适用原子操作解决线程安全
            }
        };

        //返回当前线程的唯一的序列，如果第一次get，会先调用initialValue，后面看源码就了解了
        public static int get() {
            return threadId.get();
        }
    }
}
