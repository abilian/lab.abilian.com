#public 

Hop3 is an open-source platform aimed at enhancing cloud computing with a focus on sovereignty, security, sustainability, and inclusivity.

It is designed to facilitate access to cloud technologies for a wide range of users, including small and medium-sized enterprises (SMEs), non-profits, public services, and individual developers. By leveraging existing, robust web, cloud and open source technologies, Hop3 enables these groups to deploy and manage web applications efficiently and securely.

→ <https://github.com/abilian/hop3>

# Tasks

## General

- [ ] Change the file structure to `~hop3/apps/<app-name>/{app,env,data,etc.}`
- [ ] Central configuration file / database
- [ ] Refactor Procfile parsing (use a class). See also Honcho code.
- [ ] Add support for app.json (or similar) for additional configuration
- [ ] Plugins
- [ ] Isolation (each app gets a unique user)

## Hop client

- [ ] Make a real (smart) client
- [ ] Determine the protocol for client ↔︎ server communication
- [ ] Implement all the commands
- [ ] Add `hop check`

## Builders

### General

- [ ] Refactor code using classes

### Python

- [ ] Fix poetry support
- [ ] Support uv/rye
- [ ] Support pypenv
- [ ] Support hatch, pdm, etc.
- [ ] Tests for all supported installer / dependency managers

### Go support

- [ ] Support for go modules https://go.dev/blog/using-go-modules
- [ ] Tests for go modules

### Ruby support

- [ ] Test with a Rails app

### Testing

- [ ] Add support for smoke tests (in the Procfile)

## Runtime

- [ ] Refactor code using classes
- [ ] Review / improve CLI DX
- [ ] Manage external services (databases, etc.)
- [ ] Support for Heroku, Render, Compose, Fly... config files, 

## Hosting

- [ ] Architecture for a hosting service based on Hop
