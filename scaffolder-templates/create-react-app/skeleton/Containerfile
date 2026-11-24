# Stage 1: Build the React application using Node.js 20 on Red Hat UBI 9
FROM registry.access.redhat.com/ubi9/nodejs-20:latest AS builder

WORKDIR /opt/app-root/src

# Enable legacy OpenSSL cryptographic provider for react-scripts 4 / Webpack 4 on Node 20
ENV NODE_OPTIONS="--openssl-legacy-provider"

# Install application dependencies
COPY package.json tsconfig.json ./
RUN npm install

# Copy source code and build production bundle
COPY public ./public
COPY src ./src
RUN npm run build

# Stage 2: Serve production bundle with Red Hat UBI 9 Nginx 1.24
FROM registry.access.redhat.com/ubi9/nginx-124:latest

WORKDIR /opt/app-root/src

# Copy built static files to Nginx document root
COPY --from=builder /opt/app-root/src/build ./

# Expose unprivileged port 8080
EXPOSE 8080

# Start Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
