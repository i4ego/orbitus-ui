### python3 -m pip install -r req.txt
# hosting
import fastapi
from fastapi import FastAPI, responses, requests
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
# webview
import webview
# built-in
import os
import pathlib
import threading
# internal module
import outils

DEFAULTS = {
    "host" : "localhost",
    "port" : 4549
}
WORKING_DIRECTORY = pathlib.Path(__file__).parent
FRONT_DIRECTORY = pathlib.Path(__file__).parent/"frontend"
ORBITUS_DIRECTORY = pathlib.Path(__file__).parent.parent
VERSION = (ORBITUS_DIRECTORY/".service"/"ui-version.txt").read_text()
ORBITUS_VERSION = (ORBITUS_DIRECTORY/".service"/"orbitus_version.txt").read_text()

app = FastAPI(title="orbitus ui")
app.mount("/css", StaticFiles(directory=FRONT_DIRECTORY/"css"), name="css")
app.mount("/js", StaticFiles(directory=FRONT_DIRECTORY/"js"), name="js")
app.mount("/images", StaticFiles(directory=FRONT_DIRECTORY/"images"), name="images")

app.mount("/api/files/lists", StaticFiles(directory=ORBITUS_DIRECTORY/"lists"), name="lists")
templates = Jinja2Templates(directory=FRONT_DIRECTORY/"html")

status = "Запущен"
gf = "Отключен"
ipsetf = "Отключен"
config = "general (FAKE TLS AUTO ALT3)"

@app.get("/", response_class=responses.HTMLResponse)
async def index(request: requests.Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "version" : VERSION,
            "orbitusversion" : ORBITUS_VERSION,
            "status" : status,
            "gf" : gf,
            "ipsetf" : ipsetf,
            "config" : config
        },
    )

@app.get("/api/hardware", response_class=responses.HTMLResponse)
async def index(request: requests.Request):
    hw = outils.getHardware()
    hw["version"] = VERSION
    hw["orbitus-version"] = ORBITUS_VERSION
    return responses.JSONResponse(hw)

@app.get("/api/close", response_class=responses.HTMLResponse)
async def index(request: requests.Request):
    webview.set_title("closing..")
    webview.destroy_window()
    return responses.RedirectResponse("/")

def host_worker():
    uvicorn.run(app, host=DEFAULTS["host"], port=DEFAULTS["port"])

def main() -> int:
    hw = threading.Thread(target=host_worker, daemon=True, name="orbitus server")
    hw.start()

    webview.create_window(app.title, url=f"http://{DEFAULTS['host']}:{DEFAULTS['port']}/", width=1200, height=800, min_size=(1200, 800))
    webview.start()
    return 0

if __name__ == "__main__":
    exit(main())