'''
Module handles the creation of schedules.
'''

from flask import abort, current_app as app


def on_insert_schedule(items):
    data = app.data

    def search_user(schedule):
        doc = data.find_one_raw('outbuilding', 
                                **{'_id': schedule['outbuilding'],})
        if doc is None:
            abort(422, 'Failed to get outbuilding')
        return doc['user']

    for schedule in items:
        schedule['user'] = search_user(schedule)

        # TODO verify whether is confirmed
        schedule['confirmed'] = True


def register_hooks(app):
    app.on_insert_schedule += on_insert_schedule