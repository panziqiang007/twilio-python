# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.lookups.v1.phone_number import PhoneNumberList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Lookups

        :returns: V1 version of Lookups
        :rtype: V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._phone_numbers = None

    @property
    def phone_numbers(self):
        """
        :rtype: PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(self)
        return self._phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V1>'
