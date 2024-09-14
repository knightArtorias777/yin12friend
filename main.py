import typer
import td
import lazy
import mom
import pls

app = typer.Typer()
app.add_typer(td.app, name="td")
app.add_typer(lazy.app, name="lazy")
app.add_typer(mom.app, name="mom")
app.add_typer(pls.app, name="pls")


# @app.callback() # 下载有用
# def app_callback():
#     print("hello yin's friends!")
#     print('>')


if __name__ == "__main__":
    app()
