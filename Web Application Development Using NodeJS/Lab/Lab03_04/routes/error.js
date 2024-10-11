const express = require("express");
const router = express.Router();

router.get("/", (req, res, next) => {
    return res.render("error", {
        title: "404 Not Found",
        message: "Page not found",
    });
});

module.exports = router;
