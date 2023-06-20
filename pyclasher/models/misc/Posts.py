class VerifyTokenRequest:
    def __init__(self, token: str):
        self.token = token
        return

    def to_dict(self) -> dict:
        return {'token': self.token}

    def __str__(self) -> str:
        return f"VerifyTokenRequest({self.token})"

    def __repr__(self) -> str:
        return f"VerifyTokenRequest(token={self.token}, dict={self.to_dict()})"


class DeepLinkCreationRequest:
    def __init__(self, player_tags: list[str], clan_tag: str, opponent_clan_tag: str):
        self.player_tags = player_tags
        self.clan_tag = clan_tag
        self.opponent_clan_tag = opponent_clan_tag
        return
