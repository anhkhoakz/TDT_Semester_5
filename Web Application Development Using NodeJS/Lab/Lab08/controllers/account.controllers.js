const Account = require("../models/accounts.models");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const { JWT_SECRET } = process.env;

const emailRegex =
    /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/gi;

exports.getAllAccounts = async (req, res) => {
    try {
        const accounts = await Account.find();
        res.status(200).json(accounts);
    } catch (err) {
        res.status(500).json({ error: err });
    }
};

exports.createAccount = async (req, res) => {
    const { email, password } = req.body;

    const areEmptyFields = !email || !password;

    if (areEmptyFields)
        return res
            .status(400)
            .json({ code: 400, message: "Missing required fields" });

    const isValidEmail = emailRegex.test(email);
    if (!isValidEmail)
        return res.status(400).json({ code: 400, message: "Invalid email" });

    const existingAccount = await Account.findOne({ email: email });
    if (existingAccount)
        return res
            .status(403)
            .json({ code: 403, message: "Email already registered" });

    const hashedPassword = await bcrypt.hash(password, 10);

    const newAccount = new Account({
        email,
        password: hashedPassword,
    });

    newAccount
        .save()
        .then((result) => {
            res.status(201).json({
                message: "Account created successfully",
                Account: result,
            });
        })
        .catch((err) => {
            res.status(500).json({
                code: 500,
                error: err.message,
            });
        });
};

exports.login = async (req, res) => {
    const { email, password } = req.body;

    const areEmptyFields = !email || !password;
    if (areEmptyFields)
        return res
            .status(400)
            .json({ code: 400, message: "Missing required fields" });

    const isValidEmail = emailRegex.test(email);
    if (!isValidEmail)
        return res.status(400).json({ code: 400, message: "Invalid email" });

    const account = await Account.findOne({ email: email });
    if (!account)
        return res
            .status(404)
            .json({ code: 404, message: "Account not found" });

    const isValidPassword = await bcrypt.compare(password, account.password);
    if (!isValidPassword)
        return res.status(401).json({ code: 401, message: "Invalid password" });

    const token = jwt.sign(
        { email: account.email, _id: account._id },
        JWT_SECRET
    );
    res.status(200).json({ token });
};
