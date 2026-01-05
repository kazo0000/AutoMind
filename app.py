"""
Flask web application for the AutoMind MVP.

This minimal server exposes a simple form for entering user preferences,
generates a shortlist of cars based on a static dataset, and provides
an extended report for individual models. The business logic is
encapsulated in the ``core`` package, which can be extended later to
integrate real data sources, machine learning models, authentication and
payment systems.
"""

from flask import Flask, render_template, request
from core.shortlist import generate_shortlist
from core.report import generate_report


def create_app() -> Flask:
    """Factory to create and configure the Flask application."""
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Render the main page with a form and optionally the shortlist."""
        if request.method == 'POST':
            # Extract user preferences from form input
            budget_input = request.form.get('budget')
            try:
                budget = float(budget_input) if budget_input else None
            except ValueError:
                budget = None
            fuel_type = request.form.get('fuel_type') or 'any'
            body_type = request.form.get('body_type') or 'any'
            preferences = {
                'budget': budget,
                'fuel_type': fuel_type,
                'body_type': body_type,
            }
            shortlist = generate_shortlist(preferences, top_n=5)
            return render_template('shortlist.html', shortlist=shortlist)
        return render_template('index.html')

    @app.route('/report/<int:car_id>')
    def report(car_id: int):
        """Return a detailed report for a single car model."""
        report_data = generate_report(car_id)
        if report_data is None:
            return "Report not found", 404
        return render_template('report.html', report=report_data)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
