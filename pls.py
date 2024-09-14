"""
下载
> pls downfile
> pls sftp
> pls ssh
> pls curl
"""
import typer
from typing import Optional
from typing_extensions import Annotated
app = typer.Typer()


# 下载反馈 好用
@app.callback()
def download_callback():
    print("下载文件中...")


@app.command()
def downfile(order: Annotated[Optional[str], typer.Argument()] = None):

    if order is None:
        print("列出所有的计划")
    else:
        print(f"Hello {order}")


@app.command()
def curl(order: )
