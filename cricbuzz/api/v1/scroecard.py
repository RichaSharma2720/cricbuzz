from flask import Flask, jsonify, request
from flask_restx import Resource, Namespace
import logging
import logging.config

log = logging.getLogger(__name__)



api = Namespace('test', description='scroe card')

@api.route('')
class Something(Resource):

    def get(self):
        log.info("came inside")
        log.info("sadasdasds")
        return "Welocme"