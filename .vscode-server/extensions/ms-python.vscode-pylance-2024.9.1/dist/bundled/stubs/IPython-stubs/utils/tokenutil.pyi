"""
This type stub file was generated by pyright.
"""

"""Token-related utilities"""
Token = ...
def generate_tokens(readline):
    """wrap generate_tokens to catch EOF errors"""
    ...

def line_at_cursor(cell, cursor_pos=...):
    """Return the line in a cell at a given cursor position

    Used for calling line-based APIs that don't support multi-line input, yet.

    Parameters
    ----------
    cell : str
        multiline block of text
    cursor_pos : integer
        the cursor position

    Returns
    -------
    (line, offset): (string, integer)
        The line with the current cursor, and the character offset of the start of the line.
    """
    ...

def token_at_cursor(cell, cursor_pos=...):
    """Get the token at a given cursor

    Used for introspection.

    Function calls are prioritized, so the token for the callable will be returned
    if the cursor is anywhere inside the call.

    Parameters
    ----------
    cell : unicode
        A block of Python code
    cursor_pos : int
        The location of the cursor in the block where the token should be found
    """
    ...

