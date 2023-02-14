import uvicorn
from fastapi import Form, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings
from openai import OpenAI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()
openai = OpenAI()


@app.get("/")
async def root():
    return 'It works.'


@app.post("/chat")
async def chat(prompt: str = Form(settings.prompt_default)):

    try:
        text = openai.completions(prompt)
    except Exception as e:
        return str(e)
    else:
        # 反馈文本以两个换行符打头("\n\n")，在此之前还可能存在对用户输入语句的补全文本
        i = text.find('\n\n')
        if i != -1:
            return text[i+2:]
        else:
            return text

if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
