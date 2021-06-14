from django.forms import ClearableFileInput as BaseFileInput


class ClearableFileInput(BaseFileInput):
    """Modified ClearableFileInput widget, with custom template."""

    template_name = 'widget.html'
    omit_value = False
    initial_text = 'Currently'
    input_text = 'Change'
    clear_checkbox_label = 'Clear'
