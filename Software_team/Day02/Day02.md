## XMLHttpRequest

XMLHttpRequest (XHR) objects are used to interact with servers. You can retrieve data from a URL without having to do a full page refresh. This enables a Web page to update just part of a page without disrupting what the user is doing.
EventTarget XMLHttpRequestEventTarget XMLHttpRequest

Despite its name, XMLHttpRequest can be used to retrieve any type of data, not just XML.

If your communication needs to involve receiving event data or message data from a server, consider using server-sent events through the EventSource interface. For full-duplex communication, WebSockets may be a better choice.

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "/server", true);

xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
        console.log("The request succeeded!");
        console.log(xhr.responseText);
    } else {
        console.log("The request failed!");
    }
};

xhr.onerror = function () {
    console.log("The request failed!");
};

xhr.send();
```

## Promise

An asynchronous operation's future value is represented as a promise, which enables handlers to be configured for either success or failure. This makes it possible for asynchronous methods to return promises, which will ultimately yield the outcome. There are three states for a promise:

**Pending**: the starting point.
**Fulfilled**: The procedure has successfully finished.
**Rejected**: The operation was unsuccessful.

## Fetch API

Through the `fetch()` function and associated `Request` and `Response` objects, the Fetch API offers capabilities for managing network requests. By providing a resource path, the `fetch()` method—which is accessible worldwide in both Window and Worker contexts—is utilized to seek resources. Even in the event of an HTTP error, it produces a Promise that resolves to a `Response` object as soon as the server replies with headers. The request can also be customized by providing an optional configuration object.

The response body content can be managed using the methods provided by the `Response` object. `Request` and `Response` objects are usually formed by other API activities, like in service workers, although they can be created directly. Furthermore, the HTTP Origin header and CORS, which deal with security and cross-origin queries, are supported by the Fetch API.

```javascript
fetch("/server")
    .then((response) => {
        if (!response.ok) {
            throw new Error("The request failed!");
        }
        return response.text();
    })
    .then((data) => {
        console.log("The request succeeded!");
        console.log(data);
    })
    .catch((error) => {
        console.log(error);
    });
```

```javascript
try {
    const response = await fetch("/server");
    if (!response.ok) {
        throw new Error("The request failed!");
    }
    const data = await response.text();
    console.log("The request succeeded!");
    console.log(data);
} catch (error) {
    console.log(error);
}
```

## Axios

What is Axios?

Axios is a promise-based HTTP Client for node.js and the browser. It is isomorphic (= it can run in the browser and nodejs with the same codebase). On the server-side it uses the native node.js http module, while on the client (browser) it uses XMLHttpRequests.

### Features

-   Make XMLHttpRequests from the browser
-   Make http requests from node.js
-   Supports the Promise API
-   Intercept request and response
-   Transform request and response data
-   Cancel requests
-   Timeouts
-   Query parameters serialization with support for nested entries
-   Automatic request body serialization to:
-   JSON (application/json)
-   Multipart / FormData (multipart/form-data)
-   URL encoded form (application/x-www-form-urlencoded)
-   Posting HTML forms as JSON
-   Automatic JSON data handling in response
-   Progress capturing for browsers and node.js with extra info (speed rate, remaining time)
-   Setting bandwidth limits for node.js
-   Compatible with spec-compliant FormData and Blob (including node.js)
-   Client side support for protecting against XSRF

### Installation

```bash
npm install axios
```

Using jsDelivr CDN:

```html
<script
    src="https://cdn.jsdelivr.net/npm/axios@1.7.7/dist/axios.min.js"
    integrity="sha256-9bKyYHG7WfRmaDNW3xG1OSYUz2lmWGkXmQxl1Irw3Lk="
    crossorigin="anonymous"
></script>
```

### Example ```javascript const axios = require("axios"); axios .get("/server")

.then((response) => { console.log("The request succeeded!");
console.log(response.data); }) .catch((error) => { console.log("The request
failed!"); });

```

## Axios vs Fetch

#### Key Points on Axios and Fetch API Comparison

-   **Feature Limitations with Fetch**:
    -   Fetch API is built into the browser but lacks several advanced features by default.
-   **Flexibility with Fetch**:
    -   Developers can manually implement missing features from Axios (like request/response interceptors, automatic JSON handling, and request cancellation) on top of the Fetch API.

#### Advantages of Using Axios

-   **Out-of-the-Box Features**:
    -   Axios provides a range of features by default that streamline HTTP requests, reducing the need for additional code.
-   **Enhanced Developer Experience**:
    -   With built-in utilities, Axios can simplify API interactions more than Fetch does without extra setup.
```
