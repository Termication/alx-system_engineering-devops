tack Debugging Tasks

## Overview

This project involves two web stack debugging tasks where we aim to optimize the performance and stability of a web server setup running Nginx under heavy load and fix OS configuration issues that prevent a user from logging in due to file descriptor limits.

### Task 0: Sky is the Limit, Let's Bring That Limit Higher

In this task, we are testing the performance of a web server setup featuring Nginx. The server was subjected to a stress test using ApacheBench, a popular benchmarking tool that simulates HTTP requests to a web server. The objective was to determine how the server handles a high volume of requests and to fix any issues that arise.

#### Problem

Initially, the server was not handling the load efficiently, resulting in a significant number of failed requests. Out of 2000 requests, 943 requests failed, indicating that the server's configuration was inadequate for the given load.

#### Solution

To resolve this, we modified the server configuration to improve its ability to handle concurrent requests. After applying the configuration changes using a Puppet script (`0-the_sky_is_the_limit_not.pp`), we re-ran the benchmark, and the server successfully handled all 2000 requests without any failures.

#### Benchmarking Results

**Before Fix:**

- **Failed Requests:** 943
- **Requests per second:** 5664.01
- **Time per request:** 17.655 ms
- **Transfer rate:** 3309.15 KB/sec

**After Fix:**

- **Failed Requests:** 0
- **Requests per second:** 6650.99
- **Time per request:** 15.035 ms
- **Transfer rate:** 5540.33 KB/sec

### Task 1: User Limit

In this task, we encountered an issue where the `holberton` user was unable to log in and perform basic operations due to the "Too many open files" error. This error occurs when the system reaches its limit on the number of file descriptors that can be opened simultaneously.

#### Problem

The `holberton` user was unable to log in or execute commands due to the system's file descriptor limit being too low, leading to a "Too many open files" error.

#### Solution

We resolved this issue by increasing the system's file descriptor limit for the `holberton` user. The configuration change was applied using a Puppet script (`1-user_limit.pp`). After the fix, the user was able to log in and perform operations without encountering the error.

#### Steps to Reproduce and Fix

1. **Login Error:**
   ```bash
   su - holberton
   -su: /etc/profile: Too many open files
```
