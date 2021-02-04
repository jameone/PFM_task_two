# Security vulnerabilities on: https://juice-shop.herokuapp.com

This project discusses 3 security vulnerabilities present on the OWASP Juice Shop
demo application. 

1. Broken Anti Automation - An examination of the Juice Stands API reveals that there exists 
   a vulnerability in the logic of the Complaints https://juice-shop.herokuapp.com/api/Complaints
   endpoint. Essentially, by manually altering the body of a valid complaint request a user can lodge
   a null complaint which contains no message, no user id, and optionally a file. This should return
   an HTTP 400 for malformed request, and certainly should not generate records for each erroneous
   request. The current behaviour can cause performance issues and is susceptible to DoS attacks.
   A DoS attacks would be especially effective if the server has limited memory.
   
    * [Exploit Example](broken_anit_automation/example.md)
    * [Potential Mitigation](broken_anit_automation/mitigation.md)
    

2. Vulnerable Components - Here we will examine JSON Web Tokens (or JWTs) which is an authentication 
   mechanism employed by the Juice Shop application. Specifically we will discuss how this mechanism
   is being underutilized/incorrectly employed, as there are a number of high severity
   vulnerabilities raised with ``jsonwebtoken@0.4.0`` (the version employed by the Juice Shop). 
   
    * [Exploit Example](vulnerable_components/example.md)
    * [Potential Mitigation](vulnerable_components/mitigation.md)

   
3. Cross-Site Scripting (reflected XSS) - In general, this type of vulnerability involves the execution of malicious
   code on an otherwise legitimate site. Without properly escaping user data or employing the "safe" facilities
   available for encoding user input, the attacker can execute arbitrary JS or active DOM elements and change the visual
   appearance of the site, send a copy of user data to the attackers servers for analysis, or virtually anything the
   attacker decides to instruct via their malicious input. The logic behind the Juice Shop's search bar is vulnerable
   to a reflected XSS attack.  
   
    * [Exploit Example](reflected_xss/example.md)
    * [Potential Mitigation](reflected_xss/mitigation.md)
    

## Extra

I had written a small script where I attempted to brute force the coupon code challenge. I simply provide
a random guess of length 10 chars from the set I noticed with the coupon ``mNYT0f!Cal``. I ran the program
for an hour or so and it is too slow (network latency) to be effective. However, more time invested into
collecting coupon codes and improving the guess, in addition to performance optimizations and distributed
execution are essentially how such a brute force attack would be carried out. See the script [here](./main.py).

*Note: It would take [54.02](https://tmedweb.tulane.edu/content_open/bfcalc.php?uc=4&lc=4&nu=1&sc=1&ran=&rans=&dict=)
days to break such a 10 char password (1 valid combination). So it stands to reason it would be considerably
less to guess an 80% off coupon and complete the challenge when you consider there are likely many valid combinations*