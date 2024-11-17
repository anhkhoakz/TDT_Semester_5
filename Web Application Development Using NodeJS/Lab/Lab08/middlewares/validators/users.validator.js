const form = require("express-form");
const { body, validationResult } = require("express-validator");

exports.validateCreateUser = form(
    body("email", "Email is required").notEmpty().isEmail(),
    body("password", "Password is required").notEmpty().isLength({ min: 6 }),
    (req, res, next) => {
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        next();
    }
);

exports.validateLogin = form(
    body("email", "Email is required").notEmpty().isEmail(),
    body("password", "Password is required").notEmpty().isLength({ min: 6 }),
    (req, res, next) => {
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        next();
    }
);
