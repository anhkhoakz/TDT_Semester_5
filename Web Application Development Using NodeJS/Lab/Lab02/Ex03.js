const http = require("http");
const URL = require("url");
let students = new Map();

students.set("1", {
    id: 1,
    name: "Nguyen Van A",
});

students.set("2", {
    id: 2,
    name: "Nguyen Van B",
});

students.set("3", {
    id: 3,
    name: "Nguyen Van C",
});

students.set("4", {
    id: 4,
    name: "Nguyen Van D",
});

// console.log(student.values());

const server = http.createServer(async (req, res) => {
    const url = URL.parse(req.url);
    const pattern = /^\/students\/\d+$/g;
    const requestMethod = req.method;

    if (url.pathname === "/students") {
        if (requestMethod === "GET") {
            res.writeHead(200, {
                "Content-Type": "application/json charset=utf-8",
            });
            return res.end(JSON.stringify([...students.values()]));
        } else if (requestMethod === "POST") {
            // console.log("POST");
            const newStudent = await parseBody(req);
            // console.log(newStudent);
            students.set(newStudent.id, newStudent);
            res.writeHead(201, {
                "Content-Type": "application/json; charset=utf-8",
            });
            return res.end(JSON.stringify(newStudent));
        } else {
            res.writeHead(405, {
                "Content-Type": "application/json charset=utf-8",
            });
            return res.end(
                JSON.stringify({
                    code: 405,
                    error: `${requestMethod} method is not supported`,
                })
            );
        }
    } else if (url.pathname.match(pattern)) {
        // console.log("Matched");

        const id = url.pathname.split("/")[2];

        if (requestMethod === "GET") {
            res.writeHead(200, {
                "Content-Type": "application/json charset=utf-8",
            });
            return res.end(JSON.stringify(students.get(id)));
        } else if (requestMethod === "PUT") {
            const body = await parseBody(req);
            students.set(id, body);
            res.writeHead(200, {
                "Content-Type": "application/json charset=utf-8",
            });
            return res.end(JSON.stringify(body));
        } else if (requestMethod === "DELETE") {
            students.delete(id);
            res.writeHead(204, {
                "Content-Type": "application/json charset=utf-8",
            });
            return res.end(
                JSON.stringify({ code: 204, message: `Student ${id} deleted` })
            );
        }
    } else {
        res.writeHead(404, {
            "Content-Type": "application/json charset=utf-8",
        });
        return res.end(JSON.stringify({ code: 104, message: "Invalid URL" }));
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
                resolve(JSON.parse(body));
            } catch (error) {
                reject(error);
            }
        });
    });
};

server.listen(8080, () => {
    console.log("Server is listening on http://localhost:8080");
});
