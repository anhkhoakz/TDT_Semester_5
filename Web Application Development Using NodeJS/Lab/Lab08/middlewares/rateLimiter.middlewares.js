const rateLimit = require("express-rate-limit");

const rateLimiter = rateLimit({
    legacyHeaders: true,
    limit: 100,
    message: "Too many requests, please try again in 15 minutes",
    standardHeaders: true,
    windowMs: 15 * 60 * 1000,
    keyGenerator: (req) => {
        return req.headers["x-forwarded-for"] || req.connection.remoteAddress;
    },
});

module.exports = rateLimiter;
