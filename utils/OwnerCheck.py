class Owner:
    async def isOwner(self, bot, user_id: int):
            owner = bot.owner_ids
            for id in owner:
                if id == user_id:
                    return True
            return False