private int expungeStaleEntry(int staleSlot) {
    Entry[] tab = table;
    int len = tab.length;

    // expunge entry at staleSlot
    // 因为entry对应的ThreadLocal已经被回收，value设为null，显式断开强引用
    tab[staleSlot].value = null;
    tab[staleSlot] = null; // 将整个键值对清除
    size--; // 数量减一

    // Rehash until we encounter null 直到遇到null，然后rehash操作
    Entry e;
    int i;
    // 从当前的staleSlot后面的位置开始，直到遇到null为止
    for (i = nextIndex(staleSlot, len);
            (e = tab[i]) != null;
            i = nextIndex(i, len)) {
        // 获取键对象，也就是map中的key对象
        ThreadLocal<?> k = e.get();
        // 如果为null,直接清除值和整个entry，数量size减一
        if (k == null) {
            e.value = null;
            tab[i] = null;
            size--;
        } else {
            // k不为null，说明当前key未被GC回收，弱引用还存在
            // 此时执行再哈希操作
            int h = k.threadLocalHashCode & (len - 1);
            if (h != i) { // 如果不等的话，表明与之前的hash值不同这个元素需要更新
                tab[i] = null; // 将这个地方设置为null

                // Unlike Knuth 6.4 Algorithm R, we must scan until
                // null because multiple entries could have been stale.
                while (tab[h] != null) // 从当前h位置找一个为null的地方将当前元素放下
                    h = nextIndex(h, len);
                tab[h] = e;
            }
        }
    }
    return i; // 返回的是第一个entry为null的下标
}
