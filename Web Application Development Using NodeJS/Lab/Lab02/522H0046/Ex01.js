const http = require("http");
const URL = require("url");
const queryString = require("querystring");

const server = http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/html charset=utf-8",
    });

    if (req.url === "/") {
        return res.end(`<!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Ex01</title>
          <link
            rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
          />
        </head>

        <body>
          <main class="container">
            <form action="/result" method="get">
              <label for="n1">Số hạng 1</label>
              <input type="number" name="n1" id="n1" required />
              <label for="n2">Số hạng 2</label>
              <input type="number" name="n2" id="n2" required />
              <label for="operation">Phép tính</label>
              <select name="operation" id="operation" >
                <option value="default" selected>Chọn phép tính</option>
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
              </select>
              <button type="submit">Tính</button>
            </form>
          </main>
        </body>
      </html>
`);
    } else if (req.url.startsWith("/result")) {
        const url = URL.parse(req.url);
        const query = queryString.decode(url.query);

        let { n1, n2, operation } = query;
        n1 = parseInt(n1);
        n2 = parseInt(n2);

        if (isNaN(n1) || isNaN(n2)) {
            res.end("Invalid number");
            return;
        }
        if (operation === "default") {
            return res.end("You haven't choose the operation");
        }

        let result;
        switch (operation) {
            case "+":
                result = n1 + n2;
                break;
            case "-":
                result = n1 - n2;
                break;
            case "*":
                result = n1 * n2;
                break;
            case "/":
                result = n2 !== 0 ? n1 / n2 : "Cannot divide by zero";
                break;
            default:
                result = "Invalid operation";
                break;
        }

        return res.end(`${n1} ${operation} ${n2} = ${result}`);
    } else {
        return res.end("Invalid URL");
    }
});

server.listen(8080, () => {
    console.log("Server running on http://localhost:8080");
});
