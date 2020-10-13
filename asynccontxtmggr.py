if sys.version_info >= (3, 7):
    from contextlib import asynccontextmanager
else:
    from photons_app.polyfill import asynccontextmanager

    
def ensure_aexit(instance):
    """
    Used to make sure a manual async context manager calls ``__aexit__`` if
    ``__aenter__`` fails.
    Turns out if ``__aenter__`` raises an exception, then ``__aexit__`` doesn't
    get called, which is not how I thought that worked for a lot of context
    managers.
    Usage is as follows:
    .. code-block:: python
        from photons_app import helpers as hp
        class MyCM:
            async def __aenter__(self):
                async with hp.ensure_aexit(self):
                    return await self.start()
            async def start(self):
                ...
            async def __aexit__(self, exc_typ, exc, tb):
                await self.finish(exc_typ, exc, tb)
            async def finish(exc_type=None, exc=None, tb=None):
                ...
    """

    @asynccontextmanager
    async def ensure_aexit_cm():
        try:
            yield
        finally:
            # aexit doesn't run if aenter raises an exception
            exc_info = sys.exc_info()
            if exc_info[1] is not None:
                await instance.__aexit__(*exc_info)
                raise

    return ensure_aexit_cm()
