## Runtime checking

- [beartype](https://pypi.org/project/beartype/) -> Needs to modify code (`@beartype`)
- [enforce](https://github.com/RussBaz/enforce). -> Need code modification (`@runtime\_validation`) + unmaintained
- [pytypes](https://github.com/Stewori/pytypes). -> Same
- [typeen](https://github.com/k2bd/typen). -> Same
- [typeguard](https://github.com/agronholm/typeguard). -> No need for code modification, but buggy ("typeguard cannot check these packages because they are already imported")

=> And the winner is: **Typeguard**.
