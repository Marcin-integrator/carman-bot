from app.library.helpers import readcsv
from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..library.helpers import *

router = APIRouter()
templates = Jinja2Templates(directory='templates/')
conversation = []

@router.get('/chat', response_class=HTMLResponse)
def show_chat(request: Request):
    conversation.clear()
    return templates.TemplateResponse('cartmanbot.html', context={'request': request})



@router.post('/chat', response_class=HTMLResponse)
def tell_something(request: Request, user_line: str = Form(...)):
    answer = find_answer(user_line)

    two_line = (user_line, answer)
    conversation.append(two_line)

    return templates.TemplateResponse('cartmanbot.html', context={'request': request, 'conversation': conversation})