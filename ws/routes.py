from aiohttp import web
from ws import handler


def setup(app, resources, websocket_handler, graphs_handler):
    index_handler = handler.index.Handler(resources)
    collections_handler = handler.collections.Handler(resources)
    collection_handler = handler.collection.Handler(resources)
    appliance_handler = handler.appliance.Handler(resources)
    event_enable_handler = handler.appliance.enable.Handler(resources)
    send_to_collection_handler = handler.appliance.send_to_collection.Handler(resources)
    send_to_others_handler = handler.appliance.send_to_others.Handler(resources)
    apply_to_collection_handler = handler.appliance.apply_to_collection.Handler(
        resources
    )
    apply_to_others_handler = handler.appliance.apply_to_others.Handler(resources)
    history_handler = handler.history.Handler(resources)
    details_handler = handler.details.Handler(resources)
    editor_handler = handler.editor.Handler(resources)
    login_handler = handler.login.Handler(resources)
    logout_handler = handler.logout.Handler(resources)
    collection_regexp = r"/collection/{name}"
    appliance_regexp = r"/appliance/{name}"
    event_enable_regexp = r"/appliance/{name}/enable"
    send_to_collection_regexp = r"/appliance/{name}/send_to_collection"
    send_to_others_regexp = r"/appliance/{name}/send_to_others"
    apply_to_collection_regexp = r"/appliance/{name}/apply_to_collection"
    apply_to_others_regexp = r"/appliance/{name}/apply_to_others"
    history_regexp = r"/appliance/{name}/history"
    graphs_regexp = r"/appliance/{name}/graphs"
    details_regexp = r"/appliance/{name}/details"
    app.router.add_routes(
        [
            web.get("/", index_handler.get),
            web.get("/index", index_handler.get),
            web.get("/collections", collections_handler.get),
            web.get("/ws", websocket_handler.get),
            web.get("/editor", editor_handler.get),
            web.post("/editor", editor_handler.post),
            web.post("/login", login_handler.post),
            web.post("/logout", logout_handler.post),
            web.get(collection_regexp, collection_handler.get),
            web.post(appliance_regexp, appliance_handler.post),
            web.get(appliance_regexp, appliance_handler.get),
            web.post(event_enable_regexp, event_enable_handler.post),
            web.post(send_to_collection_regexp, send_to_collection_handler.post),
            web.post(send_to_others_regexp, send_to_others_handler.post),
            web.post(apply_to_collection_regexp, apply_to_collection_handler.post),
            web.post(apply_to_others_regexp, apply_to_others_handler.post),
            web.get(history_regexp, history_handler.get),
            web.post(history_regexp, history_handler.post),
            web.get(details_regexp, details_handler.get),
        ]
    )

    app.router.add_resource(collection_regexp, name="collection")
    app.router.add_resource(appliance_regexp, name="appliance")
    app.router.add_resource(event_enable_regexp, name="event_enable")
    app.router.add_resource(send_to_collection_regexp, name="send_to_collection")
    app.router.add_resource(send_to_others_regexp, name="send_to_others")
    app.router.add_resource(apply_to_collection_regexp, name="apply_to_collection")
    app.router.add_resource(apply_to_others_regexp, name="apply_to_others")
    app.router.add_resource(history_regexp, name="history")
    app.router.add_resource(details_regexp, name="details")

    if graphs_handler:
        app.router.add_routes(
            [
                web.get(graphs_regexp, graphs_handler.get),
                web.post(graphs_regexp, graphs_handler.post),
            ]
        )
    app.router.add_resource(graphs_regexp, name="graphs")
