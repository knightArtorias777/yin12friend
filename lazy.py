"""
lazyfriend Zerotier
> lazy connect
> lazy status
"""
import typer
from typing import Optional, Annotated

app = typer.Typer()


@app.command()
def connect(order: Annotated[Optional[str], typer.Argument()] = None):

    if order is None:
        print("列出所有的计划")
    else:
        print(f"Hello {order}")
