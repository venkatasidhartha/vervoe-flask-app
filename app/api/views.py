from flask import Blueprint, request, jsonify,current_app
import requests
from app.api.process import (DataProcessing,DataProcessed)
from app.api.error_capture import capture_error
import logging

api = Blueprint('api',__name__)



@api.route('/fetch-data')
@capture_error
def fetch_process_data():
    service = DataProcessing()
    response = service.start_process()
    return jsonify(response),200

@api.route('/get-processed-data')
@capture_error
def get_processed_data():
    page_no = int(request.args.get("page_no",1))
    page_length = int(request.args.get("page_length",10))
    service = DataProcessed()
    response = service.get_processedData(page_no=page_no,page_length=page_length)
    return jsonify(response),200

