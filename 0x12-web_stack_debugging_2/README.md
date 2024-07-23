# Web Stack Debugging

## Introduction
Debugging usually takes a significant amount of a software engineer’s time. The art of debugging is challenging and takes years, even decades, to master. Seasoned software engineers excel at it due to their experience. They have encountered lots of broken code, buggy systems, weird edge cases, and race conditions.

## Non-exhaustive Guide to Debugging

### School Specific
If you are struggling with something that is run on the checker, like a Bash script or a piece of code, remember that you can simulate the flow by starting a Docker container with the distribution specified in the requirements and running your code. Check the Docker concept page for more information.

### Test and Verify Your Assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

1. **Is the web server started?** 
   - Check using the service manager, and double-check by examining the process list.
2. **On what port should it listen?** 
   - Check your web server configuration.
3. **Is it actually listening on this port?** 
   - Use `netstat -lpdn` (run as root or sudo to see the process for each listening port).
4. **Is it listening on the correct server IP?** 
   - `netstat` is also useful here.
5. **Is there a firewall enabled?**
6. **Have you looked at logs?** 
   - Usually found in `/var/log` and `tail -f` is your friend.
7. **Can I connect to the HTTP port from the location I am browsing from?** 
   - `curl` is your friend.

There is a good chance that at this point, you will have found part of the issue.

### Get a Quick Overview of the Machine State
Watch the [YouTube video "First 5 Commands When I Connect on a Linux Server"](https://www.youtube.com/watch?v=...)

When you connect to a server/machine/computer/container, you want to understand what’s happened recently and what’s happening now. You can do this with 5 commands in a minute or less:

1. **`w`**
   - Shows server uptime, which is the time during which the server has been continuously running.
   - Shows which users are connected to the server.
   - Load average will give you a good sense of the server health.
2. **`history`**
   - Shows which commands were previously run by the user you are currently connected to.
   - You can learn a lot about what type of work was previously performed on the machine and what could have gone wrong with it.
3. **`top`**
   - Shows what is currently running on this server.
   - Orders results by CPU, and memory utilization, and catches the ones that are resource-intensive.
4. **`df`**
   - Shows disk utilization.
5. **`netstat`**
   - Shows what port and IP your server is listening on.
   - Shows what processes are using sockets.
   - Try `netstat -lpn` on a Ubuntu machine.

### Machine
Debugging is about verifying assumptions. In a perfect world, the software or system we are working on would be functioning perfectly, the server is in perfect shape, and everybody is happy. But actually, it NEVER goes this way; things ALWAYS fail.

For the machine level, ask yourself these questions:

1. **Does the server have free disk space?** 
   - Use `df`.
2. **Is the server able to keep up with CPU load?** 
   - Use `w`, `top`, `ps`.
3. **Does the server have available memory?** 
   - Use `free`.
4. **Are the server disk(s) able to keep up with read/write IO?** 
   - Use `htop`.

If the answer is no to any of these questions, then that might be the reason why things are not going as expected. There are often three ways of solving the issue:

1. Free up resources (stop processes or reduce their resource consumption).
2. Increase the machine resources (adding memory, CPU, disk space…).
3. Distribute the resource usage to other machines.

### Network Issue
For network-level issues, ask yourself these questions:

1. **Does the server have the expected network interfaces and IPs up and running?** 
   - Use `ifconfig`.
2. **Does the server listen on the sockets that it is supposed to?** 
   - Use `netstat` (`netstat -lpd` or `netstat -lpn`).
3. **Can you connect from the location you want to connect from, to the socket you want to connect to?** 
   - Use `telnet` to the IP + PORT (e.g., `telnet 8.8.8.8 80`).
4. **Does the server have the correct firewall rules?** 
   - Use `iptables`, `ufw`:
     - `iptables -L`
     - `sudo ufw status`

### Process Issue
If a piece of software isn’t behaving as expected, it can obviously be due to the above reasons. However, there is always more to look into.

1. **Is the software started?** 
   - Use `init`, `init.d`:
     - `service NAME_OF_THE_SERVICE status`
     - `/etc/init.d/NAME_OF_THE_SERVICE status`
2. **Is the software process running?** 
   - Use `pgrep`, `ps`:
     - `pgrep -lf NAME_OF_THE_PROCESS`
     - `ps auxf`
3. **Is there anything interesting in the logs?** 
   - Look for log files in `/var/log/` and `tail -f` is your friend.

### Debugging is Fun
Debugging can be frustrating, but it will definitely be part of your job. It requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck :)

