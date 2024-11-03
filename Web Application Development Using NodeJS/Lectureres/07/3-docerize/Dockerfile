# Write docerfile for nodejs express


# Use the official image as a parent image

FROM node:18

# Set the working directory

WORKDIR /usr/src/app

# Copy the file from your host to your current location

COPY package*.json ./

# Run the command inside your image filesystem

RUN npm install --only=production

# Copy the rest of the application code

COPY . .

# Inform Docker that the container is listening on the specified port at runtime

EXPOSE 8080

# Run the specified command within the container

CMD [ "node", "server.js" ]

