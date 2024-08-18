
# postmortem: Web Application Outage Due to Database Connection Leak

## Issue Summary:
Duration: August 15, 2024, 10:00 AM - 12:30 PM (UTC)
Impact: During the outage, 60% of users experienced slow page load times, and 25% of users faced complete service unavailability. The affected services included the main web application and the API endpoints, leading to disrupted user sessions and failed API requests.
Root Cause: The root cause was a database connection leak in the application layer, leading to exhaustion of the connection pool and rendering the database unable to accept new connections.

## Timeline:
10:00 AM - Issue detected via automated monitoring alert indicating a sharp increase in response times and a high rate of 500 errors.
10:05 AM - On-call engineer initiated an investigation by checking server logs and database health.
10:15 AM - Initial assumption: High traffic spike due to a recent feature release, leading to resource exhaustion.
10:20 AM - The engineering team scaled up the application servers, assuming that resource limitation was the issue. This action temporarily reduced the error rate but did not resolve the underlying issue.
10:40 AM - Misleading path: Investigated the new feature codebase for potential memory leaks or infinite loops.
11:00 AM - Escalated to the database administration team after noticing the database connection pool was saturated.
11:20 AM - Database logs reviewed, revealing a large number of idle connections.
11:30 AM - Identified a database connection leak in the application layer, causing connections to remain open and eventually saturating the pool.
12:00 PM - Applied a hotfix to close connections properly after use.
12:30 PM - Confirmed that normal service was restored, with monitoring showing a return to expected performance levels.

### Root Cause and Resolution:
Root Cause: The application had a faulty connection management logic where database connections were not properly closed after transactions. This caused a gradual build-up of idle connections, eventually leading to the exhaustion of the connection pool. Once the pool was exhausted, the application could no longer establish new connections to the database, resulting in widespread service disruption.
Resolution: The issue was resolved by patching the application to ensure that all database connections were correctly closed after each transaction. Specifically, a missing finally block in the connection handling code was added to guarantee closure of connections regardless of whether an operation succeeded or failed.

## Corrective and Preventative Measures:
Improvement Areas:
Enhance code reviews, particularly around resource management sections, to catch such issues earlier.
Implement more granular monitoring for database connection pools to detect leaks or unusual connection patterns before they cause outages.
Increase load testing to simulate high-traffic scenarios with extensive database interactions, identifying potential weak points.
Task List:
 Patch all instances of the application with the fixed connection management logic.
 Add database connection pool monitoring with automated alerts for high usage or abnormal patterns.
 Conduct a thorough code audit focusing on resource management, including file handles, threads, and database connections.
 Implement automated tests that simulate heavy database usage and monitor connection pool behavior.
 Schedule a post-incident review meeting to discuss the incident and ensure all team members are aware of the root cause and resolution.
