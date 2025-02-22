from functools import reduce
from typing import List
from pydantic import BaseModel, Field

def compose(*fns):
    """
        Compose any number of functions with variable number of arguments
        functions are applied from left to right
    """
    def composed(*args):
        return reduce(
            lambda acc, fn: fn(
                    *(acc if isinstance(acc, tuple) else (acc,))
                ),
            fns,
            args
        )
    return composed


# INFO: start of project funcitons

# TODO: validate response schema
class RespSchema(BaseModel):
    """ Crossword to learn from """
    questions: List[str] = Field(..., description="questions for crossword puzzle.")
    # hints: List[conlist(str, min_items=3, max_items=3)] = Field(
    #     ...,
    #     description="hints for each question, each containing exactly 3 strings."
    # )
    answers: List[str] = Field(..., description="solutions for the puzzle questions.")
