from app.library.helpers import readcsv
from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..library.helpers import *

router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@router.get('/lines', response_class=HTMLResponse)
def get_accordion(request: Request):
    episodes = readcsv()

    return templates.TemplateResponse('lines.html', context={'request': request, 'episodes': episodes})


@router.post('/lines', response_class=HTMLResponse)
def post_accordion(request: Request, episode: str = Form(...)):
    episodes = readcsv()
    coords = episode.split(' ')
    lines = get_lines(coords[0], coords[1])

    return templates.TemplateResponse('lines.html', context={'request': request, 'episodes': episodes, 'season': coords[0], 'episode': coords[1], 'lines': lines})