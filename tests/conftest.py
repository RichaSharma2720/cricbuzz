# import pytest
# from cricbuzz.app import create_app
#
# @pytest.fixture(scope="module")
# def app():
#     app = create_app('dev')
#     app.app_context().push()
#     yield app
#     app.app_context().pop()
#
#
# @pytest.fixture(scope='module', autouse=True)
# def teardown():
#     # Teardown code
#     pass