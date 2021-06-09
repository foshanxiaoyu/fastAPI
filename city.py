from fastapi import FastAPI
from pydantic import BaseModel
import requests
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

db =[]

class City(BaseModel):
    name:str
    timezone:str
    


app.mount("/blabla", StaticFiles(directory="blabla"), name="static")
# 创建一个templates（模板）对象，以后可以重用。
templates = Jinja2Templates(directory="blabla")
# templates = Jinja2Templates(directory="static")

# Request在路径操作中声明一个参数，该参数将返回模板。
# 使用templates您创建的渲染并返回TemplateResponse，并request在Jinja2“上下文” 中将用作键值对之一。
@app.get("/items/{id}")
# async def read_item(rst:Request,id:str):
async def read_item(res:Request,id:str):
    context = {
        'request':res,
        'id':id,
        'name':'小古怪',
        'age' : 48
    }
    # return templates.TemplateResponse("item.html", {"request": rst, "id": id})
    # return templates.TemplateResponse("index3.html",{'request':res,'name':'Xiao','age':48,'id':id})
    return templates.TemplateResponse("index3.html",context)
    
'''
http://worldtimeapi.org/api/timezone  (requests)
"Asia/Aqtau","Asia/Aqtobe","Asia/Ashgabat","Asia/Atyrau","Asia/Baghdad","Asia/Baku","Asia/Bangkok",
"Asia/Barnaul","Asia/Beirut","Asia/Bishkek","Asia/Brunei","Asia/Chita","Asia/Choibalsan",
"Asia/Colombo","Asia/Damascus","Asia/Dhaka","Asia/Dili","Asia/Dubai","Asia/Dushanbe","Asia/Famagusta",
"Asia/Gaza","Asia/Hebron","Asia/Ho_Chi_Minh","Asia/Hong_Kong","Asia/Hovd","Asia/Irkutsk","Asia/Jakarta",
"Asia/Jayapura","Asia/Jerusalem","Asia/Kabul","Asia/Kamchatka","Asia/Karachi","Asia/Kathmandu",
"Asia/Khandyga","Asia/Kolkata","Asia/Krasnoyarsk","Asia/Kuala_Lumpur","Asia/Kuching","Asia/Macau",
"Asia/Magadan","Asia/Makassar","Asia/Manila","Asia/Nicosia","Asia/Novokuznetsk","Asia/Novosibirsk",
"Asia/Omsk","Asia/Oral","Asia/Pontianak","Asia/Pyongyang","Asia/Qatar","Asia/Qostanay","Asia/Qyzylorda",
"Asia/Riyadh","Asia/Sakhalin","Asia/Samarkand","Asia/Seoul","Asia/Shanghai","Asia/Singapore",
"Asia/Srednekolymsk","Asia/Taipei","Asia/Tashkent","Asia/Tbilisi","Asia/Tehran","Asia/Thimphu",
"Asia/Tokyo","Asia/Tomsk","Asia/Ulaanbaatar","Asia/Urumqi"
'''
@app.get('/cities')
def get_cities():
    res = []
    for city in db:
        r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
        current_time = r.json()['datetime']
        res.append({'城市名称':city['name'],'所属时区':city['timezone'],'当前时间':current_time})
    return res

@app.post('/cities')
def creat_city(city:City):
    db.append(city.dict())
    return db[-1]


@app.get('/cities/{city_id}')
def get_city(city_id:int):
    return db[city_id-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id:int):
    db.pop(city_id-1)
    return db


@app.get('/')
def home():
    return {'key':'veluse'}
