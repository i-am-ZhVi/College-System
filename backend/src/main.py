import asyncio

from queries.orm import update_tables


if __name__ == "__main__":
    asyncio.run(update_tables())
