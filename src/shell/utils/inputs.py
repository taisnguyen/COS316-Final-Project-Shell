"""Utility functions for inputting."""


def input_options(prompt, options_to_handlers, case_sensitive=False, default_handler=None):
    """Function to prompt options to user."""

    try:
        normalized_opts_to_handlers = {(opt.lower(
        ) if not case_sensitive else opt): options_to_handlers[opt] for opt in options_to_handlers}

        displayed_prompt = f"{prompt} ({'/'.join([opt for opt in options_to_handlers])}) "

        user_input = input(displayed_prompt)
        while ((user_input.lower() if not case_sensitive else user_input) not in normalized_opts_to_handlers):
            if default_handler:
                default_handler()
                break

            print()
            user_input = input(displayed_prompt)

        # Call handler.
        handler_func = normalized_opts_to_handlers[user_input.lower(
        ) if not case_sensitive else user_input]
        if handler_func:
            handler_func()
        print()

        return user_input

    except:
        if default_handler:
            print()
            default_handler()
