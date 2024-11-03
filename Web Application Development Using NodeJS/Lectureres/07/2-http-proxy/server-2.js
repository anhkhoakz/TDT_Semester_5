const express = require("express");
const app = express();

const products = [
    { id: 1, name: "Apple" },
    { id: 2, name: "Banana" },
    { id: 3, name: "Cherry" },
    { id: 4, name: "Date" },
    { id: 5, name: "Elderberry" },
];

app.get("/", (req, res) => {
    res.json(products);
});

app.listen(8001, () => {
    console.log("Server running on port 8001");
});
