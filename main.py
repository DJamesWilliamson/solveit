
'''
Notes extracted for context
FastHTML is a python library which brings together Starlette, Uvicorn, HTMX, and fastcore&#39;s `FT` "FastTags"
into a library for creating server-rendered hypermedia applications. The `FastHTML` class itself
inherits from `Starlette`, and adds decorator-based routing with many additions, Beforeware,
automatic `FT` to HTML rendering, and much more.'>Things to remember when writing FastHTML apps:

- Although parts of its API are inspired by FastAPI, it is *not* compatible with FastAPI syntax and is not targeted at creating API services
- FastHTML includes support for Pico CSS and the fastlite sqlite library, although using both are optional; sqlalchemy can be used directly or via the fastsql library, and any CSS framework can be used. Support for the Surreal and css-scope-inline libraries are also included, but both are optional
- FastHTML is compatible with JS-native web components and any vanilla JS library, but not with React, Vue, or Svelte
- Use `serve()` for running uvicorn (`if __name__ == "__main__"` is not needed since it's automatic)
- When a title is needed with a response, use `Titled`; note that that already wraps children in `Container`, and already includes both the meta title as well as the H1 element.<docs><doc title="FastHTML quick start" desc="A brief overview of many FastHTML features"># Web Devs Quickstart
'''

# https://docs.fastht.ml/

# pip install python-fasthtml

# from fasthtml.common import *

# '''We instantiate a FastHTML app with the `fast_app()` utility function.
# This provides a number of really useful defaults that we’ll take
# advantage of later in the tutorial.'''
# app,rt = fast_app()

# '''We use the `rt()` decorator to tell FastHTML what to return when a user
# visits `/` in their browser.
# We connect this route to HTTP GET requests by defining a view function
# called `get()`'''
# @rt('/')
# def get(): return Div(P('Hello World!'), hx_get="/change")

# @rt('/change')
# def get(): return P('Nice to be here!')

# '''The serve() utility configures and runs FastHTML using a library 
# called `uvicorn`.'''
# serve()


"""
Sometimes useful not to import * but rather use a namespace so that options are presented in the IDE.
"""
# Adding live=True will ensure that it automatically updates on saving file.
# from fasthtml import common as fh
# app,rt = fh.fast_app(live=True)
# @rt('/')
# def get(): return fh.Div(fh.P('Hello Everyone!'))
# fh.serve()

# Add title for page and tab
# from fasthtml.common import *
# app,rt = fast_app(live=True)
# @rt('/')
# def get():
#     return Titled("Greeting",
#                   Div(P('Hello Everyone!'))
#     )
# serve()

# Add clickable link (which then requires a new route)
from fasthtml.common import *
app,rt = fast_app(live=True)
@rt('/')
def get():
    return Titled("Greeting",
                  Div(P('Hello Everyone!')),
                  P(A('Link', href='/change'))
                  )
@rt('/change')
def get():
    return Titled("Sub-page",
                  P('Nice to see you!'),
                  P(A('Home', href='/'))
                  )

serve()