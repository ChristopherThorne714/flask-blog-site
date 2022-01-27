"""
Pytest
"""
from app import app

def test1():
    """
    This function tests that the flask application has a correct response code
    when the application goes live
    """
    response = app.test_client().get("/info")
    assert response.status_code == 200

def test2():
    """Dummy docstring"""
    response = app.test_client().get("/login")
    assert response.status_code == 200
    
def test3():
    """Dummy docstring"""
    response = app.test_client().get("/")
    assert response.status_code == 200

def test3():
    """Dummy docstring"""
    response = app.test_client().get("/account")
    assert response.status_code == 200

def test5():
    """Dummy docstring"""
    response = app.test_client().get("/register")
    #test if the string is on the page
    assert b"Email" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    #assert b"Project" in response.data

