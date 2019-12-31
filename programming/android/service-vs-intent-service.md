
# `Service` vs. `IntentService`

  * `IntentService` is a subclass of `Service`
  * Both are used to run operations that do not need a UI
  * An `IntentService` is used to run tasks sequentially. Each time you call an `Intent` on an `IntentService`, that operation would be added into the queue
 
---

## Differences

| `Service` | `IntentService` |
| :------- | :------------- |
| run on the main thread | run on a worker thread | 
| support parallel operations | sequentially |
| can be invoked from any thread | only from main thread |
| invoke by `startService` | invoke using `Intent` |
| multiple invocation leads to multiple instances | a single instance |
| manually `stopSelf()` or `stopService()` | automatically stop itself when the queue is empty |
| multiple-thread cases | use a worker thread in `onHandleIntent` |
| | `onBind()` returns null by default, i.e. not bindable by default | 
| | only should implement `onStartCommand` to send intent to queue and `onHandleIntent` to handle it|

---

## References

  * [Service vs. IntentService in Android](https://www.linkedin.com/pulse/service-vs-intentservice-android-anwar-samir)
  * [Android IntentService using BroadCastReceiver](https://www.journaldev.com/20735/android-intentservice-broadcastreceiver)

