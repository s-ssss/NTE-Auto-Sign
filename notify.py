import os, requests
def push(title, content):
    key = os.getenv("SCKEY")
    if not key: return
    try:
        requests.post(f"https://sctapi.ftqq.com/{key}.send", data={"title": title, "desp": content}, timeout=10)
    except: pass
