/* ========= TEMA CLARO (default) ========= */
:root{
  --bg: #f4f7ff;
  --text: #0b1220;
  --muted: #54627b;
  --line: rgba(15, 23, 42, .12);

  --panel: rgba(255,255,255,.80);
  --panel2: rgba(255,255,255,.65);
  --shadow: 0 14px 30px rgba(15, 23, 42, .10);

  --primary: #2563eb;
  --danger:  #ef4444;
  --ok:      #16a34a;

  --chipBg: rgba(37,99,235,.10);
  --chipBd: rgba(37,99,235,.22);
}

/* ========= TEMA OSCURO (nocturno) ========= */
[data-theme="dark"]{
  --bg:#0b1220;
  --text:#eaf0ff;
  --muted:#a9b6d6;
  --line:rgba(255,255,255,.10);

  --panel: rgba(15,23,42,.55);
  --panel2: rgba(17,28,51,.65);
  --shadow: 0 18px 40px rgba(0,0,0,.45);

  --primary:#7aa8ff;
  --danger:#ff5a6a;
  --ok:#37d67a;

  --chipBg: rgba(122,168,255,.12);
  --chipBd: rgba(122,168,255,.22);
}

*{ box-sizing:border-box; }
html,body{ height:100%; }
body{
  margin:0;
  font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
  color: var(--text);
  background:
    radial-gradient(900px 500px at 20% 0%, rgba(37,99,235,.12), transparent 60%),
    radial-gradient(900px 500px at 90% 20%, rgba(22,163,74,.10), transparent 55%),
    var(--bg);
}

.muted{ color: var(--muted); }

.shell{
  min-height:100%;
  display:grid;
  grid-template-columns: 320px 1fr;
}

.side{
  padding:18px 16px;
  border-right:1px solid var(--line);
  background: var(--panel);
  backdrop-filter: blur(10px);
}

.brand{
  display:flex;
  gap:12px;
  align-items:center;
  padding:10px 8px 14px;
}
.mark{
  width:46px;height:46px;
  border-radius:14px;
  display:grid;place-items:center;
  font-weight:900;
  color: #fff;
  background: linear-gradient(135deg, var(--primary), var(--ok));
  box-shadow: var(--shadow);
}
[data-theme="dark"] .mark{ color:#0b1220; }

.title{ font-weight:900; }
.sub{ color:var(--muted); font-size:12px; margin-top:2px; }

.panel{
  margin-top:12px;
  border:1px solid var(--line);
  border-radius:16px;
  background: var(--panel2);
  box-shadow: var(--shadow);
  padding:12px;
}

.row{
  display:flex;justify-content:space-between;align-items:center;
  padding:8px 2px;
  border-bottom:1px dashed rgba(127,127,127,.25);
}
[data-theme="dark"] .row{ border-bottom:1px dashed rgba(255,255,255,.10); }
.row:last-child{ border-bottom:none; }

.k{ color:var(--muted); font-size:12px; }
.v{ font-size:12px; display:flex; align-items:center; gap:8px; }

.dot{
  width:10px;height:10px;border-radius:50%;
  background: rgba(127,127,127,.35);
  box-shadow:0 0 0 4px rgba(127,127,127,.12);
}
.dot.ok{ background:var(--ok); box-shadow:0 0 0 4px rgba(22,163,74,.18); }
.dot.bad{ background:var(--danger); box-shadow:0 0 0 4px rgba(239,68,68,.16); }

.actions{ display:grid; gap:10px; margin-top:10px; }
.toggleRow{ display:flex; justify-content:space-between; align-items:center; margin-top:12px; }

.miniText{
  margin-top:6px;
  font-size:12px;
  color: var(--muted);
}

.logout{
  display:block;
  margin-top:14px;
  text-decoration:none;
  color:var(--muted);
  font-weight:800;
  padding:10px 10px;
  border-radius:12px;
}
.logout:hover{ background: rgba(127,127,127,.10); }

.main{ padding:18px 18px 26px; }

.top{
  display:flex; justify-content:space-between; align-items:center;
  border:1px solid var(--line);
  border-radius:16px;
  background: var(--panel);
  backdrop-filter: blur(10px);
  box-shadow: var(--shadow);
  padding:14px 16px;
}
.top h1{ margin:0; font-size:18px; font-weight:900; }

.grid{
  margin-top:14px;
  display:grid;
  grid-template-columns: repeat(2, 1fr);
  gap:14px;
}

.card{
  border:1px solid var(--line);
  border-radius:16px;
  background: var(--panel2);
  box-shadow: var(--shadow);
  padding:14px;
}

.cardHead{
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin-bottom:10px;
}
.tag{
  font-weight:900;
  padding:6px 10px;
  border-radius:999px;
  background: var(--chipBg);
  border:1px solid var(--chipBd);
  color: var(--primary);
}

.card input[type="range"]{
  width:100%;
  accent-color: var(--primary);
}

.bottom{
  margin-top:12px;
  display:grid;
  grid-template-columns: 90px 1fr;
  gap:10px;
  align-items:center;
}

.num{
  width:100%;
  padding:10px 12px;
  border-radius:12px;
  border:1px solid var(--line);
  background: rgba(255,255,255,.70);
  color:var(--text);
}
[data-theme="dark"] .num{
  background: rgba(0,0,0,.18);
}

.bar{
  height:10px;
  border-radius:999px;
  background: rgba(37,99,235,.10);
  border:1px solid var(--line);
  overflow:hidden;
}
.bar > span{
  display:block;
  height:100%;
  width:0%;
  background: linear-gradient(90deg, var(--primary), var(--ok));
}

/* Switch */
.switch{ position:relative; display:inline-block; width:54px; height:28px; }
.switch input{ display:none; }
.switch .track{
  position:absolute; inset:0;
  border-radius:999px;
  background: rgba(148,163,184,.25);
  border:1px solid var(--line);
  transition:.18s ease;
}
.switch .track:before{
  content:"";
  position:absolute;
  width:22px;height:22px;
  left:3px; top:2px;
  background:#fff;
  border-radius:999px;
  box-shadow: 0 6px 14px rgba(0,0,0,.22);
  transition:.18s ease;
}
.switch input:checked + .track{
  background: rgba(37,99,235,.25);
  border-color: rgba(37,99,235,.25);
}
[data-theme="dark"] .switch input:checked + .track{
  background: rgba(122,168,255,.30);
  border-color: rgba(122,168,255,.22);
}
.switch input:checked + .track:before{
  transform: translateX(26px);
}

/* Buttons */
.btn{
  border:1px solid var(--line);
  background: rgba(255,255,255,.70);
  color:var(--text);
  padding:10px 12px;
  border-radius:12px;
  cursor:pointer;
  font-weight:800;
}
[data-theme="dark"] .btn{ background: rgba(255,255,255,.06); }
.btn:hover{ filter: brightness(1.02); }
.btn:active{ transform: translateY(1px); }

.btn.primary{
  border-color: rgba(37,99,235,.30);
  background: rgba(37,99,235,.12);
  color: var(--primary);
}
[data-theme="dark"] .btn.primary{
  border-color: rgba(122,168,255,.30);
  background: rgba(122,168,255,.12);
}

.btn.danger{
  border-color: rgba(239,68,68,.30);
  background: rgba(239,68,68,.10);
  color: var(--danger);
}
[data-theme="dark"] .btn.danger{
  border-color: rgba(255,90,106,.30);
  background: rgba(255,90,106,.10);
}

/* Console */
.console{
  margin-top:14px;
  border:1px solid var(--line);
  border-radius:16px;
  background: var(--panel);
  backdrop-filter: blur(10px);
  box-shadow: var(--shadow);
  overflow:hidden;
}
.consoleHead{
  padding:10px 14px;
  border-bottom:1px solid var(--line);
  display:flex; justify-content:space-between; align-items:center;
}
.console pre{
  margin:0;
  padding:12px 14px;
  background: #0b1220;
  color:#dbeafe;
  min-height:140px;
  white-space:pre-wrap;
  font-size:12px;
}

/* Login */
.auth{
  min-height:100%;
  display:grid;
  place-items:center;
  padding:18px;
}
.auth-card{
  width:100%;
  max-width:420px;
  border:1px solid var(--line);
  border-radius:16px;
  background: var(--panel);
  backdrop-filter: blur(10px);
  box-shadow: var(--shadow);
  padding:16px;
}
.auth-title{ font-size:18px; font-weight:900; }
.auth-sub{ margin-top:6px; color:var(--muted); font-size:12px; }
.auth-form{ margin-top:12px; display:grid; gap:10px; }
.auth-form label{ color:var(--muted); font-size:12px; }
.auth-form input{
  padding:10px 12px;
  border-radius:12px;
  border:1px solid var(--line);
  background: rgba(255,255,255,.70);
  color:var(--text);
}
[data-theme="dark"] .auth-form input{
  background: rgba(0,0,0,.18);
}
.auth-error{
  margin-top:10px;
  padding:10px 12px;
  border-radius:12px;
  border:1px solid rgba(239,68,68,.30);
  background: rgba(239,68,68,.10);
  color:#b91c1c;
}
[data-theme="dark"] .auth-error{ color:#ffd0d6; }

/* Scenes */
.scenes{
  margin-top:14px;
  padding-top:12px;
  border-top:1px dashed rgba(127,127,127,.25);
}
[data-theme="dark"] .scenes{ border-top:1px dashed rgba(255,255,255,.12); }

.scenesTitle{ font-weight:900; margin-bottom:10px; }

.sceneInput{
  width:100%;
  padding:10px 12px;
  border-radius:12px;
  border:1px solid var(--line);
  background: rgba(255,255,255,.70);
  color:var(--text);
  margin-bottom:10px;
}
[data-theme="dark"] .sceneInput{ background: rgba(0,0,0,.18); }

.sceneList{ margin-top:10px; display:grid; gap:10px; }
.sceneRow{
  display:grid;
  grid-template-columns: 1fr auto auto;
  gap:8px;
  align-items:center;
  padding:10px;
  border:1px solid var(--line);
  border-radius:12px;
  background: rgba(127,127,127,.06);
}
.sceneLabel{
  font-weight:900;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.sceneBtn{ padding:8px 10px; font-size:12px; }
.sceneEmpty{ color:var(--muted); font-size:12px; padding:8px 2px; }

@media (max-width: 980px){
  .shell{ grid-template-columns: 1fr; }
  .side{ border-right:none; border-bottom:1px solid var(--line); }
  .grid{ grid-template-columns: 1fr; }
}
