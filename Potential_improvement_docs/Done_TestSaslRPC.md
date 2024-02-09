| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testSimpleServerWithTokens | 19 | 0 |

**Reason(s) for Failure(s):**

Assertion failures, to further analyze the tests comment out the assertions, keep the function calls and see whether there are any failures

**Potential fixes:**


Commenting out the assertion to see if there is any other reasons which might cause tests to fail:

```
//    assertEquals(expect.toString(), actual);
```
the change resulted in 18 to 12 failures


After taking out all the assertions I got no failures!!!! means the code is no exceptions when running with all the parameter combinations, 

```Tests run: 24, Failures: 0, Errors: 0, Skipped: 0```





<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testDigestRpc | 12 | 6 |

**Reason(s) for Failure(s):**

12 errors as in ```testSimpleServerWithTokens```

The remaining 6 errors were  ```java.io.IOException: javax.security.sasl.SaslException: DIGEST-MD5: No common protection layer between client and server```

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testDigestRpcWithoutAnnotation | 12 | 6 |

**Reason(s) for Failure(s):**

same as ```testDigestRpc```

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testNoClientFallbackToSimple | 18 | 0 |

**Reason(s) for Failure(s):**

Same as ```testSimpleServerWithTokens```

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testTokenOnlyServerWithTokens | 18 | 0 |

**Reason(s) for Failure(s):**


Same as ```testSimpleServerWithTokens```

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testKerberosServerWithTokens | 18 | 0 |

**Reason(s) for Failure(s):**

Same as ```testSimpleServerWithTokens```

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testErrorMessage | 6 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testPerConnectionConf | 0 | 6 |

**Reason(s) for Failure(s):**

``` javax.security.sasl.SaslException: DIGEST-MD5: No common protection layer between client and server```

**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testSimpleServerWithInvalidTokens | 6 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testTokenOnlyServerWithInvalidTokens | 6 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testKerberosServerWithInvalidTokens | 6 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testSaslResponseOrdering | 0 | 6 |

**Reason(s) for Failure(s):**

```java.lang.UnsupportedOperationException: TOKEN login authentication is not supported```

**Potential fixes:**

Authentication required







<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testPingInterval | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testSaslPlainServer | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testSaslPlainServerBadPassword | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testSimpleServer | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testClientFallbackToSimpleAuthForASecondClient | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testTokenOnlyServer | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-common-project/hadoop-common | TestSaslRPC | testKerberosServer | 0 | 0 |

**Reason(s) for Failure(s):**


**Potential fixes:**









<br><br>
________
