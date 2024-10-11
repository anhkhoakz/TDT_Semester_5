const express = require("express");
const router = express.Router();

router.get("/", async (req, res, next) => {
    if (!req.session.isLoggedIn) {
        // return res.redirect("/login"); // TODO: Uncomment this line
    }
    const products = await (
        await fetch("http://localhost:8081/products")
    ).json();

    res.render("index", { products });
});

module.exports = router;
