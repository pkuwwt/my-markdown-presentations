
# Java Threads

---

## `wait()` and `notify()`

  * We can test an async operation by

```java
final boolean[] lock = {false};
Runnable onSuccess = () -> {
	synchronized(lock) {
		lock[0] = true;
		lock.notify();
	}
};
asyncTask(onSuccess);
synchronized(lock) {
	lock.wait(3000);
}
if (!lock[0]) {
	throw new Exception("timeout");
}
```
