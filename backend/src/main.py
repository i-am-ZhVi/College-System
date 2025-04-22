import asyncio

from queries.orm import update_tables


asyncio.run(update_tables())
