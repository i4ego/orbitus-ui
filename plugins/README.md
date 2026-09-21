## Создание плагинов для orbitus-ui
### Ручная компиляция
Плагин составляет из себя такое содержимое:
```
<json header-ов плагина>
<код плагина на python>
```
Example-плагин
```
{
  "name": "example",
  "description": "example plugin",
  "ui-version": ">0.1",
}
print(VERSION)
@app.get("/api/example"):
    return VERSION
```
У вас будет полный доступ к orbitus-ui.py (главному файлу UI)
Данный код выполняется после строки webview.create_window(..) и у плагина будет полный доступ ко всем переменным на тот момент.
