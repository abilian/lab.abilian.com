APIs expose business logic and data to external systems, so it's important to make the communication between systems secure and efficient, but also to improve user experience and system reliability.

## References

- \[Designing APIs for humans Series (at Stripe)\]https://dev.to/paulasjes/series/19794

## Details

Here are some guidelines and best practices that we use at Abilian for designing robust APIs that are secure, efficient, and easy to use.

## API Key Generation

API keys are essential for tracking and controlling how the API is being used by different clients, and for ensuring that the access is secure. The process typically involves:

- **Unique Application IDs**: Assign a unique application ID for each client to uniquely identify different applications accessing your API.
- **Key Pairs for Different Access Levels**: Generate distinct pairs of public (access key) and private (secret key) keys for different authorization levels. For example:
  - A read-only key pair that restricts the client to fetching data without making changes.
  - A read-write key pair that allows clients to both fetch and modify data.

This differentiation ensures that clients have access only to the functionalities that their application requires.

## Signature Generation

To maintain the integrity and security of API requests, signatures are used. These signatures help verify that requests are coming from an authenticated source and have not been altered in transit.

Here's the process of generating a signature:

- **Collecting Parameters**: Gather all the necessary parameters required to make an API call.
- **Creating a Signing String**: Concatenate the collected parameters into a string format that will be signed.
- **Hashing the String**: Utilize a cryptographic hash function, such as HMAC (Hash-based Message Authentication Code) combined with SHA-256. The string is hashed using the secret key, which verifies the authenticity and integrity of the request.

## Sending Requests

When constructing requests to send to an API, one should include specific elements within the HTTP request parameters to ensure security and proper handling of the request:

- **Authentication Credentials**: Include API keys or other credentials to authenticate the request.
- **Timestamp**: Add a timestamp to each request to prevent replay attacks where old requests are resubmitted.
- **Request-Specific Data**: Incorporate necessary data for processing the request, such as user IDs, transaction details, or search queries.
- **Nonces**: Use a nonce, a unique and randomly generated string for each request, to ensure that each request is distinct and to further safeguard against replay attacks.

## Security Guidelines

Protecting APIs against common security vulnerabilities and threats is fundamental. You must adhere to established security guidelines, such as:

- **Regularly updating and rotating keys**: Ensure that keys are changed periodically to minimize the risk of unauthorized access.
- **Using secure connections**: Always use HTTPS to encrypt the data in transit.
- **Implementing rate limiting**: Prevent abuse and DoS attacks by limiting how many requests a user can make in a given period.
- **Validating and sanitizing inputs**: Protect your API from SQL injection, XSS, and other attacks by properly checking and cleaning the data being sent to your API.

## Additional tips

### Language

Naming things is notoriously difficult in computer science, and API design is no exception. Like naming variables and functions, you want API routes, fields, and types to be clear yet concise. Here are some tips to achieve that.

#### Use Simple Language

Although this seems straightforward, it often leads to extensive debates. Try to distill a concept down to its essence and use a thesaurus if necessary. For instance, differentiate clearly between terms like 'member' and 'subscriber'. A 'member' might be someone who has signed up to use your platform, while a 'subscriber' is the individual who has paid for a service. Consistency in language is key, even if you choose different terms.

#### Avoid Jargon

Every industry has its own jargon. If you expect a significant part of your users to not be familiar with it, consider using more generic terms.

For example, instead of using specialized terms like 'Electronic Program Guide (EPG)', use something more universally understood, like 'TV schedule':

```javascript
`tv_schedule.time_slot = "20:00 - 21:00";`
```

This approach ensures clarity, especially for developers who might not have expertise in your specific domain.

### Structure

#### Prefer Enums Over Booleans

Consider an API for a content management system. Initially, you might have:

```javascript
Article.published = {true, false}
```

However, if you later introduce a 'reviewed' state, using booleans can become confusing:

```javascript
Article.published = {true, false}
Article.reviewed = {true, false}
```

A more scalable approach is to use enums:

```javascript
Article.status = {"draft", "published", "reviewed"}
```

This makes the API more descriptive and easier to extend in the future.

#### Use Nested Objects for Future Extensibility

Group related fields together logically:

```javascript
author.address = {
  street: "Main Street 123",
  city: "San Francisco",
  postal_code: "12345"
};
```

This method is cleaner and allows for easier expansion, such as adding a 'country' field later, while keeping field names manageable.

### Responses

#### Return the Object Type

When an API call is made to get or mutate data, the response should clearly indicate the type of object being returned. For example:

```json
{
  "id": "art_123",
  "object": "article",
  "created": 1672217299,
  "author": "auth_123",
  "status": "published",
  ...
}
```

This clarity helps developers understand and handle the API responses correctly.

### Security

#### Use a Permission System

If you’re releasing a new feature to select users for beta testing, ensure it’s protected by a permission system tied to the API key. This prevents unauthorized access and ensures that only authorized users can use the new feature.

#### Make Your IDs Unguessable

Ensure that object IDs are not easily guessable to avoid leaking sensitive information. Use UUIDs instead of sequential IDs. For example:

```json
{
  "id": "book_3LKQhvGUcADgqoEM3bh6pslE",
  ...
}
```

### Designing APIs for Humans

If you found this useful, explore the "[APIs You Won’t Hate](https://apisyouwonthate.com/)" community for additional insights on API design.
