from asyncio import Queue


class PQueue(Queue):
    async def put(self,
                  future,
                  request_url,
                  request_method,
                  body,
                  status,
                  error):
        return await super().put(
            (future, request_url, request_method, body, status, error)
        )
