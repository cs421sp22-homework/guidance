from .._utils import strip_markers, ContentCapture

async def role(name, hidden=False, _parser_context=None):
    ''' A chat role block.
    '''
    block_content = _parser_context['block_content']
    parser = _parser_context['parser']
    variable_stack = _parser_context['variable_stack']

    # capture the content of the block
    with ContentCapture(variable_stack, hidden) as new_content:
        
        # send the role-start special tokens
        new_content += parser.program.llm.role_start(name)

        # visit the block content
        new_content += await parser.visit(
            block_content,
            variable_stack,
            next_node=_parser_context["block_close_node"],
            prev_node=_parser_context["prev_node"],
            next_next_node=_parser_context["next_node"]
        )

        # send the role-end special tokens
        new_content += parser.program.llm.role_end(name)
role.is_block = True