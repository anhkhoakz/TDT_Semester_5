const mysql = require("mysql2");
const dotenv = require("dotenv");

dotenv.config();

const pool = mysql.createPool({
    host: "localhost",
    user: "root",
    // password: "",
    database: "file_manager",
    port: 3306,
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0,
    maxIdle: 10,
    idleTimeout: 60000,
    enableKeepAlive: true,
    keepAliveInitialDelay: 0,
});

pool.getConnection((err, connection) => {
    if (err) {
        console.error("Error connecting to the database:", err);
        if (err.code === "ECONNREFUSED") {
            console.error(
                "Connection refused. Please ensure the MySQL server is running and the connection details are correct."
            );
        }
        return;
    }
    console.log("Connected to the database");
    connection.release();
});

module.exports = pool.promise();
