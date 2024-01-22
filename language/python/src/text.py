import re
import textwrap
import binascii


def is_engnum(text: str) -> bool:
    return bool(re.match("^[a-zA-Z0-9]*$", text))


def shorten_text(text: str, width: int = 15) -> str:
    return textwrap.shorten(text, width=width)


def wrap_text(text: str, width: int = 70) -> str:
    return textwrap.fill(text, width=width)


def hexpack(text: str|bytes, locale="ko_KR") -> bytes|None:
    if isinstance(text, str) & (locale.lower() == "ko_kr"):
        return binascii.hexlify(text.encode("utf-8"))
    elif isinstance(text, str) & (locale.lower() == "en_us"):
        return binascii.hexlify(text)
    elif isinstance(text, bytes):   # bytes only accept ASCII characters
        return text.hex()
    return None


def unhexpack(text: str|bytes, locale="ko_KR") -> str|None:
    if isinstance(text, str):
        return bytes.fromhex(text)
    elif isinstance(text, bytes):
        text = binascii.unhexlify(text)
        _codec = "utf-8"
        if locale.lower() == "ko_kr":
            try:
                text = text.decode(_codec)
            except UnicodeDecodeError:
                text = text.decode("euc-kr")
            finally:
                return text
        elif locale.lower() == "en_us":
            return text.decode(_codec)

    return None


def secure_social_number(text: str, locale="ko_KR", is_strict=True) -> str:
    if locale == "ko_KR":
        if is_strict:
            return re.sub(r"\d{6}-\d{7}", "XXXXXX-XXXXXXX", text)
        else:
            pat = re.compile("(\d{6})[-]\d{7}")
            return pat.sub("\g<1>-*******", text)
    elif locale == "en_US":
        if is_strict:
            return re.sub(r"\d{3}-\d{2}-\d{4}", "XXX-XX-XXXX", text)
        else:
            pat = re.compile("(\d{3})[-]\d{2}[-]\d{4}")
            return pat.sub("\g<1>-**-****", text)
    else:
        raise ValueError(f"Unsupported locale: {locale}")
