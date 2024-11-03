const express = require("express");
const {
    getUsers,
    getUserById,
    addUser,
    deleteUser,
    updateUser,
    patchUser,
} = require("../controllers/users");

const router = express.Router();

/* GET users listing. */
router.get("/", async (req, res) => {
    const users = await getUsers();
    res.send(users);
});

router.get("/add", (req, res) => {
    res.render("add", { error: null });
});

router.post("/add", (req, res) => {
    const user = req.body;

    if (!user.fullName || !user.email) {
        return res.render("add", { error: "Name and email are required" });
    }

    try {
        addUser(user);
        req.flash("success", "User added successfully");
        res.redirect("/");
    } catch (error) {
        req.flash("error", "Error adding user");
        res.render("error", { error, message: error.message });
    }
});

router.post("/", (req, res) => {
    const user = req.body;
    res.send(addUser(user));
});

router.get("/:id", async (req, res) => {
    const { id } = req.params;
    try {
        const user = await getUserById(id);
        console.log(user);

        res.render("profile", { user });
    } catch (error) {
        res.status(500).send("Error fetching user");
    }
});

router.delete("/:id", async (req, res) => {
    const { id } = req.params;
    try {
        await deleteUser(id);
        req.flash("success", "User deleted successfully");
        res.status(200).send({ message: "User deleted successfully" });
    } catch (error) {
        req.flash("error", "Error deleting user");
        res.status(500).send({ error: "Error deleting user" });
    }
});

router.get("/:id/edit", async (req, res) => {
    const { id } = req.params;
    try {
        const user = await getUserById(id);
        res.render("edit", { user });
    } catch (error) {
        res.status(500).send("Error fetching user");
    }
});

router.put("/:id/edit", async (req, res) => {
    const { id } = req.params;
    const user = req.body;
    try {
        await updateUser(id, user);
        req.flash("success", "User updated successfully");
        res.redirect("/");
    } catch (error) {
        req.flash("error", "Error updating user");
        res.status(500).send({ error: "Error updating user" });
    }
});

router.patch("/:id/edit", async (req, res) => {
    const { id } = req.params;
    const user = req.body;
    try {
        await patchUser(id, user);
        req.flash("success", "User updated successfully");
        res.status(200).send({ message: "User updated successfully" });
    } catch (error) {
        req.flash("error", "Error updating user");
        res.status(500).send({ error: "Error updating user" });
    }
});

module.exports = router;
