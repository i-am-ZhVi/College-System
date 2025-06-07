from pydantic import BaseModel

class News_PagePost(BaseModel):
    message: str

class News_PageGet(News_PagePost):
    id: int

class News_PageRel(News_PageGet):
    files: list["FileGet"]


class File_to_Main_Page(BaseModel):
    news_id: int
    file_id: int
