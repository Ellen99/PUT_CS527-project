| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestSLSRunner | testSimulatorRunning | 0 | 24 |

**Reason(s) for Failure(s):**
Along with some intentionally thrown exceptions("org.apache.hadoop.yarn.exceptions.YarnException: No node! Please configure nodes." - which was a result of the tests not being configured properly with nodes(for those test cases where nodeFile=null) there were also some additional errors, which are really similar to bugs:


 - Looks like a bug, for some parameter combinations, the executor is null, which results in: 
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

TaskRunner.java
```
public void stop() throws InterruptedException {
    if(executor!=null){
      executor.shutdownNow();
      executor.awaitTermination(20, TimeUnit.SECONDS);
    }
  }
```

Same for RMRunner.java
```
  public void stop() {
    if(rm!=null){
      rm.stop();
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
