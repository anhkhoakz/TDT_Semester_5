const express = require("express");
const router = express.Router();
const { getUsers } = require("../controllers/users");

router.get("/", async (req, res, next) => {
    try {
        const users = await getUsers();
        res.render("index", { users });
    } catch (error) {
        console.error(error);
        res.status(500).send("Internal Server Error");
    }
});

module.exports = router;
