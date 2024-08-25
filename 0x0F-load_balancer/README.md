# Load Balancer Setup with HAProxy

This README provides instructions on how to set up a simple load balancer using HAProxy. The load balancer will distribute traffic across multiple backend servers using a round-robin algorithm. The setup is intended for HTTP traffic on port 80.

## Prerequisites

- A Linux-based system with `apt` package manager (e.g., Ubuntu).
- Two or more backend servers to balance traffic.
- Root or sudo privileges to install packages and modify system configurations.

## Steps to Install and Configure HAProxy

### 1. Update the System

Ensure your system's package list is up-to-date:

```bash
sudo apt-get -y update
```

### 2. Install HAProxy

Install HAProxy using the package manager:

```bash
sudo apt-get -y install haproxy
```

### 3. Configure HAProxy

Modify the HAProxy configuration to set up a frontend and backend. In this example, we define a frontend named Innocent that listens on port 80 and uses round-robin load balancing to distribute traffic across two backend servers.

Append the following configuration to the HAProxy config file:

```bash
sudo tee -a /etc/haproxy/haproxy.cfg > /dev/null <<EOL

frontend Innocent
        bind *:80
        mode http
        default_backend app

backend app
        balance roundrobin
        server 459074-web-01 184.72.96.209:80 check
        server 459074-web-02 100.25.152.248:80 check
EOL
```

### 4. Validate Configuration

Before applying the new configuration, ensure there are no syntax errors:

```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

### 5. Restart HAProxy

After validating the configuration, restart HAProxy to apply the changes:

```bash
sudo systemctl restart haproxy
```

### 6. Verify HAProxy Status

Check the status of HAProxy to ensure it's running and configured correctly:

```bash
sudo systemctl status haproxy

$curl -Is 34.227.92.1
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Sun, 25 Aug 2024 12:10:32 GMT
content-type: text/html
content-length: 13
last-modified: Sat, 24 Aug 2024 13:48:15 GMT
etag: "66c9e49f-d"
x-served-by: 459074-web-01
accept-ranges: bytes

$curl -Is 34.227.92.1
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Sun, 25 Aug 2024 12:10:36 GMT
content-type: text/html
content-length: 13
last-modified: Sun, 25 Aug 2024 10:38:20 GMT
etag: "66cb099c-d"
x-served-by: 459074-web-02
accept-ranges: bytes
```
