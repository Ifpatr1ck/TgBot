from typing import Final

NOTION_TOKEN: Final[str] = "secret_hAmvy4eQVJUGyyCe89LVxcOZxWdjo42GaEno1Ckwri9"  # НЕ ТРОГАТЬ

HEADERS: Final[dict] = {  # НЕ ТРОГАТЬ
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

PYTHON_LESSON = {
    "ПИН-221": ["26ab0ac4c46c41f2a1bb943f6d6af36a", "80d6f42fbf0048ac950084e5ddbfe56c"]
}

OOP_LESSON = {
    "ПИН-221": "",
    "ПИН-222": ""
}
