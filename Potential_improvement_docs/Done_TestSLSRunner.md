| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestSLSRunner | testSimulatorRunning | 0 | 24 |

**Reason(s) for Failure(s):**
One subset of errors were because of
Looks like a bug, with some parameter values, the executor returns 
```
java.lang.NullPointerException
        at org.apache.hadoop.yarn.sls.scheduler.TaskRunner.stop(TaskRunner.java:171)
        at org.apache.hadoop.yarn.sls.SLSRunner.stop(SLSRunner.java:321)
        at org.apache.hadoop.yarn.sls.BaseSLSRunnerTest.tearDown(BaseSLSRunnerTest.java:68)
```


There are also some other java.lang.NullPointerException s:
```
SynthTraceJobProducer.java:266
CapacityScheduler.java:248
SynthTraceJobProducer.java:266
RMRunner.java:127
```

**Potential fixes:**
Add condition to check whether executor is null before shutting down
```
public void stop() throws InterruptedException {
    if(executor!=null){
      executor.shutdownNow();
      executor.awaitTermination(20, TimeUnit.SECONDS);
    }
  }
```






<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestSLSRunner | testEnableCaching | 0 | 0 |

**Reason(s) for Failure(s):**

No errors for this test

**Potential fixes:**









<br><br>
________
