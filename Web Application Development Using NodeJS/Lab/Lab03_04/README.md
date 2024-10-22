#

## Rate Limit

To implement rate limiting in your project, you can use the `express-rate-limit` middleware. Here’s how you can do it:

1. **Install the `express-rate-limit` package**:

    ```sh
    npm install express-rate-limit
    ```

2. **Create a rate limiter middleware**:
   Create a new file middlewares/rateLimiter.js and add the following code:

    ```js
    const rateLimit = require("express-rate-limit");

    const limiter = rateLimit({
        windowMs: 15 * 60 * 1000, // 15 minutes
        max: 100, // limit each IP to 100 requests per windowMs
        message:
            "Too many requests from this IP, please try again after 15 minutes",
    });

    module.exports = limiter;
    ```

3. **Apply the rate limiter middleware**:
   In your

index.js

file, apply the rate limiter middleware to your routes:
```js
const express = require('express');
const app = express();
const rateLimiter = require('./middlewares/rateLimiter');

    // Apply rate limiter to all requests
    app.use(rateLimiter);

    // Other middlewares and routes
    app.use(require('./routes/index'));
    app.use(require('./routes/add'));
    app.use(require('./routes/error'));
    app.use(require('./routes/login'));
    app.use(require('./routes/product'));

    const PORT = process.env.PORT || 3000;
    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });
    ```

This setup will limit each IP to 100 requests per 15 minutes across all routes. You can adjust the `windowMs` and `max` options to fit your needs.
