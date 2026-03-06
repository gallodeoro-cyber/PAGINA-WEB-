import os
import json
import socket
from flask import Flask, jsonify, render_template, request, redirect, session, url_for

app = Flask(__name__, template_folder="templates2", static_folder="static2", static_url_path="/static")
app.secret_key = os.environ.get("FLASK_SECRET", "cambia_esta_clave")

TCP_HOST = os.environ.get("TCP_HOST", "127.0.0.1")
TCP_PORT = int(os.environ.get("TCP_PORT", "5001"))

LOGIN_USER = os.environ.get("LOGIN_USER", "admin")
LOGIN_PASS = os.environ.get("LOGIN_PASS", "1234")

SCENES_PATH = os.path.join(os.path.dirname(__file__), "scenes.json")


def tcp_send(cmd: str, timeout: float = 1.0) -> str:
    cmd = cmd.strip()
    with socket.create_connection((TCP_HOST, TCP_PORT), timeout=timeout) as s:
        s.sendall((cmd + "\n").encode())
        s.settimeout(timeout)
        data = b""
        while not data.endswith(b"\n"):
            chunk = s.recv(256)
            if not chunk:
                break
            data += chunk
        return data.decode(errors="ignore").strip()


def is_logged_in() -> bool:
    return session.get("logged_in") is True


def require_login():
    if not is_logged_in():
        return jsonify({"ok": False, "error": "No autorizado"}), 401
    return None


def parse_state(resp: str):
    # STATE:v1,v2,v3,v4
    if not resp.startswith("STATE:"):
        return None
    try:
        tail = resp.split(":", 1)[1].strip()
        parts = [int(x.strip()) for x in tail.split(",")]
        if len(parts) != 4:
            return None
        parts = [max(0, min(255, v)) for v in parts]
        return {1: parts[0], 2: parts[1], 3: parts[2], 4: parts[3]}
    except Exception:
        return None


def load_scenes():
    if not os.path.exists(SCENES_PATH):
        data = {"scenes": {}}
        save_scenes(data)
        return data
    try:
        with open(SCENES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        data = {"scenes": {}}
        save_scenes(data)
        return data


def save_scenes(data):
    with open(SCENES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    user = (request.form.get("user") or "").strip()
    passwd = request.form.get("pass") or ""

    if user == LOGIN_USER and passwd == LOGIN_PASS:
        session["logged_in"] = True
        return redirect(url_for("index"))

    return render_template("login.html", error="Usuario o contraseña incorrectos."), 401


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def index():
    if not is_logged_in():
        return redirect(url_for("login"))
    return render_template("index.html")


@app.get("/api/health")
def api_health():
    r = require_login()
    if r:
        return r
    try:
        with socket.create_connection((TCP_HOST, TCP_PORT), timeout=0.5):
            pass
        return jsonify({"ok": True, "tcp": True})
    except Exception as e:
        return jsonify({"ok": False, "tcp": False, "error": str(e)}), 200


@app.get("/api/state")
def api_state():
    r = require_login()
    if r:
        return r
    try:
        resp = tcp_send("STATE")
        st = parse_state(resp)
        if st is None:
            return jsonify({"ok": False, "resp": resp}), 200
        return jsonify({"ok": True, "state": st})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


@app.post("/set_led")
def set_led():
    r = require_login()
    if r:
        return r

    data = request.get_json(silent=True) or {}
    try:
        led = int(data.get("led"))
        value = int(data.get("value"))
    except Exception:
        return jsonify({"ok": False, "error": "JSON inválido: {led:1-4, value:0-255}"}), 400

    if led not in (1, 2, 3, 4):
        return jsonify({"ok": False, "error": "led debe ser 1..4"}), 400
    value = max(0, min(255, value))

    cmd = f"LED{led}:{value}"
    try:
        resp = tcp_send(cmd)
        return jsonify({"ok": True, "cmd": cmd, "resp": resp})
    except Exception as e:
        return jsonify({"ok": False, "cmd": cmd, "error": str(e)}), 500


@app.post("/api/all")
def api_all():
    r = require_login()
    if r:
        return r

    data = request.get_json(silent=True) or {}
    try:
        value = int(data.get("value"))
    except Exception:
        return jsonify({"ok": False, "error": "JSON inválido: {value:0-255}"}), 400

    value = max(0, min(255, value))
    cmd = f"ALL:{value}"
    try:
        resp = tcp_send(cmd)
        return jsonify({"ok": True, "cmd": cmd, "resp": resp})
    except Exception as e:
        return jsonify({"ok": False, "cmd": cmd, "error": str(e)}), 500


# ---------- Escenas / Configuraciones ----------
@app.get("/api/scenes")
def api_scenes_list():
    r = require_login()
    if r:
        return r
    db = load_scenes()
    scenes = list(db.get("scenes", {}).keys())
    return jsonify({"ok": True, "scenes": scenes})


@app.post("/api/scenes/save")
def api_scenes_save():
    r = require_login()
    if r:
        return r

    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    state = data.get("state")

    if not name:
        return jsonify({"ok": False, "error": "Falta name"}), 400
    if not isinstance(state, dict):
        return jsonify({"ok": False, "error": "Falta state"}), 400

    cleaned = {}
    for k in ("1", "2", "3", "4"):
        try:
            v = int(state.get(k, 0))
        except Exception:
            v = 0
        v = max(0, min(255, v))
        cleaned[k] = v

    db = load_scenes()
    db.setdefault("scenes", {})[name] = cleaned
    save_scenes(db)

    return jsonify({"ok": True, "saved": name})


@app.post("/api/scenes/delete")
def api_scenes_delete():
    r = require_login()
    if r:
        return r

    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()

    db = load_scenes()
    scenes = db.get("scenes", {})
    if name not in scenes:
        return jsonify({"ok": False, "error": "No existe"}), 404

    scenes.pop(name)
    save_scenes(db)
    return jsonify({"ok": True, "deleted": name})


@app.post("/api/scenes/apply")
def api_scenes_apply():
    r = require_login()
    if r:
        return r

    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()

    db = load_scenes()
    scene = db.get("scenes", {}).get(name)
    if not scene:
        return jsonify({"ok": False, "error": "No existe"}), 404

    # Aplica LED1..4 secuencial
    results = []
    ok_all = True
    for led in (1, 2, 3, 4):
        value = int(scene.get(str(led), 0))
        value = max(0, min(255, value))
        cmd = f"LED{led}:{value}"
        try:
            resp = tcp_send(cmd)
            results.append({"led": led, "ok": True, "cmd": cmd, "resp": resp})
        except Exception as e:
            ok_all = False
            results.append({"led": led, "ok": False, "cmd": cmd, "error": str(e)})

    return jsonify({"ok": ok_all, "name": name, "results": results})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
