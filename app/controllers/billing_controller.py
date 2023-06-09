from flask import Blueprint, request, jsonify
from app.services.billing_service import BillingService


billing_bp = Blueprint("billing", __name__, url_prefix="/billing")
billing_service = BillingService()


@billing_bp.route("/perform_advance", methods=["POST"])
def perform_advance():
    data = request.get_json()
    dst_bank_account = data.get("dst_bank_account")
    amount = data.get("amount")

    try:
        transaction_id = billing_service.perform_advance(
            dst_bank_account, amount)
        return jsonify({"transaction_id": transaction_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@billing_bp.route("/transactions/<transaction_id>", methods=["GET"])
def get_transaction(transaction_id):
    transaction = billing_service.get_transaction(transaction_id)
    if transaction:
        return jsonify(transaction)
    return jsonify({"error": "Transaction not found"}), 404


@billing_bp.route("/transactions", methods=["GET"])
def get_all_transactions():
    transactions = billing_service.get_all_transactions()
    return jsonify(transactions)
