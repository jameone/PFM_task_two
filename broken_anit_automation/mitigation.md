# Broken Anti Automation - Mitigation

In order to resolve this vulnerability the application logic needs to be revised. The ``POST`` end
point https://juice-shop.herokuapp.com/api/Complaints obviously does not validate the incoming data
before updating the database. This will eventually impact database performance as more and more 
superfluous records are added. It also a security risk for DoS and DDoS attacks.

The logic here cannot be narrowed down to line, as the handlers for the routes such as ``api/Users``,
``api/Products``, ..., ``api/Complaints``, etc. are dynamically generated using the third party library 
[finale-rest](https://www.npmjs.com/package/finale-rest) and as such data persistence is defined at a high level.
However, you may take a look at the [complaint model](https://github.com/bkimminich/juice-shop/blob/master/models/complaint.js#L14)
and see it simply associates a `User` with a complaint without performing any additional checks to see if the user actually
exists. The only check it to ensure the user is authenticated.


## Action

* **Recommend a code review and update business logic for next deployment.**
