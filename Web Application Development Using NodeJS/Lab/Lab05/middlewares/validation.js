const { check, validationResult } = require("express-validator");

const userValidationRules = () => {
    return [
        check("fullName").notEmpty().withMessage("Full Name is required"),
        check("email").isEmail().withMessage("Email is invalid"),
        check("gender").notEmpty().withMessage("Gender is required"),
        check("age")
            .isInt({ min: 0 })
            .withMessage("Age must be a positive integer"),
    ];
};

const validate = (req, res, next) => {
    const errors = validationResult(req);
    if (errors.isEmpty()) {
        return next();
    }
    const extractedErrors = [];
    errors.array().map((err) => extractedErrors.push({ [err.param]: err.msg }));

    req.flash("error", extractedErrors);
    res.redirect("back");
};

module.exports = {
    userValidationRules,
    validate,
};
