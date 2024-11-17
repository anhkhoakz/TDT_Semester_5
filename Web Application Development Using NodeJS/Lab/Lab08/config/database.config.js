const mongoose = require("mongoose");
const dotenv = require("dotenv");
dotenv.config();
const { DB_URL } = process.env;

const mongodb = {
    connect: async () => {
        mongoose
            .connect(DB_URL)
            .then(() => console.log("✅ Database connected"))
            .catch(() => console.error("❌ Database connection error"));
        mongoose.Promise = global.Promise;
    },
    disconnect: async () => {
        await mongoose.disconnect();
    },
};

module.exports = mongodb;
