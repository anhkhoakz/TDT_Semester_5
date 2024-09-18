const express = require("express");

const app = express();
const port = 3030;

app.get("/", (req, res) => {
    const n = 5;
    const m = 5;
    let table = "<table>";
    for (let i = 0; i < n; i++) {
        table += "<tr>";
        for (let j = 0; j < m; j++) {
            table += `<td>${i + j}</td>`;
        }
        table += "</tr>";
    }
    table += "</table>";
    res.send(table);
});

app.listen(port, () => {
    console.log(`Server listening on http://localhost:${port}`);
});
