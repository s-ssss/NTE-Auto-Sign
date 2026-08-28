import os, sys, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notify import push
exit_code = 0
try:
    # 原逻辑直接调用 nte.py 的主函数或执行
    import nte
    nte.main() if hasattr(nte, 'main') else os.system("python nte.py")
except Exception:
    traceback.print_exc()
    exit_code = 1
finally:
    status = "成功 ✅" if exit_code == 0 else f"失败 ❌（退出码 {exit_code}）"
    push("NTE自动签到（GitHub）", f"状态：{status}")
sys.exit(exit_code)
