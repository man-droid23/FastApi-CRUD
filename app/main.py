from typing import Optional
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = []


@app.get("/")
def root():
    return {"message": "hello world"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    posts_dict = post.dict()
    my_posts.append(posts_dict)
    return {"data": f"Post created successfully"}

@app.get("/posts")
def get_Allposts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    try:
        return {"data": my_posts[id-1]}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    try:
        post_dict = post.dict()
        my_posts[id-1] = post_dict
        return {"data": f"Post {id} updated successfully"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    try:
        my_posts.pop(id-1)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

