const session = require("express-session");

module.exports = session({
    secret:
        "QzdHwIl/VrIPqCOmUbkEArg+G/NBx+eN5+sm6PkpvhQ=" ||
        process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
});
