import os, sys, traceback, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notify import push
exit_code = 0
try:
    exit_code = subprocess.run([sys.executable, "qinglong.py"]).returncode
except Exception:
    traceback.print_exc()
    exit_code = 1
finally:
    status = "成功 ✅" if exit_code == 0 else f"失败 ❌（退出码 {exit_code}）"
    push("NTE自动签到（青龙）", f"状态：{status}")
sys.exit(exit_code)
