# Authentication Vulnerabilities - Example

``jsonwebtoken@0.4.0`` - A look at the Juice Shops source code reveals they are using the ``jsonwebtoken@0.4.0`` 
package found on ``npm``. This particular version has a number of alarming, high severity
vulnerabilities which have been raised. Specifically **Authentication Bypass**, and
**Forgeable Public/Private Tokens**. Both of these completely negate any benefit of using the package
and provide a false sense of security. See [here](https://snyk.io/test/npm/jsonwebtoken/0.4.0) for a
complete list of vulnerabilities.