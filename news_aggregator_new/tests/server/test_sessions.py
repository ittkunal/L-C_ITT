def test_session_creation(client):
    # Simulate login to create a session
    resp = client.post("/auth/signup", json={
        "username": "sessionuser",
        "email": "sessionuser@example.com",
        "password": "testpass123"
    })
    assert resp.status_code == 200 or resp.status_code == 400  # May already exist

    resp = client.post("/auth/login", json={
        "email": "sessionuser@example.com",
        "password": "testpass123"
    })
    assert resp.status_code == 200
    assert "user_id" in resp.json()