import models

from database import Base, engine, Session
from models.messanger import *
from models.person import *
from models.system import *





async def recreates_tables():
    engine.echo = False

    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

    engine.echo = True

async def creates_tables():
    engine.echo = False

    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

    engine.echo = True



# Mini Tests

async def new_message(id_person, id_chat, message):
    async with Session() as session:
        async with session.begin():
            message = Message(sender_id=id_person, chat_id=id_chat, message=message)
            session.add(message)


async def new_login(name, password):
    async with Session() as session:
        async with session.begin():
            login = Login(login=name, password=password)
            session.add(login)


async def new_person(login_id, surname, name, teacher=False):
    async with Session() as session:
        async with session.begin():
            if teacher:
                person = Person(login_id=login_id, surname=surname, name=name, role=Role.teacher)
            else:
                person = Person(login_id=login_id, surname=surname, name=name)

            session.add(person)




async def new_chat(id_creator, name, desc):
    async with Session() as session:
        async with session.begin():
            chat = Chat(creator_id=id_creator, name=name, description=desc)
            session.add(chat)

async def new_channel(id_creator, name, desc):
    async with Session() as session:
        async with session.begin():
            channel = Channel(creator_id=id_creator, name=name, description=desc)
            session.add(channel)


async def new_file(name, type):
    async with Session() as session:
        async with session.begin():
            file = File(name=name, type=type)
            session.add(file)


async def new_subscriber(person_id, chat_id):
    async with Session() as session:
        async with session.begin():
            subs = Subscriber(person_id=person_id, chat_id=chat_id)
            session.add(subs)


async def new_post(name):
    async with Session() as session:
        async with session.begin():
            post = Post(name=name)
            session.add(post)


async def new_teacher(id_post, id_person):
    async with Session() as session:
        async with session.begin():
            teacher = Teacher(person_id=id_person, post_id=id_post)
            session.add(teacher)


async def new_item(name, post_id):
    async with Session() as session:
        async with session.begin():
            item = Item(name=name, post_id=post_id)
            session.add(item)


async def new_grade(teacher_id, student_id, item_id, eval, couple_num):
    async with Session() as session:
        async with session.begin():
            grade = Grade(teacher_id=teacher_id, student_id=student_id, item_id=item_id, evaluation=eval, number_couple=couple_num)
            session.add(grade)


async def new_group(name):
    async with Session() as session:
        async with session.begin():
            group = Group(name=name)
            session.add(group)


async def add_teacher_to_group(teacher_id, group_id):
    async with Session() as session:
        async with session.begin():
            teacher_group = Teacher_to_Group(person_id=teacher_id, group_id=group_id)
            session.add(teacher_group)


async def add_student_to_group(student_id, group_id):
    async with Session() as session:
        async with session.begin():
            student_group = Student_to_Group(person_id=student_id, group_id=group_id)
            session.add(student_group)


async def add_item_to_group(item_id, group_id):
    async with Session() as session:
        async with session.begin():
            item_group = Item_for_Group(item_id=item_id, group_id=group_id)
            session.add(item_group)
