from flask import request, jsonify, g
from modules.app import mongo
from modules.app.api import api
from modules.logger import log
from modules.app import groups


@api.route('/api/user', methods=['GET'])
def get_users():
    query = request.args
    log.info("search users", query=query, client=g.user['_id'])
    users = [u for u in mongo.db.users.find(
        query, {'last_changed_by': 0, 'last_changed_on': 0})]
    return jsonify(users), 200


@api.route('/api/user/<string:id>', methods=['GET'])
def get_user(id):
    log.info("get user", id=id, client=g.user['_id'])
    user: dict = mongo.db.users.find_one(
        {'shib_id': id}, {'last_changed_by': 0, 'last_changed_on': 0})
    if not user:
        return jsonify(), 404
    gms = groups.get_for_one(id, ['uw_rit_kpmp_role_developer', 'uw_rit_kpmp_app_userportal'])
    user.update({'groups':gms})
    return jsonify(user), 200
