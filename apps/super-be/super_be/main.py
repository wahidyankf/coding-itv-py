from fastapi import FastAPI

app = FastAPI(title="super-be")


@app.get("/health")
def health() -> dict[str, str]:
    # Load balancers and uptime checks call this, so keep it free of I/O.
    return {"status": "ok"}
