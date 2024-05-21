from faction_wars.database_interface.models import Account, Player , Events


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

class AsyncAccountDataAccess:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_account(self, username: str, password: str) -> Account:
        account = Account(username=username, password=password)
        self.session.add(account)
        await self.session.commit()
        return account

    async def delete_account(self, account_id: int) -> bool:
        stmt = delete(Account).where(Account.id == account_id)
        await self.session.execute(stmt)
        await self.session.commit()
        return True

    async def get_all_accounts(self) -> list[Account]:
        result = await self.session.execute(select(Account))
        return result.scalars().all()

class AsyncPlayerDataAccess:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_players(self) -> list[Player]:
        result = await self.session.execute(select(Player))
        return result.scalars().all()
    
    async def get_account_by_player_id(self, player_id: int) -> Account:
        result = await self.session.execute(select(Account).where(Account.player_id == player_id))
        return result.scalars().first()

class AsyncEventDataAccess:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_events(self) -> list[dict]:
        result = await self.session.execute(select(Events))
        return result.scalars().all()