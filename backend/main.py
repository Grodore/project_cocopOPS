from fastapi import FastAPI, status
from routes import WPT, inference
from starlette.responses import RedirectResponse

app = FastAPI(title="WPT", version="1.0.0")


app.include_router(WPT.router)
app.include_router(inference.router)


@app.get(
    "/",
    tags=["startup"],
    description="API startup on documentation page.",
)
def main():
    """Redirect to the api documentation at launch."""
    return RedirectResponse(url="/docs")


@app.get(
    "/healthcheck",
    tags=["healthcheck"],
    status_code=status.HTTP_200_OK,
    response_description="ok",
    summary="resume",
)
def get_api_status() -> str:
    """Return Ok if the api is up."""
    return "ok"
