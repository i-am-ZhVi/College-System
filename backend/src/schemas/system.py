from pydantic import BaseModel
from datetime import datetime

from models.system import Days


class PostPost(BaseModel):
    name: str

class PostGet(PostPost):
    id: int

class PostRel(PostGet):
    teachers: list["PersonGet"]
    items: list["ItemGet"]


class TeacherPost(BaseModel):
    person_id: int
    post_id: int
    mail: str | None

class TeacherGet(TeacherPost):
    pass


class ItemPost(BaseModel):
    name: str
    post_id: int

class ItemGet(ItemPost):
    id: int

class ItemRel(ItemGet):
    post: "PostGet"
    grades: list["GradeGet"]
    groups: list["GroupGet"]
    specialties: list["SpecialtiesGet"]
    substitutions_specialties: list["Substitutions_SpecialtiesGet"]
    professions_i: list["ProfessionsGet"]
    substitutions_professions: list["Substitutions_ProfessionsGet"]


class GradePost(BaseModel):
    teacher_id: int
    student_id: int
    item_id: int
    evaluation: int
    truancy: bool
    number_couple: int

class GradeGet(GradePost):
    id: int
    create_at: datetime
    update_at: datetime

class GradeRel(GradeGet):
    student: "PersonGet"
    teacher: "PersonGet"
    item: "ItemGet"


class GroupPost(BaseModel):
    name: str
    professions: bool
    denominator: bool
    start_year: datetime | None

class GroupGet(GroupPost):
    id: int

class GroupRel(GroupGet):
    teachers: list["PersonGet"]
    students: list["PersonGet"]
    items: list["ItemGet"]
    specialties: list["SpecialtiesGet"]
    substitutions_specialties: list["Substitutions_SpecialtiesGet"]
    professions_i: list["ProfessionsGet"]
    substitutions_professions: list["Substitutions_ProfessionsGet"]


class Student_to_GroupPost(BaseModel):
    person_id: int
    group_id: int
    is_elder: bool

class Student_to_GroupGet(Student_to_GroupPost):
    pass


class Teacher_to_GroupPost(BaseModel):
    person_id: int
    group_id: int
    is_master: bool

class Teacher_to_GroupGet(Teacher_to_GroupPost):
    pass


class Item_for_GroupPost(BaseModel):
    item_id: int
    group_id: int

class Item_for_GroupGet(Item_for_GroupPost):
    pass


class SpecialtiesPost(BaseModel):
    weekly_day: Days
    teacher_id: int
    group_id: int
    item_id: int
    number_couple: int
    distance: bool
    denominator: bool

class SpecialtiesGet(SpecialtiesPost):
    id: int

class SpecialtiesRel(SpecialtiesGet):
    teacher: "PersonGet"
    group: "GroupGet"
    item: "ItemGet"


class Substitutions_SpecialtiesPost(BaseModel):
    weekly_day: Days
    teacher_id: int
    group_id: int
    item_id: int
    number_couple: int
    distance: bool
    denominator: bool

class Substitutions_SpecialtiesGet(SpecialtiesPost):
    id: int

class Substitutions_SpecialtiesRel(SpecialtiesGet):
    teacher: "PersonGet"
    group: "GroupGet"
    item: "ItemGet"


class ProfessionsPost(BaseModel):
    weekly_day: Days
    teacher_id: int
    group_id: int
    item_id: int
    number_couple: int
    distance: bool
    denominator: bool

class ProfessionsGet(ProfessionsPost):
    id: int

class ProfessionsRel(ProfessionsGet):
    teacher: "PersonGet"
    group: "GroupGet"
    item: "ItemGet"


class Substitutions_ProfessionsPost(BaseModel):
    weekly_day: Days
    teacher_id: int
    group_id: int
    item_id: int
    number_couple: int
    distance: bool
    denominator: bool

class Substitutions_ProfessionsGet(Substitutions_ProfessionsPost):
    id: int

class Substitutions_ProfessionsRel(Substitutions_ProfessionsGet):
    teacher: "PersonGet"
    group: "GroupGet"
    item: "ItemGet"
