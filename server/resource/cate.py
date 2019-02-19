import json
from datetime import datetime, timedelta

from flask import make_response, jsonify
from flask_restful import Resource

from models import Category, db
from utility import clean_list

class CategoryView(Resource):
    """RESTful api for category"""

    def get(self):
        items = clean_list(db.session.query(Category).all())

        json_data = json.dumps(items, ensure_ascii=False, indent=4)
        res = make_response(json_data)
        res.headers["Content-Type"] = "application/json;charset=utf-8"
        res.status_code = 200

        return res