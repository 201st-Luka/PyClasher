# Setting up a Client

The [Client][client_ref]
is the heard of this package. It allows to make the requests.

## The client

The [Client][client_ref] uses API tokens that you can obtain from the official
[ClashOfClans developer portal](https://developer.clashofclans.com/#/). Those tokens serve as a verification to 
the ClashOfClans API. It is sufficient to create an account and create one or
multiple tokens. 

## Setting up

### With tokens

To set up a client, you need to import the [Client][client_ref] from 
`pyclasher.client` and adding the tokens to it:

```python
import asyncio

from pyclasher.client import Client


my_tokens = [
    "enter your first token here",
    "enter the other tokens here separated as strings in a list"
]

my_client = Client(tokens=my_tokens)

async def main():
    # starting the client
    await my_client.start()

    # doing requests here
    ...

    # stopping the client
    await my_client.close()

asyncio.run(main())
```

!!! note
    It is recommended to use environment variables for the tokens. So you can 
    make sure that the tokens are never leaked on the Internet or on GitHub, ...

### With ClashOfClans developer account

It is also possible to set up a client using the login data from 
https://developer.clashofclans.com/#/login.

```python
import asyncio

from pyclasher.client import Client


my_email = "email@example.com"
my_password = "examplePassword1234"

async def login():
    return await Client.from_login(
        my_email, my_password,
        login_count=1   # this parameter is used to log in multiple times to the 
                        # ClashOfClans developer portal and create multiple tokens
    )

async def main():
    my_client = await login()
    
    # starting the client
    await my_client.start()

    # requests
    ...

    # stopping the client
    await my_client.close()
```

!!! warning
    This is an alternative method to get tokens. Those tokens are temporarily 
    and expire after one hour. It is intended for testing purpose only.
    An implementation to renew the tokens after one hour will not ever happen.
    Use [tokens](#with-tokens) for production purpose.



<!---links--->
[client_ref]: ../API%20Reference/client/client.md#pyclasher.client.client.Client

