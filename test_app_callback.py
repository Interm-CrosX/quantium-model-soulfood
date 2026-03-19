from asyncio import timeout

import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app('soul_food_visualiser')

def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element('#header')
    assert header.text == 'PINK MORSEL SALES DATA'


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    radio = dash_duo.find_element('#region-radio')
    assert radio is not None


def test_sales_chart_visualiser_present(dash_duo, app):
    dash_duo.start_server(app)
    chart = dash_duo.wait_for_element("#pinkM_Sales")
    assert chart is not None
