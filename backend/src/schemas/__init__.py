from pydantic_core.core_schema import field_before_validator_function
from schemas import person
from schemas import call_schedule
from schemas import site
from schemas import system
from schemas import messanger

from schemas.person import *
from schemas.call_schedule import *
from schemas.site import *
from schemas.system import *
from schemas.messanger import *

PersonRel.model_rebuild()

ChatRel.model_rebuild()
ChannelRel.model_rebuild()
MessageRel.model_rebuild()
FileRel.model_rebuild()

News_PageRel.model_rebuild()

PostRel.model_rebuild()
ItemRel.model_rebuild()
GroupRel.model_rebuild()
GradeRel.model_rebuild()
SpecialtiesRel.model_rebuild()
Substitutions_SpecialtiesRel.model_rebuild()
ProfessionsRel.model_rebuild()
Substitutions_ProfessionsRel.model_rebuild()
