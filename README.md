# PUT_CS527-project

Parameterized runner, which runs the parameterized unit tests with the cartesian product set of initially provided values in order to achieve higher coverage.

In order to use Parameterized Cartesian runner for your tests, into the root pom file of the project add the following
```
 <dependency>
      <groupId>edu.illinois</groupId>
      <artifactId>Parameterized</artifactId>
      <version>1.0-SNAPSHOT</version>
      <scope>compile</scope>
</dependency>
```
and `import edu.illinois.Parameterized;` into the test java file.
