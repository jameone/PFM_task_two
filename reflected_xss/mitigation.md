# Reflected XSS - Mitigation

Any time user data is to be displayed on screen, it is required to be "sanitized". There are a number
of facilities available for encoding user input for use in JavaScripts and Strings to be rendered on
screen. The example of executing JS via an `iframe` which was improperly sanitized is the result
of manually calling the `innerHTML` method on some DOM node and simply feeding the user input to the
method. Thus, if the user enters some malicious code instead of an innocuous string, it too will be fed
to `innerHTML`. In our case, we formatted a string equivalent to a valid HTML element and without
sanitization it `innerHTML` was called with
`<iframe src="javascript:alert(`This is a relfective XSS attack vector.`)">`. Instead of parsing the data
as a string, the method assumed we wanted to add a child node.

Line #13 is causing the issue may be seen [here](https://github.com/bkimminich/juice-shop/blob/master/frontend/src/app/search-result/search-result.component.html).
```angular2html
    ...
    <span id="searchValue" [innerHTML]="searchValue"></span>
    ...
```

For this particular type of vulnerability, given the Juice Store application is written in Angular,
the search term may passed to the `DomSanitizer.santize` method before being passed to `innerHTML`.
See [here](https://angular.io/api/platform-browser/DomSanitizer) for more on `DomSanitizer` and it's
associated methods.

## Action

* **Recommend a code review and update business logic for next deployment.**
