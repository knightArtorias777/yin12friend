"""
## recipe菜谱
> mom planw -fld    # 计划一周菜单
> mom random        # 随机给道菜
> mom custom        # 定制化家庭用餐

"""
import typer
from typing import Optional
from typing_extensions import Annotated
app = typer.Typer()


@app.command()
def planw(order: Annotated[Optional[str], typer.Argument()] = None):

    if order is None:
        print("列出所有的计划")
    else:
        print(f"Hello {order}")
