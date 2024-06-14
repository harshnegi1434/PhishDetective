# Use the official Node.js LTS (Long Term Support) image
FROM node:lts-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if present)
COPY package.json ./

# Install dependencies using npm
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port Next.js is running on (default is 3000)
EXPOSE 3000

# Set environment variables
ENV NODE_ENV=development

# Command to run the application
CMD ["npm", "run", "dev"]
