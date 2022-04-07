import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession('http://127.0.0.1:8080') as session:
    #     async with session.post('/advertisement/post',
    #                             json={'text': 'tl;dr',
    #                                   'head': 'head',
    #                                   'owner': 'random_user',
    #                                   'date': '2022-01-02'}) as resp:
    #         print(resp.status)
    #         print(await resp.text())
    #     async with session.patch('/advertisement/patch',
    #                             json={'id': 3,
    #                                   'text': 'new text',
    #                                   'head': 'new head',
    #                                   'owner': 'new owner',
    #                                   'date': 'new date'}) as resp:
    #         print(resp.status)
    #         print(await resp.text())
    #     async with session.get('/advertisement/get', json={'id': 1}) as resp:
    #         print(resp.status)
    #         print(await resp.text())
    #     async with session.delete('/advertisement/delete', json={'id': 2}) as resp:
    #         print(resp.status)
    #         print(await resp.text())


asyncio.run(main())
