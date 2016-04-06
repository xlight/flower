from flower.utils.template import humanize

def format_task(task):
    task.args = humanize(task.args, length=100)
    #task.kwargs.pop('credit_card_number')
    task.result = humanize(task.result, length=100)
    return task
