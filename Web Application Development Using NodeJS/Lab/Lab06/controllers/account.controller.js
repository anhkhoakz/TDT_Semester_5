const bcrypt = require("bcrypt");
const pool = require("../configs/database");
const fs = require("fs");
const path = require("path");

const createAccount = async (req, res) => {
    const { confirmPassword, name, email, password } = req.body;

    try {
        const [user] = await pool.query("SELECT * FROM users WHERE email = ?", [
            email,
        ]);

        if (user.length > 0) {
            return res.render("register", {
                error: "User already exists",
            });
        }

        // Check if the password and confirmPassword match
        if (password !== confirmPassword) {
            return res.render("register", {
                error: "Passwords do not match",
            });
        }

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Insert the user into the database
        await pool.query(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            [name, email, hashedPassword]
        );

        // create a directory for the user by user id in mysql
        const [newUser] = await pool.query(
            "SELECT * FROM users WHERE email = ?",
            [email]
        );

        const dir = path.join(__dirname, `../uploads/${newUser[0].id}`);

        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir);
        }

        res.render("login", {
            error: null,
        });
    } catch (error) {
        console.error(error);
        res.render("register", {
            error: "An error occurred while creating the account",
        });
    }
};

const login = async (req, res) => {
    const { email, password } = req.body;

    try {
        const [user] = await pool.query("SELECT * FROM users WHERE email = ?", [
            email,
        ]);

        if (user.length === 0) {
            return res.render("login", {
                error: "Invalid email or password",
            });
        }

        const isPasswordValid = await bcrypt.compareSync(
            password,
            user[0].password
        );

        if (!isPasswordValid) {
            return res.render("login", {
                error: "Invalid email or password",
            });
        }

        req.session.user = user[0];
        res.redirect("/");
    } catch (error) {
        res.render("login", {
            error: "An error occurred while logging in",
        });
    }
};

module.exports = {
    createAccount,
    login,
};
