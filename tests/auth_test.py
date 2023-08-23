from unit_test_workshop.auth import (
    NotAuthorizedException,
    User,
    authorize_user,
    validate_roles,
)


def test_validate_roles():
    """
    Given:
        required_roles is a subset of the user_roles

    When:
        we need to validate if a user has the right roles

    Then:
        Check that the response did not raise an error and returned with True
    """
    # Arrange
    required_roles = ["wonderwoman"]
    user_roles = ["wonderwoman", "superman"]

    # Act
    resp = validate_roles(required_roles, user_roles)

    # Assert
    assert resp is True


def test_authorize_user_with_existing_user():
    """
    Given:
        username: that exists in the database
        password: matching the password in the database
        required_roles: that the user has
        database: a mock that returns a user with roles

    When:
        a user tries to call an endpoint that he can use

    Then:
        validate that the user returned is the correct user
    """
    # Arrange
    username = "marwa"
    password = "123"
    roles = ["wonderwoman"]

    class Database:
        def get_user(self, _username, _password) -> User:
            if _username == username and _password == password:
                return User(name=username, roles=roles)
            raise NotAuthorizedException()

    # Act
    user = authorize_user(Database(), username, password, roles)  # type: ignore

    # Assert
    assert username == user["name"]
