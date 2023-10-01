__all__ = (
    'VerifyTokenRequest',
    'DeepLinkCreationRequest'
)


class VerifyTokenRequest:
    def __init__(self, token):
        self.token = token
        return

    def to_dict(self):
        return {'token': self.token}

    def __str__(self):
        return f"VerifyTokenRequest({self.token})"

    def __repr__(self):
        return f"VerifyTokenRequest(token={self.token}, dict={self.to_dict()})"


class DeepLinkCreationRequest:
    def __init__(self, player_tags, clan_tag, opponent_clan_tag):
        self.player_tags = player_tags
        self.clan_tag = clan_tag
        self.opponent_clan_tag = opponent_clan_tag
        return
