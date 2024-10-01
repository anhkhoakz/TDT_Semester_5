const express = require("express");
const app = express();

// middleware
app.use((req, res, next) => {
    res.display = (view, data) => {
        let html = require("fs").readFileSync(
            __dirname + `/${view}.html`,
            "utf8"
        );
        data.forEach((d, i) => {
            html = html.replace(new RegExp(`\d`, "g"), d);
        });
    };
    next();
});

app.use("/", (req, res) => {
    res.display("index", ["Hello", "I love you", "3000"]);
});

app.listen(3000, () => {
    console.log("http://localhost:3000");
});
