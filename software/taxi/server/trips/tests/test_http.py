from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

PASSWORD = "pAssw0rd!"


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
