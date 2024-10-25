# Day 01

## Kiến trúc của NodeJs

[Introduction to NodeJS](https://docs.google.com/presentation/d/1Y1pQ6rT22EA6rb7p0SFskR7gDZiUTAKe/)

## Đặc điểm NodeJs

[What are the Key Features of Node.js ?](https://www.geeksforgeeks.org/what-are-the-key-features-of-node-js/)

## Tìm hiểu về 'template literal' module ES6

[How to Use Template Literals in JavaScript](https://www.freecodecamp.org/news/template-literals-in-javascript/)

### Example Code

```javascript
const name = "Khoa";
const age = 18;
const sentence = `My name is ${name} and I am ${age} years old.`;
```

## Tìm hiểu localStorage và sessionStorage, so sánh

[Window: localStorage property](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

[Window: sessionStorage property](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage)

### Difference

-   `localStorage` stores data with no expiration date.
-   `sessionStorage` stores data for one session (data is lost when the browser tab is closed).

### Example Code

```javascript
localStorage.setItem("name", "Khoa");
localStorage.getItem("name");
localStorage.removeItem("name");
localStorage.clear();
```

```javascript
sessionStorage.setItem("name", "Khoa");
sessionStorage.getItem("name");
sessionStorage.removeItem("name");
sessionStorage.clear();
```

## Tìm hiểu về 'http' module

[Node.js HTTP Module](https://docs.google.com/presentation/d/1Y1pQ6rT22EA6rb7p0SFskR7gDZiUTAKe/edit#slide=id.p15)

### Example Code

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Hello World!");
});

server.listen(3000, () => {
    console.log("Server is running on port 3000");
});
```

## Tìm hiểu về 'fs' module

[FileSystem](https://developer.mozilla.org/en-US/docs/Web/API/FileSystem)

### Example Code

```javascript
const fs = require("fs");

fs.readFile("file.txt", "utf8", (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
```
