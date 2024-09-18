// Create route to show a table n rows and m columns, each cell contains value of i+j, where i is row, j is column. (Note: n, m is set in code)

const express = require("express");
const app = express();
const port = 8080;

app.get("/", (req, res) => {
    let n = 5;
    let m = 5;
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
    console.log(`Server running at http:localhost:${port}/`);
});
