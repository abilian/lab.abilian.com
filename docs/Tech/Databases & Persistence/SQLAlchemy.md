## Reverse engineering

Use `sqlacodegen`.

## Tips

https://polar.sh/frankie567/posts/sqlalchemy-stop-calling-session-commit
Key takeaways:
- Use `session.commit()` only once (at the end of your request - this can even be abstracted away in a post-request callback in your web framework)
- Use `session.flush()` along the way. This might even not be necessary if `autoflush` is set to `True`

## API v1 → v2

https://matt.sh/sqlalchemy-the-async-ening

