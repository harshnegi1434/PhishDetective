# Use the official Node.js LTS (Long Term Support) image
FROM node:lts-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json 
COPY package.json ./

# Install dependencies using npm
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Next.js project
RUN npm run build

# Expose the port Next.js
EXPOSE 3000

# Start the Next.js application
CMD ["npm", "run", "dev"]
