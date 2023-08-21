from unit_test_workshop.use_case import enter_data_flow, send_email

import pytest
import re
class TestUseCase:
    email_address_pattern = re.compile(r".*email_address.*")

    def test_not_a_use_case_test(self):
        """
        Given:
        Empty dict, without data
        
        When:
        The user sends an empty dict by mistake

        Then:
        check that an error is raised
        """
        # prepare data
        data = {}

        # run the test (also check for response)
        with pytest.raises(KeyError, match=self.email_address_pattern):
            send_email(data)


    def test_a_use_case_test(self):
        """
        Given:
        Empty dict, without data
        
        When:
        The user sends an empty dict by mistake

        Then:
        check that an error is raised
        """
        # prepare data
        data = {
            "id": "h231bj3v12b"
        }

        # run the test (also check for response)
        with pytest.raises(KeyError, match=self.email_address_pattern):
            enter_data_flow(data)