const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.get("/image.jpg", (req, res) => {
    res.sendFile(__dirname + "/image.jpg");
});

app.get("*", (req, res) => {
    res.status(404).json({ error: 1, message: "The path is not supported" });
});

app.listen(3000, () => {
    console.log("http://localhost:3000");
});
