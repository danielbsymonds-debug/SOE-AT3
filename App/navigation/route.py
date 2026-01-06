from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required
from App.models import Location, Path

nav_bp = Blueprint("nav", __name__)

@nav_bp.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html")

@nav_bp.route("/api/locations")
def get_locations():
    locations = Location.query.all()
    return jsonify([
        {"id": loc.id, "name": loc.name, "lat": loc.lat, "lon": loc.lon}
        for loc in locations
    ])

@nav_bp.route("/api/paths")
def get_paths():
    paths = Path.query.all()
    return jsonify([
        {"from": p.from_id, "to": p.to_id, "distance": p.distance, "accessible": p.accessible}
        for p in paths
    ])