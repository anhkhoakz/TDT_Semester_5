const jwt = require("jsonwebtoken");
const { JWT_SECRET } = process.env;

exports.verifyToken = (req, res, next) => {
    const token = req.headers.authorization;
    if (!token)
        return res.status(401).json({ code: 401, message: "Unauthorized" });
    jwt.verify(token, JWT_SECRET, (err, decoded) => {
        if (err)
            return res.status(401).json({ code: 401, message: "Unauthorized" });
        req.user = decoded;
        next();
    });
};
