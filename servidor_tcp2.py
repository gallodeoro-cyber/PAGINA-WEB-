import os
import socketserver
import threading
import time
import serial

SERIAL_PORT = os.environ.get("ARDUINO_PORT", "/dev/ttyACM0")
BAUDRATE = int(os.environ.get("ARDUINO_BAUD", "9600"))

TCP_HOST = os.environ.get("TCP_HOST", "127.0.0.1")
TCP_PORT = int(os.environ.get("TCP_PORT", "5001"))

SER_TIMEOUT = 1.0


def normalize_cmd(cmd: str):
    cmd = (cmd or "").strip().upper()
    if not cmd:
        return None

    if cmd == "STATE":
        return "STATE"

    if cmd.startswith("ALL:"):
        try:
            v = int(cmd.split(":", 1)[1])
        except Exception:
            return None
        v = max(0, min(255, v))
        return f"ALL:{v}"

    if cmd.startswith("LED") and ":" in cmd:
        # LED1:128
        head, val = cmd.split(":", 1)
        if len(head) != 4:
            return None
        led = head[3]
        if led not in ("1", "2", "3", "4"):
            return None
        try:
            v = int(val)
        except Exception:
            return None
        v = max(0, min(255, v))
        return f"LED{led}:{v}"

    return None


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        srv = self.server  # type: ignore
        while True:
            line = self.rfile.readline()
            if not line:
                break

            cmd_in = line.decode(errors="ignore").strip()
            cmd = normalize_cmd(cmd_in)

            if not cmd:
                self.wfile.write(b"ERR\n")
                continue

            try:
                resp = srv.send_serial(cmd)  # type: ignore
                self.wfile.write((resp + "\n").encode())
            except Exception:
                self.wfile.write(b"ERR\n")


class SerialBridge:
    def __init__(self, port: str, baud: int):
        self.port = port
        self.baud = baud
        self.lock = threading.Lock()
        self.ser = None

    def open(self):
        self.ser = serial.Serial(self.port, self.baud, timeout=SER_TIMEOUT, write_timeout=SER_TIMEOUT)
        time.sleep(1.5)  # Arduino reset
        self.ser.reset_input_buffer()

    def send(self, cmd: str) -> str:
        if not self.ser or not self.ser.is_open:
            raise RuntimeError("Serial no abierto")

        with self.lock:
            # limpia basura previa (por READY u otros)
            self.ser.reset_input_buffer()

            self.ser.write((cmd + "\n").encode())
            self.ser.flush()

            line = self.ser.readline().decode(errors="ignore").strip()
            return line if line else "ERR"


def main():
    bridge = SerialBridge(SERIAL_PORT, BAUDRATE)
    bridge.open()

    server = ThreadingTCPServer((TCP_HOST, TCP_PORT), Handler)
    server.send_serial = bridge.send  # type: ignore

    print(f"TCP listo en {TCP_HOST}:{TCP_PORT} | Serial: {SERIAL_PORT} @ {BAUDRATE}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        if bridge.ser and bridge.ser.is_open:
            bridge.ser.close()


if __name__ == "__main__":
    main()
