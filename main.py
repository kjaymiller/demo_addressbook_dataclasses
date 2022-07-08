import addressbook

jay = addressbook.Person(name="Jay", twitter="@kjaymiller")
nina = addressbook.Person(name="Nina", twitter="@nnja")
anthony = addressbook.Person(name="Anthony", twitter="@anthonypjshaw")
sarah = addressbook.Person(name="Sarah", twitter="@crazy4pi314")
pamela = addressbook.Person(name="Pamela", twitter="@pamelafox")

MS_Python = addressbook.Team(
    name = "Team Python",
    members = [jay, sarah, nina, anthony, pamela]
)

def get_twitter_accounts_to_follow(team: addressbook.Team):
    """return a list of all the team members twitter accounts"""
    return "\n".join([member.get_twitter_url for member in team.members])


if __name__ == "__main__":
    print(get_twitter_accounts_to_follow(MS_Python))