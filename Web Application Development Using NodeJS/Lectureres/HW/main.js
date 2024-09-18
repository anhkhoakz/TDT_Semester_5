const http = require("http");
const fs = require("fs");

const port = 3000;

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        const indexFilePath = "./index.html";
        const htmlFile = fs.readFileSync(indexFilePath);
        res.writeHead(200, {
            "Content-Type": "text/html",
        });
        res.end(htmlFile);
    } else if (req.url === "/image.jpg") {
        const imageFilePath = "./image.jpg";
        const imageFile = fs.readFileSync(imageFilePath);
        res.writeHead(200, {
            "Content-Type": "image/jpeg",
        });
        res.end(imageFile);
    } else {
        res.writeHead(404, {
            "Content-Type": "application/json",
        });
        res.end(
            JSON.stringify({ error: 1, message: "The path is not supported" })
        );
    }
});

server.listen(port, () => {
    console.log(`Server is listening on http://localhost:${port}`);
});
