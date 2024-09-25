
## Libraries

- [[Loguru]]

## References

https://betterstack.com/community/guides/logging/best-python-logging-libraries/
https://ntietz.com/blog/the-only-two-log-levels-you-need-are-info-and-error/


## Recommendations (from blog posts above)

Most applications, particularly web applications, only need two log levels: **INFO** and **ERROR**. The traditional approach to logging with multiple levels (such as DEBUG, WARNING, TRACE) is often not practical or necessary. The focus should be on whether a log entry should alert someone (ERROR) or provide context and information (INFO). Additional details, like WARNING or TRACE, often either overlap with INFO for context or escalate to ERROR if they require immediate attention.

#### Actionable Advice with Python and Loguru

1. **Simplify Your Logging Strategy**
   - Reduce complexity in your logging by limiting to INFO and ERROR.
   - Use INFO for detailed application behavior and ERROR for situations that require immediate attention.

2. **Leverage Structured Logging**
   - Use structured logging to enhance the usability and filterability of logs, making them more readable and machine-processable (e.g., JSON format).

3. **Include Contextual Information**
   - Always log with contextual information such as request IDs, timestamps, related IDs, flags, and source modules/functions to make debugging easier.

4. **Avoid Temporary Logging**
   - Do not add and then remove logs just to solve a specific issue; incorporate logs that provide ongoing insights and are useful for debugging related future issues.

#### Python Example Using Loguru

Loguru is a Python library that simplifies logging with automatic file rotation, structured logging, and concise syntax. Here's how you can implement the recommended practices:

```python
from loguru import logger

# Configure Loguru to output JSON for easier parsing and automated processing
logger.add("application.log", format="{time} {level} {message}", level="INFO", serialize=True)

# Example of logging an INFO level message
def handle_request(request):
    logger.info("Handling request", extra={"request_id": request.id, "user_id": request.user_id})
    # Request handling logic...
    try:
        # Potentially problematic code
        result = process_request(request)
        logger.info("Request processed successfully", extra={"request_id": request.id})
    except Exception as e:
        # Log an ERROR with all relevant details
        logger.error("Error processing request", extra={"request_id": request.id, "error": str(e)})
        raise

def process_request(request):
    # Simulated request processing
    if request.data == "error":
        raise ValueError("Invalid data provided")
    return "Success"

# Mock request object
class MockRequest:
    def __init__(self, id, user_id, data):
        self.id = id
        self.user_id = user_id
        self.data = data

# Usage example
request = MockRequest(id="123", user_id="abc", data="some_data")
handle_request(request)
```
