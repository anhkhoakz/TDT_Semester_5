const form = require("express-form");
const { body, validationResult, param } = require("express-validator");

exports.validataGetProduct = form(
    param("id", "Product ID is required").notEmpty().isMongoId(),

    (req, res, next) => {
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        next();
    }
);

exports.validateCreateProduct = form(
    body("name", "Name is required").notEmpty(),
    body("price", "Price is required").notEmpty().isNumeric(),
    body("image", "Image is required").notEmpty(),
    body("description", "Description is required").notEmpty(),

    (req, res, next) => {
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        next();
    }
);

exports.validateUpdateProduct = form(
    param("id", "Product ID is required").notEmpty().isMongoId(),

    (req, res, next) => {
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        next();
    }
);

exports.validateDeleteProduct = form(
    param("id", "Product ID is required").notEmpty().isMongoId(),

    (req, res, next) => {
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        next();
    }
);
