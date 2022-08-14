import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from pyutter.core.primitive import Style, Function, State, View, Image
from pyutter.core_routing import state_router
from pyutter.widgets.button import OutlineButton, ButtonGroupBlock
from pyutter.widgets.layout import Center, Row, Expanded, Spacer, Grid
from pyutter.widgets.material import Card, Chip, CardImage, CardFooter, CardBody
from pyutter.widgets.text import A, P, H1

card_style = Style(width='400px')


def inc(x, y):
    """
    Very strict about the type, type must be cast everytime
    because everything is treated as a string the first time round
    """
    return {'x': int(x) + 1, 'y': int(y) + 1}


def card_generator(n=8):
    for n in range(n):
        val_counter = State(name=f'x', value=0)
        click_count = State(name=f'y', value=0)

        increment = Function(func=inc, **val_counter, **click_count)
        decrement = Function(
            func=lambda x, y: {"x": int(x) - 1, "y": int(y) + 1},
            **val_counter, **click_count
        )
        yield Card(children=[
            CardImage(children=[Image(src=f'https://picsum.photos/400/200?random={n}'), ]),
            CardBody(children=[
                Row(children=[
                    Chip(['🧮: ', val_counter]),
                    Chip(['🖱️: ', click_count]),
                ]),
                P(['Press the increment/decrement buttons to change the 🧮']),
            ],
            ),
            CardFooter(children=[
                ButtonGroupBlock(children=[
                    Expanded(),
                    OutlineButton([A(child=['increment'])], action=increment),
                    OutlineButton([A(child=['decrement'])], action=decrement)
                ])

            ]),

        ], style=card_style)


root = View([
    Row(children=[
        Spacer(width=16),
        H1(child=["Simple Counters with image"],
           style=Style(
               display='flex',
               **{"align-items": 'center'}
           )
           )
    ]
    ),
    Spacer(height=24),
    Center(children=[
        Grid(children=[x for x in card_generator()]),
    ]),
    Spacer(height=24),
])

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def demo():
    return root()


app.include_router(
    state_router,
    prefix="/state",
    responses={404: {"description": "Not found here"}},
)

if __name__ == "__main__":
    uvicorn.run("interactive_app:app", reload=True, host="0.0.0.0", port=5000, log_level="info")
