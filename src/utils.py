import ipaddress
from pathlib import Path

def validate_ip(ip_address: str) -> bool:
    """التحقق الدقيق من صحة عنوان IP (سواء IPv4 أو IPv6) باستخدام مكتبة بايثون القياسية."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def check_file_exists(file_path: str) -> Path:
    """التحقق مما إذا كان ملف السجلات موجوداً فعلياً على الجهاز."""
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"الملف غير موجود في المسار المحدد: {file_path}")
    return path