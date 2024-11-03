const cluster = require("cluster");
const http = require("http");
const numCPUs = require("os").cpus().length;

if (cluster.isMaster) {
    // Fork workers.
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }

    cluster.on("exit", function (worker, code, signal) {
        console.log("worker " + worker.process.pid + " died");
    });
} else {
    // Workers can share any TCP connection
    // In this case its a HTTP server
    http.createServer((req, res) => {
        res.writeHead(200);
        res.end("hello world from worker " + cluster.worker.id + "\n");
        let s = 0;
        for (let i = 0; i < 100000000000000; i++) {
            s += i;
            console.log(s);
        }
    }).listen(8000);
    console.log("Worker %d running!", cluster.worker.id);
}
