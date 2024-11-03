const express = require("express");
const router = express.Router();
const { getUsers, getUserById, addUser } = require("../controllers/users");

/* GET users listing. */
router.get("/", async (req, res, next) => {
    const users = await getUsers();
    res.send(users);

});

router.get("/add", (req, res, next) => {
    res.render("add");
});

router.post("/add", (req, res, next) => {
    const users = req.body;
    res.send(addUser(users));
});

router.post("/", (req, res, next) => {
    const users = req.body();
    res.send(addUser(users));
});

router.get("/:id", (req, res, next) => {
    const id = req.body();
    res.send(getUserById(id));
});

router.delete("/:id", (req, res, next) => {
    const id = req.body();
    res.send(getUserById(id));
});
router.put("/:id", (req, res, next) => {
    const id = req.body();
    res.send(getUserById(id));
});
router.patch("/:id", (req, res, next) => {
    const id = req.body();
    res.send(getUserById(id));
});



module.exports = router;
