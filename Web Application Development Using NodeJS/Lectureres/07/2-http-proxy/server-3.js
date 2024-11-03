const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");

const app = express();

app.get("/", (req, res) => {
    res.json({
        msg: "Welcome to proxy server",
        products: "http://localhost:8000",
        users: "http://localhost:8001",
    });
});

app.use(
    "/products",
    createProxyMiddleware({
        target: "http://localhost:8001",
        changeOrigin: true,
        pathRewrite: {
            "^/products": "/",
        },
    })
);
app.use(
    "/users",
    createProxyMiddleware({
        target: "http://localhost:8000",
        changeOrigin: true,
        pathRewrite: {
            "^/users": "/",
        },
    })
);

app.listen(8002, () => {
    console.log("Server running on port 8002");
});
