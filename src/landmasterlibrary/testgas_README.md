# TestGAS

# Introduction

The `TestGAS` library makes it easy to write small tests on `Google Apps Script`, yet scales to support complex functional testing for applications and libraries.

An example of a simple test:

```javascript
// content of test_sample.gs
let tester = new TestGasExecutor();

function sample(x){
  return x + 1;
}

class Test_sample{
  test_sample_1(){
    tester.assertEquals(sample(2), 4);
  }
}

function execute_Test_sample(){
  let failureFuncs = tester.executeTestGas(Test_sample);
}
```

To execute `execute_Test_sample`:

```shell_session
[ 'test_sample_1' ]
TestGAS starts: "Test_sample"
...... TestGAS terminated: "Test_sample".
====================================================== FAILURES ======================================================
______________________________________________ test_sample_1 ______________________________________________
AssertionError: Actual value is not equal to Expected value.
    at Object.test_sample_1 [as value] (aaaaa:9:13)
    at TestGasExecutor.executeTestGas (utilForTestGas:335:55)
    at execute_Test_sample (aaaaa:14:30)
  actual  :  3
  expected:  4
=================== 1 failed, 0 passed of all 1 tests in 0 seconds ===================
```

See [getting-started]() for more examples.

# Features

- You won't lose test-executing function if you write test functions as test class.
- Require Apps Script runtime powered by V8.

# Documentation

For full documentation, including installation, tutorials and PDF documents, please see [these docs]().

# Bugs/Requests

Please use the [GitHub issue tracker]() to submit bugs or request features.

# Changelog

Consult the [Changelog page]() for fixes and enhancements of each version.

# Project

- [Alpha Dev](https://github.com/landmaster135/TestGAS/projects/1)

# License

Distributed under the terms of the MIT license, TestGAS is free and open library.

[return top](#TestGAS)
