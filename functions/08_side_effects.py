import mock
UserGateway = mock.Mock()
Session = mock.Mock()
cryptographer = mock.Mock()


class UserValidator:
    cryptographer = None

    def check_password(self, user_name, password):
        user = UserGateway.findByName(user_name)
        if user is not None:
            coded_phrase = user.getPhraseEncodedByPassword()
            phrase = cryptographer.decrypt(coded_phrase, password)
            if "Valid Password".equals(phrase):
                Session.initialize()
                return True
        return False
