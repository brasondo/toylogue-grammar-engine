from grammar_engine import generate_line

scene = [
    {"event": "picked_up", "role": "hero"},
    {"event": "smile_detected", "role": "goofball"},
    {"event": "hugged", "role": "mentor"},
    {"event": "picked_up", "role": "villain"},
]

for s in scene:
    line = generate_line(role=s["role"], context=s["event"])
    print(f"[{s['event']}] {line}")