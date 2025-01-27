"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        # setup runs automatically before each test method and gives initial values
        self.client = Client(1, "Rogine", "Mirando", "rmirando2@rrc.ca")

    def test_init_valid(self):
        # Arrange & Act
        client = Client(1, "Rogine", "Mirando", "rmirando2@rrc.ca")

        # Assert
        self.assertEqual(client.client_number, 1)
        self.assertEqual(client.first_name, "Rogine")
        self.assertEqual(client.last_name, "Mirando")
        self.assertEqual(client.email_address, "rmirando2@rrc.ca")

    def test_invalid_client_number(self):
        # Arrange & Assert
        with self.assertRaises(ValueError):
            client = Client(1.2, "Rogine", "Mirando", "rmirando2@rrc.ca")

    def test_invalid_first_name(self):
        # Arrange & Assert
        with self.assertRaises(ValueError):
            client = Client(1, " ", "Mirando", "rmirando2@rrc.ca")

    def test_invalid_last_name(self):
        # Arrange & Assert
        with self.assertRaises(ValueError):
            client = Client(1, "Rogine", " ", "rmirando2@rrc.ca")

    def test_invalid_email_address(self):
        # Arrange & Assert
        with self.assertRaises(ValueError):
            client = Client(1, "Rogine", "Mirando", "rmirando")

    def test_valid_client_number(self):
        # Setup done above

        # Assert
        self.assertEqual(self.client.client_number, 1)

    def test_valid_first_number(self):
        # Setup done above

        # Assert
        self.assertEqual(self.client.first_name, "Rogine")

    def test_valid_last_name(self):
        # Setup done above

        # Assert
        self.assertEqual(self.client.last_name, "Mirando")

    def test_valid_email_address(self):
        # Setup done above

        # Assert
        self.assertEqual(self.client.email_address, "rmirando2@rrc.ca")

    def test_str_(self):
        # Arrange
        expected = ("Mirando, Rogine, [1] - rmirando2@rrc.ca")

        # Assert
        self.assertEqual(expected, str(self.client))
