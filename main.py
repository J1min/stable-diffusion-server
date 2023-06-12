from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from os import environ

import replicate

from interface import schemas, model

app = FastAPI()
load_dotenv()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.patch("/create/image")
async def create_wordcloud(body: schemas.wordcloud):

    environ['REPLICATE_API_TOKEN'] = environ.get('REPLICATE_API_TOKEN')

    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": f'{body.content}, anime style, anime, '}
    )

    print(output)

    return {
        "message": "create image~",
        "url": output[0]
    }
