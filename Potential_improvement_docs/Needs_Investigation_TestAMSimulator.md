| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestAMSimulator | testAMSimulator | 1 | 0 |

**Reason(s) for Failure(s):**
First it was an assertion error, but after commenting out the assertions, and just running the code inside them the following error came up:

One of the combinations result in '''java.lang.NullPointerException''' 

Might be a bug, need further investigation. All the other tests are passing in this class.

    metricRegistry.getGauges().containsKey(key);
    metricRegistry.getGauges().get(key).getValue();

    
**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestAMSimulator | testAMSimulatorWithNodeLabels | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestAMSimulator | testPackageRequests | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-sls | TestAMSimulator | testAMSimulatorRanNodesCleared | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
