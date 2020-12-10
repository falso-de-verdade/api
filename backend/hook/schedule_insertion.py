'''
Module handles the creation of schedules.
'''

from flask import abort, current_app as app


def handle_schedule(items, *args):
    data = app.data

    def search_outbuilding(schedule):
        doc = data.find_one_raw('outbuilding', 
                                **{'_id': schedule['outbuilding'],})
        if doc is None:
            abort(422, 'Failed to get outbuilding')
        return doc

    schedules = app.data.driver.db['schedule'].find()

    for schedule in items:
        outb = search_outbuilding(schedule)
        schedule['user'] = outb['user']

        collision = check_collision(schedule, schedules)

        schedule['confirmed'] = collision is None

        if not schedule['confirmed']:
            upsert_collision(schedule, collision)
    

def check_collision(schedule, schedules):
    day = schedule['day']
    for existing in schedules:
        if day == existing['day']:
            return existing


def upsert_collision(schedule, collision):
    lookup = {
        'schedule': collision['_id']
    }

    existing_collision = app.data.find_one_raw('collision', 
                                               **lookup)
    if not existing_collision:
        _id = app.data.insert('collision', lookup)[0]
        existing_collision = {
            '_id': _id,
        }
    
    collision_item = {
        'collision': existing_collision['_id'],
        'schedule': schedule['_id'],
    }

    app.data.insert('collisionitem', collision_item)


def register_hooks(app):
    app.on_inserted_schedule += handle_schedule
    app.on_update_schedule += handle_schedule