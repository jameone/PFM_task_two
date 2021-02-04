# Authentication Vulnerabilities - Mitigation

The typical mitigation for such a vulnerability would be (assuming the package
maintained) to patch the software. There ought to be a patch published in a subsequent version
(in this case ``jsonwebtoken@4.2.2``) which addresses these issues. It is possible to fork the package and
implement the fix yourself, then create a pull request to integrate the changes into the master branch and
convince the original author to publish the patch. In the worst case scenario, you would need to refactor
the application logic to use a different package which is free from such vulnerabilities. Each of these
requires at least a redeployment of the application.

## Action

* **Recommend a code review and update business logic for next deployment.**