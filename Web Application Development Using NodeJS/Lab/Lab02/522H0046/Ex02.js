const http = require("http");
const fs = require("fs");
const path = require("path");
const querystring = require("querystring");

const server = http.createServer(async (req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/html; charset=utf-8",
    });
    if (req.url === "/") {
        const filePath = path.join(__dirname, "views/login.html");
        const html = fs.readFileSync(filePath);
        return res.end(html);
    } else if (req.url.startsWith("/login")) {
        if (req.method != "POST") {
            return res.end(req.method + " method is not supported");
        }
        let { email, password } = await parseBody(req);
        if (email !== "admin@gmail.com") {
            return res.end("Invalid email");
        } else if (password !== "123456") {
            return res.end("Invalid password");
        }
        return res.end("Login Successfully");
    } else {
        return res.end("Invalid URL");
    }
});

const parseBody = (req) => {
    return new Promise((resolve, reject) => {
        let body = "";
        req.on("data", (data) => {
            body += data;
        });

        req.on("end", () => {
            try {
                if (req.headers["content-type"] === "application/json") {
                    resolve(JSON.parse(body));
                } else if (
                    req.headers["content-type"] ===
                    "application/x-www-form-urlencoded"
                ) {
                    resolve(querystring.parse(body));
                } else {
                    reject(new Error("Unsupported content type"));
                }
            } catch (error) {
                reject(error);
            }
        });
    });
};

server.listen(8080, () => {
    console.log("Server is listening on http://localhost:8080");
});
