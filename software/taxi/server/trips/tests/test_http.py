from base64 import b64decode
from json import loads

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

PASSWORD = "pAssw0rd!"

# helper function
def create_user(username="user@example.com", password=PASSWORD):  # new
    return get_user_model().objects.create_user(
        username=username, first_name="Test", last_name="User", password=password
    )


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self) -> None:
        """
        Tests user account creation
        """

        # given
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "user@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": PASSWORD,
                "password2": PASSWORD,
            },
        )
        # when
        user = get_user_model().objects.last()

        # then
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data["id"], user.id)
        self.assertEqual(response.data["username"], user.username)
        self.assertEqual(response.data["first_name"], user.first_name)
        self.assertEqual(response.data["last_name"], user.last_name)

    def test_when_passwords_do_not_match(self) -> None:
        """
        Tests user account creation when the passwords don't match.
        Should raise an error
        """

        # given
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "user@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": PASSWORD,
                "password2": "another_password",
            },
        )

        # when
        error = response.data["non_field_errors"][0]

        # then
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        assert error == "Passwords must match."

    def test_user_can_log_in(self):
        """
        Tests if the user can log in successfully
        """
        user = create_user()
        response = self.client.post(
            reverse("log_in"),
            data={
                "username": user.username,
                "password": PASSWORD,
            },
        )

        # Parse payload data from access token.
        access = response.data["access"]
        header, payload, signature = access.split(".")
        decoded_payload = b64decode(f"{payload}==")
        payload_data = loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data["refresh"])
        self.assertEqual(payload_data["id"], user.id)
        self.assertEqual(payload_data["username"], user.username)
        self.assertEqual(payload_data["first_name"], user.first_name)
        self.assertEqual(payload_data["last_name"], user.last_name)
