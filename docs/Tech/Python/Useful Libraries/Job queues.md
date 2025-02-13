## Discussion

https://www.fullstackpython.com/task-queues.html (old)

## Celery

We're currently using Celery, but it comes with complexity that we'd like to get rid of:

- https://medium.com/squad-engineering/celery-in-production-three-more-years-of-fixing-bugs-2ee462cef39f
- https://medium.com/squad-engineering/two-years-with-celery-in-production-bug-fix-edition-22238669601d

## Alternatives

- RQ
- ARQ (async)
- https://github.com/tobymao/saq Inspired by ARQ, but better (?)
- Huey
- Dramatiq
- MRQ <https://github.com/pricingassistant/mrq> (unmaintained)
	- https://blog.ippon.fr/2020/04/06/ne-laissez-plus-le-serpent-se-mordre-la-queue-en-choisissant-mrq/
- Wakaq https://github.com/wakatime/wakaq "Background task queue for Python backed by Redis, a super minimal Celery"
- https://github.com/joegasewicz/pytask-io Asynchronous Tasks Library using asyncio and Redis



<!-- Keywords -->
#asyncio #redis #async
<!-- /Keywords -->
