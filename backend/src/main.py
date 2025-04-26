import asyncio

from queries.orm import *


async def main():
    await recreates_tables()
    await creates_tables()


    # Mini Test

    await new_login("Nann", "12efw")

    await new_person("Nann", "Soturnov", "sota")
    await new_person("Nann", "Notorno", "Keka", True)

    await new_post("zuza")
    await new_teacher(id_person=2, id_post=1)

    await new_chat(1, "jjj", "scaa")
    await new_chat(1, "KKk", "kshacb")

    await new_channel(2, "lll", "ssssq")

    await new_subscriber(1, 1)

    await new_message(1, 1, "hello")
    await new_message(1, 1, "ey")
    await new_message(1, 2, "hey")
    await new_message(2, 1, "hi")

    await new_file(2, "/sda/sa")


    await new_item("math", 1)

    await new_grade(2, 1, 1, 4, 2)

    await new_group("222s")

    await add_teacher_to_group(2, 1)

    await add_student_to_group(1, 1)

    await add_item_to_group(1, 1)





if __name__ == "__main__":
    asyncio.run(main())
