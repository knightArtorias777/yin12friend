from typing import Optional
from typing_extensions import Annotated
import typer


# def type_example(name: str, formal: bool = False, intro: Optional[str] = None):
#     pass


"""
todo
> td onething  # 增加事件
> td ls -al    # 查看所有计划
> td done      # 标注完成
> td boss      # 广播
"""

app = typer.Typer()


@app.command()
def ls(order: Annotated[Optional[str], typer.Argument()] = None):

    if order is None:
        print("列出所有的计划")
    else:
        print(f"Hello {order}")


# 增加一个todo事件
@app.command()
def onething(order: Annotated[Optional[str], typer.Argument()] = None):
    if order is None:
        print("内容")
        print('默认时间今天')
        print('默认今天完成不会等待')
    elif order == 'done':
        print('已完成')


if __name__ == "__main__":
    ls()
