| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-aws | TestDirectoryMarkerPolicy | testNonAuthPath | 10 | 4 |

**Reason(s) for Failure(s):**

First there were 14 errors, commenting out the assertions resulted in 4 errors which are described below:

Reason is dependency between two parameters: MarkerPolicy and predicate


**Potential fixes:**



When MarkerPolicy is Authorative, the predicate shouldn’t fail when invoked(shouldn’t be FAIL_IF_INVOKED)



DirectoryPolicy.MarkerPolicy.Authoritative

FAIL_IF_INVOKED,




<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-aws | TestDirectoryMarkerPolicy | testAuthPath | 10 | 4 |

**Reason(s) for Failure(s):**

same as testNonAuthPath

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-tools/hadoop-aws | TestDirectoryMarkerPolicy | testDeepAuthPath | 10 | 4 |

**Reason(s) for Failure(s):**

same as testNonAuthPath

**Potential fixes:**









<br><br>
________
