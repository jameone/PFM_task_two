# Broken Access Control - Mitigation

In order to resolve this vulnerability the application logic needs to be revised. The ``POST`` end
point https://juice-shop.herokuapp.com/api/Complaints obviously does not validate the incoming data
before updating the database. This will eventually impact database performance as more and more 
superfluous records are added. It also a security risk for DoS and DDoS attacks.

## Action

* **Recommend a code review and update business logic for next deployment.**
