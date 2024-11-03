const express = require("express");
const app = express();

const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 3, name: "Charlie" },
    { id: 4, name: "David" },
    { id: 5, name: "Eve" },
];

app.get("/", (req, res) => {
    res.json(users);
});

app.listen(8000, () => {
    console.log("Server running on port 8000");
});
